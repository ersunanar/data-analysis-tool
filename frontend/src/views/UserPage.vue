<template>
  <div id="app">

  <!--  // https://jsfiddle.net/mshaker88/u41rgq3e/ -->

<div v-if="spinnerstatus" id="overlay" >
    <div class="spinner"></div>
    <br/>
    Loading...
</div>


  <div>
    <!-- nav bar -->
    <nav
      class="navbar navbar-inverse navbar-fixed-top"
      style="background-color: DodgerBlue"
    >
      <div class="container-fluid">
        <div class="navbar-header">
          <div class="uploadbutton" @click="chooseFile()">
            <div class="uploadicon">
              <b-icon-cloud-upload></b-icon-cloud-upload>
            </div>
            <div class="uploadtext"><strong>UPLOAD FILE</strong></div>
          </div>
        </div>
        <div class="nav navbar-nav navbar-right">
          <div style="padding-right: 50px">
            <div class="dropdown">
              <button class="dropbtn">
                {{ this.$route.params.name }} {{ this.$route.params.surname }}
              </button>
              <div class="dropdown-content">
                <div class="logout" @click="logout()">log out</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <!-- upload form -->

    <form id="uploadform" hidden>
      <input
        id="fileUpload"
        name="files"
        type="file"
        ref="file_"
        accept=".xlsx, .xls, .csv , .db, .sqlite, .sqlite3, .txt, .json"
        @change="uploadFile"
      />
    </form>

    <!-- left menu div -->

    <div class="menu">
      <div>
        <div class="accordion" id="accordionPanelsStayOpenExample">
          <div class="accordion-item">
            <h2 class="accordion-header" id="panelsStayOpen-headingOne">
              <button
                id="accordion-one"
                class="accordion-button"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#panelsStayOpen-collapseOne"
                aria-expanded="true"
                aria-controls="panelsStayOpen-collapseOne"
              >
                excel - csv - json files (.xlsx, .xls, .csv, .txt, .json)
              </button>
            </h2>
            <div
              id="panelsStayOpen-collapseOne"
              class="accordion-collapse collapse show"
              aria-labelledby="panelsStayOpen-headingOne"
            >
              <div class="accordion-body">
                <div v-for="file in excelcsvtxt_files" :key="file">
                  <div
                    class="datafiles"
                    style="text-align:left"
                    @dblclick="getData(file)"
                  >
                    {{ file.toLowerCase() }}
                  </div>
                  <div class="trashicon" @click="deleteFile(file)">
                    <b-icon-trash></b-icon-trash>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <hr />
          <div class="accordion-item">
            <h2 class="accordion-header" id="panelsStayOpen-headingTwo">
              <button
                id="accordion-two"
                class="accordion-button collapsed"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#panelsStayOpen-collapseTwo"
                aria-expanded="false"
                aria-controls="panelsStayOpen-collapseTwo"
              >
                SQLite files (.db, .sqlite, .sqlite3)
              </button>
            </h2>
            <div
              id="panelsStayOpen-collapseTwo"
              class="accordion-collapse collapse"
              aria-labelledby="panelsStayOpen-headingTwo"
            >
              <div class="accordion-body">
                <br />
                <div>
                  <div align="left">
                    <span
                      ><strong style="color: #1873CC">sqlite file name:</strong>
                    </span>
                    <select
                      id="value_for_files"
                      @change="getSqliteDBName($event)"
                    >
                      <option value="">choose file</option>
                      <option
                        v-for="file in sqlite_files"
                        :value="file"
                        :key="file"
                        ><strong>{{ file }}</strong></option
                      >
                    </select>
                    <span class="trashicon" @click="deleteFile(sqlite_filename)"
                      ><b-icon-trash></b-icon-trash>
                    </span>
                  </div>
                  <br />
                  <div v-for="tablename in sqlite_table_list" :key="tablename">
                    <div
                      class="datafiles"
                      @dblclick="getDataFromSqlite(sqlite_filename, tablename)"
                    >
                      {{ tablename.toLowerCase() }}
                    </div>
                    <div
                      class="trashicon"
                      @click="dropTable(sqlite_filename, tablename)"
                    >
                      <b-icon-trash></b-icon-trash>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <hr />
          <div class="accordion-item">
            <h2 class="accordion-header" id="panelsStayOpen-headingThree">
              <button
                id="accordion-tree"
                class="accordion-button collapsed"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#panelsStayOpen-collapseThree"
                aria-expanded="false"
                aria-controls="panelsStayOpen-collapseThree"
              >
                MySQL Database
              </button>
            </h2>
            <div
              id="panelsStayOpen-collapseThree"
              class="accordion-collapse collapse"
              aria-labelledby="panelsStayOpen-headingThree"
            >
              <div class="accordion-body">
                <div>
                  <div>
                    <tr>
                      <td>
                        <input id="mysqlloginuser" style="width:100px"
                          class="mysqlform"
                          type="text"
                          v-model="username"
                          placeholder="username"
                        />
                      </td>
                      <td>
                        <input id="mysqlloginpassword"  style="width:100px"
                          class="mysqlform"
                          type="password"
                          v-model="password"
                          placeholder="password"
                        />
                      </td>
                      <td>
                        <button v-if="!isConnected" style="width:80px"
                          class="mysqlform" @click="getConnectToMySql()">
                          connect
                        </button>
                        <button v-if="isConnected"  style="width:80px"
                          class="mysqlform" @click="getDisConnectToMySql()">
                          disconnect
                        </button>
                      </td>
                    </tr>
                    <div v-if="warningmsgmysql">
                      <span class="warningmessagemysql"
                        >wrong credentials!!!</span
                      >
                    </div>
                  </div>

                  <br />
                  <div align="left">
                    <span>
                      <strong style="color: #1873CC"
                        >MySql schema name:
                      </strong>
                    </span>
                    <select
                      id="value_for_schema"
                      @change="getMySqlDBName($event)"
                    >
                      <option value="">choose schema</option>
                      <option
                        v-for="schema in mysql_schemas"
                        :value="schema"
                        :key="schema"
                        ><strong>{{ schema }}</strong></option
                      >
                    </select>
                    <span
                      v-if="schema !== ''"
                      class="trashicon"
                      @click="deleteSchema(schema)"
                      ><b-icon-trash></b-icon-trash>
                    </span>
                  </div>
                  <br />
                  <div v-for="table_name in mysql_tables" :key="table_name">
                    <div
                      class="datafiles"
                      @dblclick="getDataFromMySql(schema, table_name)"
                    >
                      {{ table_name }}
                    </div>
                    <div class="trashicon" @click="dropMySqlTable(table_name)">
                      <b-icon-trash></b-icon-trash>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- right menu div -->

    <div class="main">
      <div class="accordion-item">
        <h2 class="accordion-header" id="panelsStayOpen-headingFour">
          <button
            id="accordion-four"
            class="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#panelsStayOpen-collapseFour"
            aria-expanded="false"
            aria-controls="panelsStayOpen-collapseFour"
          >
            Data Table
          </button>
        </h2>
        <div
          id="panelsStayOpen-collapseFour"
          class="accordion-collapse collapse"
          aria-labelledby="panelsStayOpen-headingFour"
        >
          <div class="accordion-body">
            <div>


              <data-table
                :items="items"
                :fields="fields"
                :column_values="column_values"
                              
              ></data-table>

            </div>
          </div>
        </div>
      </div>

      <hr />

      <div class="accordion-item">
        <h2 class="accordion-header" id="panelsStayOpen-headingSix">
          <button
            id="accordion-six"
            class="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#panelsStayOpen-collapseSix"
            aria-expanded="false"
            aria-controls="panelsStayOpen-collapseSix"
          >
            Data Visualization
          </button>
        </h2>
        <div
          id="panelsStayOpen-collapseSix"
          class="accordion-collapse collapse"
          aria-labelledby="panelsStayOpen-headingSix"
        >
          <div class="accordion-body">
            <chart-view
              :items="items"
              :column_values="column_values"
            ></chart-view>
          </div>
        </div>
      </div>

      <hr />

      <div class="accordion-item">
        <h2 class="accordion-header" id="panelsStayOpen-headingFive">
          <button
            id="accordion-five"
            class="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#panelsStayOpen-collapseFive"
            aria-expanded="false"
            aria-controls="panelsStayOpen-collapseFive"
          >
            Pivot Table
          </button>
        </h2>
        <div
          id="panelsStayOpen-collapseFive"
          class="accordion-collapse collapse"
          aria-labelledby="panelsStayOpen-headingFive"
        >
          <div class="accordion-body">
            <div>
              <pivot-table :items="items"></pivot-table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<!--################################### SCRIPT ###################################-->

