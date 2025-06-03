<template>
    <div class="ticketPurchasePage">
        <Window class="ticketPurchaseWindow">
            <div class="header">
                <div @click="back" class="back-button">← 返回</div>
                <h2>车票信息</h2>
            </div>
            <div v-if="loading">
                <div class="loading-container">
                    <div class="loading-spinner"></div>
                    <div class="loading-text">加载中...</div>
                </div>
            </div>
            <div v-else>
                <div class="ticket-info">
                    <div class="ticket-id">车票ID:{{ ticket.id }}</div>
                    <div class="ticket-trainId">车次:{{ ticket.train_number }}</div>
                    <div class="ticket-date">出发时间:{{ ticket.departure_time }}</div>
                    <div class="ticket-startStation">出发站:{{ ticket.departure }}</div>
                    <div class="ticket-endStation">到达站:{{ ticket.destination }}</div>
                    <div class="ticket-price">票价:{{ ticket.price }}元</div>
                    <div class="ticket-available_seats">余票:{{ ticket.available_seats }}</div>
                </div>
                <div class="ticket-purchase">
                    <button @click="purchase(ticket.id)">购票</button>
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
const ticket=ref({});


async function loadTicket(){
    loading.value=true
    try{
        // TODO: 改成具体id车票接口
        let res=await fetch('http://localhost:8000/api/tickets/tickets/',{
            method:'GET',
        })
        let data=await res.json()
        if(res.status===200){
            let _ticket=data.filter(item=>item.id==route.params.id)
            if(_ticket.length>0){
                ticket.value=_ticket[0]
            }else{
                toast.show("车票不存在","error")
                setTimeout(()=>{
                    back()
                },2000)
            }
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
loadTicket()

async function purchase(id){
    try{
        let res=await fetch('http://localhost:8000/api/tickets/book/',{
            method:'POST',
            credentials:'include',
            body:JSON.stringify({
                ticket_id:id,
            })
        })
        if(res.status===200){
            toast.show("购票成功","success")
            setTimeout(()=>{
                back()
            },2000)
        }else{
            res=await res.json()
            toast.show("购票失败: "+res.error,'error')
            console.log(res)
        }
    }catch(error){
        toast.show("购票失败，请稍后刷新重试","error")
        console.log(error)
    }
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
.ticketPurchasePage {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: aliceblue;
    height: 100%;
}
.ticketPurchaseWindow {
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
.ticket-info{
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.ticket-id{
    height: 50px;
}
.ticket-trainId{
    height: 50px;
}
.ticket-date{
    height: 50px;
}
.ticket-startStation{
    height: 50px;
}
.ticket-endStation{
    height: 50px;
}
.ticket-price{
    height: 50px;
}
.ticket-available_seats{
    height: 50px;
}
.ticket-purchase{
    height: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.ticket-purchase button{
    background-color: #1e88e5;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    padding: 5px;
    width: 100%;
    font-size: 16px;
}
.ticket-purchase button:hover{
    background-color: #1565c0;
}




</style>