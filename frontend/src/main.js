import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import { TablePlugin } from 'bootstrap-vue'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueResource from "vue-resource"
import AsyncComputed from 'vue-async-computed'
import { Bar, Line, Pie } from 'vue-chartjs'
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import VuePivottable from 'vue-pivottable'
import 'vue-pivottable/dist/vue-pivottable.css'
import "vue-easytable/libs/theme-default/index.css";
import VueEasytable from "vue-easytable";
import HomePage from './views/HomePage.vue'
import UserPage from './views/UserPage.vue';
import LoginPage from './views/LoginPage.vue';

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VueResource);
Vue.use(AsyncComputed);
Vue.use(Bar);
Vue.use(Line);
Vue.use(Pie);
Vue.use(VuePivottable);
Vue.use(VueEasytable);
Vue.use(Vuex);
Vue.use(VueRouter);
Vue.use(TablePlugin);

Vue.config.productionTip = false

const router = new VueRouter({
  mode : 'history',
  routes : [
    {
      path: '/',
      name: 'home',
      component: HomePage,
      redirect : {
        name: 'login'
      }
    },
  
    {
      path: '/user/:username',
      name: 'user',
      component: UserPage,
      beforeEnter: (to, from, next) => {
        if (store.state.authenticated == false) {
          next('/login')
        }
        else {
          next()
        }
  
      }
    },
  
    {
      path: '/login',
      name: 'login',
      component: LoginPage
    },  
  ]
})


const store = new Vuex.Store(
  {
    state : {
      authenticated : false
    },
    mutations: {
      setAuthentication(state,status) {
        state.authenticated = status;
      }
    }
  }
)

new Vue({
  router: router,
  render: h => h(App),
  store: store
}).$mount('#app')

