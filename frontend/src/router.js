import { createRouter,createWebHashHistory } from 'vue-router'
import Home from './pages/Home.vue'
import Login from './pages/Login.vue'
import Register from './pages/Register.vue'
import TrainSearch from './pages/TrainSearch.vue'
import Tickets from './pages/Tickets.vue'
import MyTickets from './pages/MyTickets.vue'
import TicketPurchase from './pages/TicketPurchase.vue'
import SystemSettings from './pages/SystemSettings.vue'

let router=createRouter({
    history:createWebHashHistory(),
    routes:[
        {
            path:'/',
            component:Home,
            meta:{title: "迷你12306 - 网站"}
        },
        {
            path:'/login',
            component:Login,
            meta:{title: "用户登录"}
        },
        {
            path:'/register',
            component:Register,
            meta:{title: "用户注册"}
        },
        {
            path:'/train-search',
            component:TrainSearch,
            meta:{
                title: "车次查询"
            }
        },
        {
            path:'/tickets',
            component:Tickets,
            meta:{
                title: "购票",
                requiresAuth: true
            }
        },
        {
            path:'/ticket-purchase/:id',
            component:TicketPurchase,
            meta:{
                title: "购票",
                requiresAuth: true
            }
        },
        {
            path:'/my-tickets',
            component:MyTickets,
            meta:{
                title: "我的车票",
                requiresAuth: true
            }
        },
        {
            path:'/system-settings',
            component:SystemSettings,
            meta:{
                title: "系统设置",
                requiresAuth: true,
                requiresAdmin: true
            }
        }
    ]
})

router.beforeEach((to, from, next)=>{
    // 设置页面标题
    if (to.meta && to.meta.title) {
        document.title = to.meta.title;
    }

    // 处理登录和注册页面
    if(to.path === '/login' || to.path === '/register'){
        if(to.redirectedFrom){
            next()
            return
        }
        // 如果已经登录，直接跳转到首页
        const isLoggedIn = localStorage.getItem('user');
        if (isLoggedIn) {
            next('/');
            return;
        }
        // 未登录时，添加redirect参数
        next({
            path: to.path,
            query: {
                lastPage: from.path === '/login' || from.path === '/register' ? '/' : from.fullPath
            }
        });
        return;
    }

    // 处理需要登录权限的页面
    if (to.meta.requiresAuth) {
        const isLoggedIn = localStorage.getItem('user');
        if (!isLoggedIn) {
            next({
                path: '/login',
                query: {
                    redirect: to.fullPath,
                    lastPage: from.fullPath
                }
            });
            return;
        }

        // 检查管理员权限
        if (to.meta.requiresAdmin) {
            const user = JSON.parse(localStorage.getItem('user'));
            if (!user.isAdmin) {
                next('/');
                return;
            }
        }
    }

    // 其他情况正常访问
    next();
})

export default router