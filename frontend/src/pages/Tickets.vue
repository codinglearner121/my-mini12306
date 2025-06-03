<template>
    <div class="ticketsPage">
        <Window class="ticketsWindow">
            <div class="header">
                <div @click="back" class="back-button">← 返回</div>
                <h2>模拟购票</h2>
            </div>
            <div v-if="loading">
                <div class="loading-container">
                    <div class="loading-spinner"></div>
                    <div class="loading-text">加载中...</div>
                </div>
            </div>
            <div v-else>
                <div class="ticket-count">共有{{ tickets.length }}张车票可购</div>
                <div class="ticket-header">
                    <div class="ticket-id">车票ID</div>
                    <div class="ticket-trainId">车次</div>
                    <div class="ticket-date">出发时间</div>
                    <div class="ticket-startStation">出发站</div>
                    <div class="ticket-endStation">到达站</div>
                    <div class="ticket-price">票价（元）</div>
                    <div class="ticket-available_seats">余票</div>
                    <div class="ticket-purchase">购票</div>
                </div>
                <div class="ticket-item" v-for="ticket in tickets" :key="ticket.id">
                    <div class="ticket-id">{{ ticket.id }}</div>
                    <div class="ticket-trainId">{{ ticket.train_number }}</div>
                    <div class="ticket-date">{{ ticket.departure_time }}</div>
                    <div class="ticket-startStation">{{ ticket.departure }}</div>
                    <div class="ticket-endStation">{{ ticket.destination }}</div>
                    <div class="ticket-price">{{ ticket.price }}</div>
                    <div class="ticket-available_seats">{{ ticket.available_seats }}</div>
                    <button class="ticket-purchase" @click="toPurchase(ticket.id)">购票</button>
                </div>
            </div>

        </Window>
    </div>
</template>

<script setup>
import { ref, reactive,inject } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import Window from '../components/Window.vue';

const toast=inject('toast')
const user=JSON.parse(localStorage.getItem('user'))
const router = useRouter();
const route = useRoute();
const loading = ref(true);
const tickets=ref([]);


async function loadTickets(){
    loading.value=true
    try{
        let res=await fetch('http://localhost:8000/api/tickets/tickets/',{
            method:'GET',
        })
        let data=await res.json()
        if(res.status===200){
            tickets.value=data.filter(item=>item.available_seats>0)
        }else{
            toast.show(data.error,'error')
        }
    }catch(error){
        console.log(error)
        toast.show("车票加载失败，请稍后刷新重试","error")
    }finally{
        loading.value=false
    }
}
loadTickets()

async function toPurchase(id){
    router.push(`/ticket-purchase/${id}`)
}

function back() {
    if (route.query.redirect) {
        router.push(route.query.redirect);
    } else {
        router.back();
    }
}

</script>

<style scoped>
.ticketsPage {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: aliceblue;
    height: 100%;
}
.ticketsWindow {
    width: 800px;
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
.loading-container {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
}
.loading-spinner {
    border: 4px solid rgba(0, 0, 0, 0.1);
    border-left-color: #1e88e5;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    animation: spin 1s linear infinite;
}
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
.loading-text {
    margin-left: 10px;
    font-size: 14px;
    color: #666;
}
.ticket-count{
    text-align: center;
    margin-bottom: 30px;
}
.ticket-header{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    background-color: #1e88e5;
    color: #fff;
    border-radius: 5px 5px 0 0;
    margin-bottom: 5px;
    padding: 5px;
}
.ticket-item{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    padding: 5px;
}
.ticket-id{
    width: 150px;
}
.ticket-trainId{
    width: 120px;
}
.ticket-date{
    width: 300px;
}
.ticket-startStation{
    width: 150px;
}
.ticket-endStation{
    width: 150px;
}
.ticket-price{
    width: 150px;
}
.ticket-available_seats{
    width: 100px;
}
.ticket-purchase{
    width: 100px;
}
.ticket-item .ticket-purchase{
    background-color: #1e88e5;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    padding: 5px;
}
.ticket-item .ticket-purchase:hover{
    background-color: #1565c0;
}




</style>