<script>
import axios from "axios";
import DataTable from "@/components/DataTable.vue";
import PivotTable from "@/components/PivotTable.vue";
import ChartView from "@/components/ChartView.vue";

export default {
  name: "UserPage",
  components: { ChartView, PivotTable, DataTable},
  data() {
    return {
      spinnerstatus : false,
      warningmsgmysql: false,
      excelcsvtxt_files: [],
      sqlite_files: [],
      sqlite_table_list: [],
      mysql_files: {},
      mysql_schemas: [],
      mysql_tables: [],
      schema: "",
      sqlite_filename: "",
      items: [],
      fields: [],
      column_values: [],
      username: "",
      password: "",
      file: "",
      isConnected : false,





    };
  },

  methods: {

    /************************** LOG OUT **************************/

    logout() {
      this.warningmsg = false;
      this.$store.commit("setAuthentication", false);
      this.$router.push({ name: "login" });
    },

    /************************** FILE UPLOAD **************************/

    chooseFile() {
      document.getElementById("fileUpload").click();
    },

    uploadFile() {
      const path =
        "http://127.0.0.1:5000/upload/" + this.$route.params.username;
      this.file = this.$refs.file_.files[0];
      let formData = new FormData();
      formData.append("file", this.file);      
      axios
        .post(path, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          this.excelcsvtxt_files = response["excelcsvtxt"];
          this.sqlite_files = response["dbsqlite"];
          this.getFileList();
        });
    },

    /************************** FILE LIST **************************/

    async getFileList() {
      this.excelcsvtxt_files = [];
      this.sqlite_files = [];
      const url_files =
        "http://127.0.0.1:5000/files/" + this.$route.params.username;
      fetch(url_files)
        .then((response) => {
          return response.json();
        })
        .then((response) => {
          this.excelcsvtxt_files = response["excelcsvtxt"];
          this.sqlite_files = response["dbsqlite"];
        });
    },

    /************************** CONNECT TO MYSQL **************************/

    getConnectToMySql() {
      const path = "http://127.0.0.1:5000/mysql_schemas";
      axios
        .post(path, {
          user: this.username,
          password: this.password,
        })
        .then((response) => {
          if (response.data !== "can not be connected to server") {
            this.warningmsgmysql = false;
            this.mysql_schemas = response.data;
            document.getElementById("mysqlloginuser").setAttribute("disabled",true)
            document.getElementById("mysqlloginpassword").setAttribute("disabled",true)
            this.isConnected = true
          } else {
            this.warningmsgmysql = true;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },


    getDisConnectToMySql() {
      this.mysql_schemas = [];
      this.mysql_tables = []
      document.getElementById("mysqlloginuser").removeAttribute("disabled")
      document.getElementById("mysqlloginpassword").removeAttribute("disabled")
      this.isConnected = false
          
    },

    /************************** TABLE LIST OF MYSQL SCHEMA **************************/

    getMySqlDBName(event) {
      this.schema = event.target.value;
      if (this.schema !== "") {
        const path = "http://127.0.0.1:5000/mysql_schema_tables";
        axios
          .post(path, {
            user: this.username,
            password: this.password,
            schema: this.schema,
          })
          .then((response) => {
            this.mysql_tables = response.data;
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        this.mysql_tables = [];
      }
    },

    /************************** TABLE LIST OF SQLITE FILE **************************/

    getSqliteDBName(event) {
      this.sqlite_filename = event.target.value;
      if (this.sqlite_filename !== "") {
        this.getSqliteTableList(this.sqlite_filename);
      } else {
        this.sqlite_table_list = [];
      }
    },

    async getSqliteTableList(file_name) {
      const json_data = await axios.get(
        "http://127.0.0.1:5000/sqlitetables/" +
          this.$route.params.username +
          "/" +
          file_name
      );
      this.sqlite_table_list = json_data.data;
    },

    /************************** GETTING DATA **************************/

    // from (.xlsx, .xls, .json, .csv) files
    async getData(file_name) {
      this.spinnerstatus = true
      this.items = [];
      this.fields = [];
      const json_data = await axios.get(
        "http://127.0.0.1:5000/data/" +
          this.$route.params.username +
          "/" +
          file_name
      );
      this.items = json_data.data;
      this.column_values = Object.keys(this.items[0]);
      this.column_values.forEach((head) => {
      this.fields.push({ key: head, sortable: true });
      
      });

      this.spinnerstatus = false
      var html_element = document.getElementById("accordion-four");
      if (
        this.items.length > 0 &&
        html_element.getAttribute("aria-expanded") === "false"
      ) {
        html_element.click();
      }
    },

// from the table in the (.sqlite, .sqlite3, .db)file
    async getDataFromSqlite(dbname, file_name) {
      this.spinnerstatus = true
      this.items = [];
      this.fields = [];
      const json_data = await axios.get(
        "http://127.0.0.1:5000/sqlite/" +
          this.$route.params.username +
          "/" +
          dbname +
          "/" +
          file_name
      );
      this.items = json_data.data;
      this.column_values = Object.keys(this.items[0]);
      this.column_values.forEach((head) => {
        this.fields.push({ key: head, sortable: true });
      });
      DataTable.data.totalRows = this.items.length  
      this.spinnerstatus = false
      var html_element = document.getElementById("accordion-four");
      if (
        this.items.length > 0 &&
        html_element.getAttribute("aria-expanded") === "false"
      ) {
        html_element.click();
      }
    },

// from the table in the mysql server
    async getDataFromMySql(schema_, table_name_) {
      this.spinnerstatus = true
      this.items = [];
      this.fields = [];
      const json_data = await axios.post("http://127.0.0.1:5000/mysql", {
        user: this.username,
        password: this.password,
        schema: schema_,
        tablename: table_name_,
      });
      this.items = json_data.data;
      this.column_values = Object.keys(this.items[0]);
      this.column_values.forEach((head) => {
        this.fields.push({ key: head, sortable: true });
      });
 
      this.spinnerstatus = false
      var html_element = document.getElementById("accordion-four");
      if (
        this.items.length > 0 &&
        html_element.getAttribute("aria-expanded") === "false"
      ) {
        html_element.click();
      }
    },

    /************************** DELETING FILE - DROPPING TABLE (IN SQLITE FILE) **************************/

    // delete (.xlsx, .xls, .json, .csv, .sqlite, .sqlite3, .db) files
    async deleteFile(filename) {
      if (
        confirm(
          "The file '" +
            filename +
            "' will be permanently deleted from the directory. Are you sure?"
        )
      ) {
        await axios.get(
          "http://127.0.0.1:5000/deleting/" +
            this.$route.params.username +
            "/" +
            filename
        );
        this.getFileList();
        if (this.sqlite_filename !== "") {
          this.getSqliteTableList(this.sqlite_filename);
        } else {
          this.sqlite_table_list = [];
        }
      } else {
        console.log("you cancelled");
      }
    },

    // drop the table in a (.sqlite, .sqlite3, .db) file
    async dropTable(sqlite_filename, tablename) {
      if (
        confirm(
          "The table '" +
            tablename +
            "' will be permanently deleted from the sqlite database file. Are you sure?"
        )
      ) {
        this.sqlite_table_list = [];
        const json_data = await axios.get(
          "http://127.0.0.1:5000/droptable/" +
            this.$route.params.username +
            "/" +
            sqlite_filename +
            "/" +
            tablename
        );
        this.sqlite_table_list = json_data.data;
      } else {
        console.log("you cancelled");
      }
    },

    // drop the schema in the mysql server
    deleteSchema(schema_name) {
      if (
        confirm(
          "The schema'" +
            schema_name +
            "' will be permanently deleted from the MySql server. Are you sure?"
        )
      ) {
        const path = "http://127.0.0.1:5000/deleteschema";
        axios
          .post(path, {
            user: this.username,
            password: this.password,
            schema: schema_name,
          })
          .then((response) => {
            this.mysql_schemas = response.data;
            this.mysql_tables = [];
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        console.log("you cancelled");
      }
    },

    // drop the table in a mysql server schema
    dropMySqlTable(table_name) {
      if (
        confirm(
          "The table '" +
            table_name +
            "' will be permanently deleted from the MySql schema. Are you sure?"
        )
      ) {
        const path = "http://127.0.0.1:5000/dropmysqltable";
        axios
          .post(path, {
            user: this.username,
            password: this.password,
            schema: this.schema,
            table: table_name,
          })
          .then((response) => {
            this.mysql_tables = response.data;
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        console.log("you cancelled");
      }
    },
  },

  computed: {
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter((f) => f.sortable)
        .map((f) => {
          return { text: f.key, value: f.key };
        });
    },
  },



  mounted() {
    this.getFileList();


  },
};
</script>

<!--################################### STYLE ###################################-->

<style lang="scss" scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

input.mysqlform {
  max-width: 150px;
  margin: 5px;
}

button.mysqlform {
  max-width: 100px;
  margin: 5px;
}

.menu {
  width: 25%;
  float: left;
  padding: 2px;
}

.main {
  width: 75%;
  float: left;
  padding: 5px;
}

.container {
  background: aqua;
  padding: 10px;
}

.one {
  width: 100%;
  background: white;
}

.two {
  width: 100%;
  background: grey;
}

div.accordion-body {
  padding: 10px;
  display: grid;
}

button.accordion-button {
  color: #0c63e4;
  background-color: #e7f1ff;
}

div.datafiles {
  background: linear-gradient(to bottom, #66ccff 0%, #ffccff 100%);
  margin-bottom: 2px;
  border-radius: 10px;
  padding-left: 7px;
  padding-right: 7px;
  text-align: left;
  float: left;
  width: 90%;
  margin-top: 2px;
  margin-bottom: 2px;
}

div.datafiles:hover {
  transform: scale(
    1.07
  ); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
  background: linear-gradient(to bottom, #fff899 0%, #99b1ff 100%);
}

div.trashicon {
  color: red;
  width: 5%;
  font-size: 18px;
  align-content: right;
  text-align: right;
  float: right;
}

div.trashicon:hover {
  color: red;
  transform: scale(1.5);
}

span.trashicon {
  color: red;
  width: 5%;
  font-size: 18px;
  align-content: center;
  text-align: center;
  float: right;
}

span.trashicon:hover {
  color: red;
  transform: scale(1.5);
}

input.mysqlform {
  margin-bottom: 2px;
  border-radius: 10px;
  padding-left: 7px;
  padding-right: 7px;
  size: 2px;
}

button.mysqlform {
  margin-bottom: 2px;
  border-radius: 10px;
  padding-left: 7px;
  padding-right: 7px;
}

.dropbtn {
  background-color: dodgerblue;
  color: orange;
  padding: 5px;
  font-size: 20px;
  border: none;
  font-weight: bold;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background: linear-gradient(to bottom, #66ccff 0%, #ffccff 100%);
  border-radius: 10px;
  z-index: 1;
}

button.dropbtn {
  background-color: #e7f1ff;
  border-radius: 10px;
  padding: 5px 10px;
  color: dodgerblue;
  font-size: 25px;
  font-weight: bold;
}

.dropdown-content div {
  background: linear-gradient(to bottom, #66ccff 0%, #ffccff 100%);
  border-radius: 10px;
  color: dodgerblue;
  font-size: 15px;
  font-weight: bold;
  padding: 10px 10px;
  text-align: center;
  text-decoration: none;
  align-items: right;
}

.dropdown-content div:hover {
  cursor: pointer;
}

.dropdown:hover .dropdown-content {
  display: block;
}

div.uploadbutton {
  background-color: #e7f1ff;
  border-radius: 10px;
  padding: 5px 10px;
  color: dodgerblue;
  font-weight: bold;
}

div.uploadbutton:hover {
  cursor: pointer;
}

div.uploadicon {
  color: dodgerblue;
  font-size: 25px;
  font-weight: bold;
}

div.uploadtext {
  color: dodgerblue;
  font-weight: bold;
}

span.warningmessagemysql {
  color: red;
  font-size: 15px;
  font-weight: bold;
}



// for loading spinner


// https://jsfiddle.net/mshaker88/u41rgq3e/


#overlay {
  background: #ffffff;
  color: #666666;
  position: fixed;
  height: 100%;
  width: 100%;
  z-index: 5000;
  top: 0;
  left: 0;
  float: left;
  text-align: center;
  padding-top: 25%;
  opacity: .80;
}

.spinner {
    margin: 0 auto;
    height: 64px;
    width: 64px;
    animation: rotate 0.8s infinite linear;
    border: 5px solid dodgerblue;
    border-right-color: transparent;
    border-radius: 50%;
}
@keyframes rotate {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}



.sr-only {
  display: none;
}

</style>
