<template>
    <div class="searchPage">
        <Window class="searchWindow">
            <div class="header">
                <RouterLink to="/" class="back-button">← 返回</RouterLink>
                <h2>车次查询</h2>
            </div>
            
            <div class="search-tabs">
                <div 
                    :class="['tab', { active: activeTab === 'route' }]" 
                    @click="activeTab = 'route'"
                >路线查询</div>
                <div 
                    :class="['tab', { active: activeTab === 'id' }]" 
                    @click="activeTab = 'id'"
                >车次/车票查询</div>
            </div>

            <!-- 路线查询表单 -->
            <div v-if="activeTab === 'route'" class="form-group">
                <div class="date-input">
                    <input type="date" v-model="routeInfo.date" class="input-field">
                </div>
                <div class="station-inputs">
                    <input type="text" v-model="routeInfo.startStation" placeholder="出发站" class="input-field">
                    <div class="station-arrow">→</div>
                    <input type="text" v-model="routeInfo.endStation" placeholder="到达站" class="input-field">
                </div>
                <button @click="handleRouteSearch" class="submit-button">查询车次</button>
            </div>

            <!-- 车次/车票ID查询表单 -->
            <div v-if="activeTab === 'id'" class="form-group">
                <div class="id-inputs">
                    <input type="text" v-model="idInfo.trainId" placeholder="车次号" class="input-field">
                    <div class="or-divider">或</div>
                    <input type="text" v-model="idInfo.ticketId" placeholder="车票ID" class="input-field">
                </div>
                <button @click="handleIdSearch" class="submit-button">查询</button>
            </div>
        </Window>
    </div>
</template>

<script setup>
import { ref, reactive,inject } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import Window from '../components/Window.vue';

const toast=inject('toast')
// TODO
toast.show("本功能未实现，车次查询仅作示范","info")

const activeTab = ref('route');

const routeInfo = reactive({
    date: '',
    startStation: '',
    endStation: ''
});

const idInfo = reactive({
    trainId: '',
    ticketId: ''
});

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
.searchPage {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: aliceblue;
    height: 100%;
}
.searchWindow {
    width: 500px;
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
    text-decoration: none;
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
.search-tabs {
    display: flex;
    margin-bottom: 20px;
    border-bottom: 2px solid #eee;
}
.tab {
    flex: 1;
    text-align: center;
    padding: 10px;
    cursor: pointer;
    color: #666;
    transition: all 0.3s;
}
.tab.active {
    color: #1e88e5;
    border-bottom: 2px solid #1e88e5;
    margin-bottom: -2px;
}
.form-group {
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.date-input {
    width: 100%;
}
.station-inputs {
    display: flex;
    align-items: center;
    gap: 10px;
}
.station-arrow {
    color: #666;
    font-size: 20px;
}
.id-inputs {
    display: flex;
    flex-direction: column;
    gap: 15px;
}
.or-divider {
    text-align: center;
    color: #666;
    margin: 5px 0;
}
.input-field {
    padding: 12px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 16px;
    width: 100%;
    box-sizing: border-box;
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
</style>