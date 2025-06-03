<template>
    <div class="loginPage">
        <Window class="loginWindow">
            <div class="header">
                <div @click="back(false)" class="back-button">← 返回</div>
                <h2>用户登录</h2>
            </div>
            <div class="form-group">
                <input type="text" v-model="phone" placeholder="手机号" class="input-field">
                <input type="password" v-model="password" placeholder="密码" class="input-field">
                <button @click="handleLogin" class="submit-button">登录</button>
            </div>
            <div class="footer">
                <RouterLink to="/register" class="link">还没有账号？立即注册</RouterLink>
            </div>
        </Window>
    </div>
</template>

<script setup>
import { ref,inject } from 'vue';
import { RouterLink,useRouter,useRoute } from 'vue-router';
import Window from '../components/Window.vue';

const phone = ref('');
const password = ref('');
const router=useRouter()
const route=useRoute()
const toast=inject('toast')


async function handleLogin(){
    try{
        let res=await fetch('http://localhost:8000/api/accounts/login/',{
            method:'POST',
            mode:'cors',
            credentials:'include',
            body:JSON.stringify({
                phone:phone.value,
                password:password.value
            })
        })
        let data=await res.json()
        if(res.status===200){
            localStorage.setItem('user',JSON.stringify({name:data.name}))
            toast.show('登录成功','success')
            back(true)
        }else{
            toast.show(data.error,'error')
        }
    }catch(error){
        toast.show(error.message,'error')
    }
};

function back(success=false) {
    if (success) {
        router.push(route.query.redirect || route.query.lastPage || '/');
    }
    else{
        router.push(route.query.lastPage || '/');
    }
}
</script>

<style scoped>
.loginPage {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: aliceblue;
    height: 100%;
}
.loginWindow {
    width: 400px;
    padding: 30px;
}
.header {
    text-align: center;
    margin-bottom: 30px;
    position: relative;
}
.back-button {
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    color: #666;
    font-size: 14px;
    cursor: pointer;
}
.back-button:hover {
    color: #1e88e5;
}
h2 {
    color: #1e88e5;
    margin: 0;
}
.form-group {
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.input-field {
    padding: 12px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 16px;
}
.input-field:focus {
    outline: none;
    border-color: #1e88e5;
}
.submit-button {
    padding: 12px;
    background-color: #1e88e5;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s;
}
.submit-button:hover {
    background-color: #1565c0;
}
.footer {
    margin-top: 20px;
    text-align: center;
}
.link {
    color: #1e88e5;
    text-decoration: none;
    font-size: 14px;
}
.link:hover {
    text-decoration: underline;
}
</style>