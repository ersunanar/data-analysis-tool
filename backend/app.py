from flask import Flask, flash, request, redirect, url_for, send_from_directory, jsonify, render_template
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

#https://python.plainenglish.io/implementing-flask-login-with-hash-password-888731c88a99
from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask_cors import CORS, cross_origin
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import datetime
import mysql.connector


df = pd.DataFrame()

mysql_user = ''
mysql_password = ''
mysql_tablename = ''
active_user = ''
user_file = './user_files'
ALLOWED_EXTENSIONS = set(['csv','xls','xlsx', 'db', 'sqlite','sqlite3','json','txt'])



app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = user_file



#https://python-adv-web-apps.readthedocs.io/en/latest/flask_db2.html


db_name = './users.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String, nullable=False, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    



Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/')
def mainpage():
    return  "<h1>Server Running....<h1>"


@app.route('/deneme')
def mainpage2():
    return  {"name":"ersun", "surname": "anar"}


################# LOG IN #################

@app.route('/user',methods=["GET", "POST"])
def getUser():
  if request.method == "POST":    
    post_data = request.get_json()
    user_for_tool = User.query.filter_by(username=post_data['user']).first()
    if check_password_hash(user_for_tool.password, post_data['password']):      
      return {
        'username':user_for_tool.username,
        'name':user_for_tool.name,
        'surname':user_for_tool.surname,
        'email':user_for_tool.email
        }
    else:
      return 'wrong credentials'


################# FILE UPLOADING #################

@app.route('/upload/<active_user>',methods=["POST","GET"])
def upload_file(active_user):
  if request.method == 'POST':
    print(request.files.getlist('file'))
    for file in request.files.getlist('file'):
      print(file.filename)
      if file and file.filename.split('.')[-1].lower() in ALLOWED_EXTENSIONS:
        filename = secure_filename(file.filename)
        file.save(os.path.join(user_file, active_user, filename))
    return listFiles(active_user)


  
################# GETTING DATA FROM (.xlsx, .xls, .json, .csv) FILE #################

@app.route('/data/<active_user>/<file_name>',methods=["GET"])
def getData(active_user,file_name):
  try:
    print(datetime.datetime.now(),"başladı")   # LOG -1 : başladı
    if file_name.split('.')[-1].lower() in ['csv','txt']:
      df = pd.read_csv(os.path.join(user_file,active_user, file_name),  encoding='utf-8-sig')
    elif file_name.split('.')[-1].lower() in ['xlsx','xls']:
      df = pd.read_excel(os.path.join(user_file, active_user, file_name))
    elif file_name.split('.')[-1].lower() == 'json':
      df = pd.read_json(os.path.join(user_file, active_user, file_name))  
    print(df.head(5))
    print(datetime.datetime.now(), "dosyayı okudu") # LOG -2 : dosyayı okudu
    df_json = df.to_json(orient='records') 
    print(datetime.datetime.now(), "json'a dönüştü")  # LOG -3 : json'a dönüştirme işlemi bitti
    print(df.shape)  
    return  df_json
  except:
    return "the file can not be read"


################# GETTING DATA FROM THE TABLE IN SQLITE FILE #################

@app.route('/sqlite/<active_user>/<dbname>/<file_name>',methods=["GET"])
def getDBData(active_user,dbname, file_name):
  try:
    print(datetime.datetime.now(),"başladı")  # LOG -1 : başladı
    con = sqlite3.connect(os.path.join(user_file, active_user, dbname))
    print(datetime.datetime.now(),"database bağlantısı ") # LOG -2 : sqlite'a bağlanıldı
    df = pd.read_sql_query("SELECT * from " + file_name, con)
    print(datetime.datetime.now(),"sql'i okudu")  # LOG -3  : sql'i okudu  
    con.close()
    print(datetime.datetime.now(),"bağlantı kapandı") # LOG -4 : bağlantı sonlandırıldı
    df_json= df.to_json(orient='records')
    print(datetime.datetime.now(),"json'a dönüştü") # LOG -5 : json'a dönüştirme işlemi bitti
    print(df.shape)  
    return df_json
  except:
    return "the query can not be executed"


################# GETTING DATA FROM THE TABLE IN MYSQL SERVER #################

@app.route('/mysql',methods=["GET", "POST"])
def getMySQLData():
  if request.method == "POST":
    try:
      post_data = request.get_json()
      print(datetime.datetime.now(),"başladı")  # LOG -1 : başladı
      con = mysql.connector.connect(host="localhost",user = post_data['user'] , password = post_data['password'], database= post_data['schema'])
      print(datetime.datetime.now(),"database bağlantısı ") # LOG -2 : mysql'e bağlanıldı  
      df = pd.read_sql_query("SELECT * from " + post_data['tablename'], con)
      print(datetime.datetime.now(),"sql'i okudu")  # LOG -3  : sql'i okudu  
      con.close()
      print(datetime.datetime.now(),"bağlantı kapandı") # LOG -4 : bağlantı sonlandırıldı
      df_json= df.to_json(orient='records')
      print(datetime.datetime.now(),"json'a dönüştü") # LOG -5 : json'a dönüştirme işlemi bitti
      print(df.shape)  
      return df_json
    except:
      return "can not be connected to server"

################# GETTING FILE LIST #################

