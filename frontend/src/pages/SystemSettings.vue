<template>
    <div class="searchPage">
        <Window class="searchWindow">
        </Window>
    </div>
</template>

<script setup>
import { reactive } from 'vue';
import Window from '@/components/Window.vue';
import { useRouter } from 'vue-router';
const router = useRouter()
const route = router.currentRoute

const inputInfo=reactive({
})

function back(){
    if(route.value.query.redirect){
        router.push(route.value.query.redirect)
    }else{
        router.back()
    }
}
</script>

<style scoped>
.searchPage{
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: aliceblue;
    height: 100%;
}
.searchWindow{
    position: relative;
    width: 500px;
    height: 600px;
    padding: 20px;
    display: flex;
    flex-direction: column;
}
.back{
    position: absolute;
    right: calc(100% + 40px);
    cursor: pointer;
    width: 40px;
    height: 40px;
    background-color: rgb(255, 119, 119);
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>