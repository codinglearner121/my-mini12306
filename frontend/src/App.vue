<script setup>
import { RouterView,useRoute } from 'vue-router'
import { ref, provide } from 'vue'
import Toast from './components/Toast.vue'

const toastRef = ref(null)
const route=useRoute()
let user=JSON.parse(localStorage.getItem('user'))
const isLogin=ref(user?true:false)

setInterval(()=>{
    user=JSON.parse(localStorage.getItem('user'))
    isLogin.value=user?true:false
},1000)
// 提供全局toast方法
provide('toast', {
    show: (message, type = 'info') => {
        toastRef.value?.show(message, type)
    }
})
</script>

<template>
    <div class="app">
        <div class="header">
            <RouterLink to="/" style="font-size: 24px; font-weight: bold; text-decoration: none; color: #fff;">迷你12306</RouterLink>
            <div style="flex: 1;"></div>
            <RouterLink v-if="!isLogin" :to="'/login?redirect='+route.path" class="nav-link">登录</RouterLink>
            <div v-if="!isLogin" style="margin: 0 3px;">/</div>
            <RouterLink v-if="!isLogin" :to="'/register?redirect='+route.path" class="nav-link">注册</RouterLink>
            <div v-if="isLogin">欢迎 {{ user.name }}</div>
        </div>
        <RouterView />
        <Toast ref="toastRef" />
    </div>
</template>

<style scoped>
.app{
    height: 100%;
    display: flex;
    flex-direction: column;
}
.header{
    height: 60px;
    background-color: #1e88e5;
    color: #fff;
    display: flex;
    align-items: center;
    padding: 0 20px;
}
.nav-link {
    color: white;
    text-decoration: none;
    margin: 0 10px;
}
.nav-link:hover {
    text-decoration: underline;
}
</style>