@app.route('/files/<active_user>', methods=["GET"])
def listFiles(active_user):
  myfiles = {'excelcsvtxt' : [], 'dbsqlite': []}  
  file_list = os.listdir(os.path.join(user_file,active_user))
  for file in file_list:
    if file.split('.')[-1].lower() in ('xlsx', 'xls', 'csv', 'txt', 'json'):
      myfiles['excelcsvtxt'].append(file)
    elif file.split('.')[-1].lower() in ('db', 'sqlite', 'sqlite3'):
      myfiles['dbsqlite'].append(file)            
  return jsonify(myfiles)


################# GETTING TABLE LIST OF A SQLITE FILE #################

@app.route('/sqlitetables/<active_user>/<filename>', methods=["GET"])
def listSqliteTables(active_user, filename):
  sqlite_table_list = []
  con = sqlite3.connect(os.path.join(user_file,active_user,filename))
  cursor = con.cursor()
  cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
  db_tables = cursor.fetchall()
  for table_name in db_tables:
    table_name = table_name[0]
    sqlite_table_list.append(table_name)
  cursor.close()
  con.close()      
  return jsonify(sqlite_table_list)


################# GETTING SCHEMAS IN THE MYSQL SERVER #################

@app.route('/mysql_schemas',methods=["GET", "POST"])
def listMySQLSchemas():
  if request.method == "POST":
    print(request)
    post_data = request.get_json()
    print(post_data)
    mysql_user  = post_data['user']
    mysql_password  = post_data['password']
    print(mysql_user, mysql_password)  
  mysqlschemas = []  
  try:
    cnx = mysql.connector.connect(host="localhost", user=mysql_user, password=mysql_password)
    cur = cnx.cursor()
    cur.execute("SHOW DATABASES")
    schemas = cur.fetchall()    
    for schema in schemas:
      if schema[0] not in ["information_schema","mysql", "performance_schema",  "sys"]:
        mysqlschemas.append(schema[0])    
    cnx.close()
    print(mysqlschemas)
    return jsonify(mysqlschemas)
  except:
    return "can not be connected to server"
  

################# GETTING TABLE LIST OF A SCHEMA IN THE MYSQL SERVER #################

@app.route('/mysql_schema_tables',methods=["GET", "POST"])
def listMySQLTables():  
  if request.method == "POST":
    post_data = request.get_json()    
    mysql_tables = []
    cnx = mysql.connector.connect(host="localhost",user = post_data['user'] , password = post_data['password'])  
    cur = cnx.cursor()  
    cur.execute("USE " + post_data['schema'])
    cur.execute("SHOW TABLES")
    tables = cur.fetchall()
    for table in tables:
      mysql_tables.append(table[0])
    cnx.close()    
  return jsonify(mysql_tables)



################# DELETING FILE (.xlsx, .xls, .csv, .json, .sqlite3, .sqlite, .db) #################


@app.route('/deleting/<active_user>/<file_name>',methods=["GET"])
def deleteFile(active_user,file_name):
  try:
    os.remove(os.path.join(user_file,active_user, file_name))
    return {'text':'the file was deleted'}
  except:
    return "the file can not be deleted"


################# DROPPING SQLITE TABLE #################

@app.route('/droptable/<active_user>/<filename>/<tablename>', methods=["GET"])
def dropSqliteTable(active_user, filename, tablename):  
  try:
    con = sqlite3.connect(os.path.join(user_file,active_user,filename))
    cursor = con.cursor()
    cursor.execute("DROP TABLE "+tablename)
    sqlite_table_list = []
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    db_tables = cursor.fetchall()
    for table_name in db_tables:
      table_name = table_name[0]
      sqlite_table_list.append(table_name)
    cursor.close()
    con.close()      
    return jsonify(sqlite_table_list)
  except:
    return "the table can not be dropped"



################# DELETING SCHEMA IN THE MYSQL SERVER #################

@app.route('/deleteschema',methods=["GET", "POST"])
def deleteSchema():
  mysqlschemas = []
  if request.method == "POST":
    try:
      post_data = request.get_json()
      cnx = mysql.connector.connect(host="localhost", user=post_data['user'], password=post_data['password'])
      cur = cnx.cursor()
      cur.execute("DROP DATABASE "+post_data['schema'])
      cur.execute("SHOW DATABASES")
      schemas = cur.fetchall()
      for schema in schemas:
        if schema[0] not in ["information_schema","mysql", "performance_schema",  "sys"]:
          mysqlschemas.append(schema[0])
      cnx.close()
      print(mysqlschemas)
      return jsonify(mysqlschemas)
    except:
      return "can not be connected to server"

  
################# DROPPING MYSQL TABLE #################
  
@app.route('/dropmysqltable',methods=["GET", "POST"])
def dropMySqlTable():
  mysql_tables = []
  if request.method == "POST":
    try:
      post_data = request.get_json()
      cnx = mysql.connector.connect(host="localhost",user = post_data['user'] , password = post_data['password'], database= post_data['schema'])
      cur = cnx.cursor()
      cur.execute("DROP TABLE " + post_data['table'])
      cur.execute("SHOW TABLES")
      tables = cur.fetchall()
      for table in tables:
        mysql_tables.append(table[0])
      cnx.close()
      print(mysql_tables)
      return jsonify(mysql_tables)
    except:
      return "can not be connected to server"


if __name__ == "__main__":
    app.run(debug=True)


