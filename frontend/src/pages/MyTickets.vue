<template>
    <div class="myTicketsPage">
        <Window class="myTicketsWindow">
            <div class="header">
                <div @click="back" class="back-button">← 返回</div>
                <h2>我的车票</h2>
            </div>
            <div v-if="loading">
                <div class="loading-container">
                    <div class="loading-spinner"></div>
                    <div class="loading-text">加载中...</div>
                </div>
            </div>
            <div v-else>
                <div class="ticket-count">共有{{ tickets.length }}张车票</div>
                <div class="ticket-header">
                    <div class="ticket-id">车票ID</div>
                    <div class="ticket-trainId">车次</div>
                    <div class="ticket-date">出发时间</div>
                    <div class="ticket-startStation">出发站</div>
                    <div class="ticket-endStation">到达站</div>
                    <div class="ticket-price">票价</div>
                </div>
                <div class="ticket-item" v-for="ticket in tickets" :key="ticket.id">
                    <div class="ticket-id">{{ ticket.id }}</div>
                    <div class="ticket-trainId">{{ ticket.train_number }}</div>
                    <div class="ticket-date">{{ ticket.departure_time }}</div>
                    <div class="ticket-startStation">{{ ticket.departure }}</div>
                    <div class="ticket-endStation">{{ ticket.destination }}</div>
                    <div class="ticket-price">{{ ticket.price }}</div>
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

(async()=>{
    try{
        // let res=await fetch('http://localhost:3000/myTickets',{
        //     method:'POST',
        //     body:JSON.stringify({
        //         name:user.name
        //     })
        // })
        // if(res.status===200){
        //     res=await res.json()
        //     tickets.value=res.data
        //     loading.value=false
        // }else{
        //     toast.show(res.message,'error')
        // }
        toast.show("本功能未实现，车票信息仅作示范","info")
        tickets.value=[
            {
                "id": 1,
                "train_number": "G120",
                "departure": "北京",
                "destination": "上海",
                "departure_time": "2025-05-26 08:00",
                "seat_type": "二等座",
                "price": "550.00",
                "available_seats": 100
            },
            {
                "id": 2,
                "train_number": "G121",
                "departure": "北京",
                "destination": "上海",
                "departure_time": "2025-05-26 08:00",
                "seat_type": "二等座",
                "price": "560.00",
                "available_seats": 100
            },
            {
                "id": 3,
                "train_number": "G122",
                "departure": "北京",
                "destination": "上海",
                "departure_time": "2025-05-27 08:00",
                "seat_type": "二等座",
                "price": "570.00",
                "available_seats": 100
            },
            {
                "id": 4,
                "train_number": "G123",
                "departure": "北京",
                "destination": "上海",
                "departure_time": "2025-05-27 08:00",
                "seat_type": "二等座",
                "price": "580.00",
                "available_seats": 100
            },
            {
                "id": 5,
                "train_number": "G124",
                "departure": "北京",
                "destination": "上海",
                "departure_time": "2025-05-28 08:00",
                "seat_type": "二等座",
                "price": "590.00",
                "available_seats": 100
            }
        ]
        loading.value=false
    }catch(error){
        console.log(error)
        toast.show("车票加载失败，请稍后刷新重试","error")
    }
})()

const routeInfo = reactive({
    date: '',
    startStation: '',
    endStation: ''
});

const idInfo = reactive({
    trainId: '',
    ticketId: ''
});

function back() {
    if (route.query.redirect) {
        router.push(route.query.redirect);
    } else {
        router.back();
    }
}

async function handleRouteSearch() {
    // TODO: 实现路线查询逻辑
    console.log('路线查询:', routeInfo);
}

async function handleIdSearch() {
    // TODO: 实现车次/车票ID查询逻辑
    console.log('ID查询:', idInfo);
}
</script>

<style scoped>
.myTicketsPage {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: aliceblue;
    height: 100%;
}
.myTicketsWindow {
    width: 700px;
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
    width: 120px;
}





</style>