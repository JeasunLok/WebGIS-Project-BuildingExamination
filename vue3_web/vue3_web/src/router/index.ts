import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import HomeView from '../views/HomeView.vue'


const routes: Array<RouteRecordRaw> = [
  
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/homeview',
    name: 'homeview',
    component: () => import( '../views/HomeView.vue'),
    children:[
      {  
        // 子路由中默认显示的页面
        path: '',
        name: 'Monitor',
        component:() => import( '../components/Monitor.vue')
      },
      {
        path: 'nav',
        name: 'navigation',
        component:() => import( '../components/Navigation.vue')
      },
      {
        path: 'dataview',
        name: 'data',
        component:() => import( '../components/Dataview.vue')
      }
    ]
  },
  // {
  //   path: '/set',
  //   name: 'set',
  //   component: () => import( '../views/SetParameter.vue')
  // },
  {
    path: '/user',
    name: 'register',
    component: () => import( '../views/Register.vue')
  },

 /*
  {
    path: '/',
    name: 'header',
    component: Header
  },
  */

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

