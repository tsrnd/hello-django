import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import Contact from '@/components/Contact'

Vue.use(Router)

export default new Router({
  routes: [ // bao gồm danh sách route
    {
      path: '/', ///path của route
      name: 'hello', // tên route
      component: Hello // component route sử dụng
    },
    {
      path: '/about',
      name: 'contact',
      component: Contact
    }
  ]
})