import Vue from 'vue'
import App from './App.vue'
import router from './router'
// import VueRouter from 'vue-router';
// import ourRoutes from './router'
Vue.config.productionTip = false

// const router = new VueRouter({
//   routes: ourRoutes
// });

// // The usual app stuff goes here.
// new Vue({
//   //
//   router,
//   render: h => h(App)
// }).$mount('#app');


new Vue({
  router,               // Add this line
  render: h => h(App)
}).$mount('#app')