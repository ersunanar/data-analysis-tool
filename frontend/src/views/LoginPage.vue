<template>
<div>
    <div class="auto-wrapper">
    <br>
    <br>
    <br>
        <div class="auth-inner" >
            <form @submit.prevent="login()">
                <h3>Login</h3>
                <div class="form-group">
                    <label for="user_name">User Name</label>
                    <input type="text" name="user_name" v-model="username"  class="form-control" placeholder="username">
                </div>
                <div class="form-group">
                    <label for="pass">Password</label>
                    <input type="password" name="pass" v-model="password" class="form-control" placeholder="password">
                </div>
                <br>
                <button class="btn btn-primary btn-block">Login</button>
            </form>
        </div>
    </div>
    <br>
    <br>
    <div v-if="warningmsg">
        <h1  class="warningmessage" style="color: red font-size: 20px">your credentials are wrong. please check your username and password</h1>
    </div>
</div>
</template>

<script>

import axios from 'axios'

export default {
name: 'LoginPage',
data() {
return {
username: '',
password: '',
warningmsg : false
}
},

methods: {
login() {
const path = 'http://127.0.0.1:5000/user'
axios.post(path, {
user:this.username.toUpperCase(),
password:this.password,
}
).then(response => {
if (response.data !== 'wrong credentials') {
this.warningmsg = false
this.$store.commit("setAuthentication",true);
this.$router.push({ name: 'user', params: { username: response.data.username, name: response.data.name, surname: response.data.surname, email: response.data.email} })
}
else {
this.warningmsg = true
}
})
.catch(err =>{
console.log(err);
}); 
},
}
}
</script>

<style scoped>

div.auth-wrapper {
    display: flex;
    justify-content: center;
    flex-direction: column;
    text-align: left;
}

div.auth-inner {
    width: 450px;
    margin: auto;
    background-color: #ffffff;
    box-shadow: 0px, 14px, 80px, rgba(34,35,58,0.2);
    padding: 40px, 55px, 45px, 55px;
}

h1.warningmessage {
    color: red;
    font-size: 20px;
    font-weight: bold;
}

</style>