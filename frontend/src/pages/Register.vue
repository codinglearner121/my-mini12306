<template>
    <div class="registerPage">
        <Window class="registerWindow">
            <div class="header">
                <div @click="back(false)" class="back-button">← 返回</div>
                <h2>用户注册</h2>
            </div>
            <div class="form-group">
                <input type="text" v-model="name" placeholder="姓名" class="input-field">
                <input type="password" v-model="password" placeholder="密码" class="input-field">
                <input type="password" v-model="confirmPassword" placeholder="确认密码" class="input-field">
                <input type="text" v-model="id_card" placeholder="身份证号" class="input-field">
                <input type="text" v-model="phone" placeholder="手机号" class="input-field">
                <input type="text" v-model="bank_card" placeholder="银行卡号" class="input-field">
                <button @click="handleRegister" class="submit-button">注册</button>
            </div>
            <div class="footer">
                <RouterLink to="/login" class="link">已有账号？立即登录</RouterLink>
            </div>
        </Window>
    </div>
</template>

<script setup>
import { ref,inject } from 'vue';
import { RouterLink,useRouter,useRoute } from 'vue-router';
import Window from '../components/Window.vue';

const name = ref('');
const password = ref('');
const confirmPassword = ref('');
const id_card = ref('');
const phone = ref('');
const bank_card = ref('');
const router=useRouter()
const route=useRoute()
const toast=inject('toast')

async function handleRegister(){
    if(password.value!==confirmPassword.value){
        toast.show('密码不一致','error')
        return
    }
    try{
        const info={
            name:name.value,
            password:password.value,
            id_card:id_card.value,
            phone:phone.value,
            bank_card:bank_card.value
        }
        const res=await fetch('http://localhost:8000/api/accounts/register/',{
            method:'POST',
            body:JSON.stringify(info)
        })
        let data=await res.json()
        if(res.status===200){
            toast.show('注册成功','success')
            router.push({path:'/login',query:route.query})
        }else{
            toast.show(data.error,'error')
        }
    }catch(error){
        toast.show(error.message,'error')
    }
}
function back(success=false) {
    if (success) {
        router.push(route.query.redirect || route.query.lastPath || '/');
    }
    else{
        router.push(route.query.lastPath || '/');
    }
}
</script>

<style scoped>
.registerPage {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: aliceblue;
    height: 100%;
}
.registerWindow {
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
    gap: 15px;
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
    margin-top: 10px;
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