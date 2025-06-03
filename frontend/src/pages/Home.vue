<template>
    <div class="homePage">
        <div class="content">
            <Window class="mainWindow">
                <div class="welcome-text">欢迎使用迷你12306</div>
                <div class="button-group">
                    <RouterLink to="/train-search" class="action-button">
                        查询车票
                    </RouterLink>
                    <RouterLink v-if="!isLogin" to="/login" class="action-button">
                        用户登录
                    </RouterLink>
                    <RouterLink v-if="!isLogin" to="/register" class="action-button">
                        用户注册
                    </RouterLink>
                    <RouterLink v-if="isLogin" to="/tickets" class="action-button">
                        模拟购票
                    </RouterLink>
                    <RouterLink v-if="isLogin" to="/my-tickets" class="action-button">
                        我的车票
                    </RouterLink>
                    <div v-if="isLogin" @click="logout" class="action-button">
                        退出登录
                    </div>
                </div>
            </Window>
        </div>
    </div>
</template>

<script setup>
import { inject } from 'vue';
import { RouterLink,useRouter } from 'vue-router';
const router=useRouter()
const user=JSON.parse(localStorage.getItem('user'))
const isLogin=user?true:false
const toast=inject('toast')
function logout(){
    localStorage.removeItem('user')
    document.cookie = 'sessionid= ; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;'
    toast.show('退出登录成功','success')
    setTimeout(()=>{
        router.go(0)
    },1000)
}
</script>

<style scoped>
.homePage{
    height: 100%;
    display: flex;
    flex-direction: column;
    background-color: aliceblue;
}
.content{
    flex: 1;
    height: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
}
.mainWindow {
    width: 600px;
    padding: 30px;
    text-align: center;
}
.welcome-text {
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 40px;
    color: #1e88e5;
}
.button-group {
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.action-button {
    padding: 15px 30px;
    background-color: #1e88e5;
    color: white;
    text-decoration: none;
    border-radius: 5px;
    font-size: 18px;
    transition: background-color 0.3s;
    cursor: pointer;
}
.action-button:hover {
    background-color: #1565c0;
}
</style>