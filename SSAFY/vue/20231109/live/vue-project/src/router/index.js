import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '../views/Userview.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path:'/user/:id',
      name:'user',
      component: UserView,
      beforeEnter: (to, from) => {
        console.log(to)
        console.log(from)
      }
    },
    {
      path:'/login',
      name:'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        const isAuthenticated = true
        if (isAuthenticated) {
          console.log('이미 로그인한 상태입니다.')
          return {name:'home'}
        }
      }
    }
  ]
  
})
// router.beforeEach((to, from) => {
//   const isAuthenticated = false
//   if (!isAuthenticated && to.name!=='login') {
//     console.log('로그인이 필요합니다.')
//     return {name:'login'}
//   }
  
// })
export default router
