<template>
    <Transition name="toast">
        <div v-if="visible" class="toast" :class="type">
            {{ message }}
        </div>
    </Transition>
</template>

<script setup>
import { ref, watch } from 'vue';

const visible = ref(false);
const message = ref('');
const type = ref('info');
let timer = null;

// 显示消息
const show = (msg, msgType = 'info') => {
    message.value = msg;
    type.value = msgType;
    visible.value = true;
    
    // 清除之前的定时器
    if (timer) {
        clearTimeout(timer);
    }
    
    // 3秒后隐藏
    timer = setTimeout(() => {
        visible.value = false;
    }, 3000);
};

// 暴露方法给父组件
defineExpose({
    show
});
</script>

<style scoped>
.toast {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    padding: 12px 24px;
    border-radius: 4px;
    color: white;
    font-size: 14px;
    z-index: 9999;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.toast.info {
    background-color: #1e88e5;
}

.toast.success {
    background-color: #4caf50;
}

.toast.warning {
    background-color: #ff9800;
}

.toast.error {
    background-color: #f44336;
}

/* 动画效果 */
.toast-enter-active {
    transition: all 0.3s ease-out;
}

.toast-leave-active {
    transition: all 0.3s ease-in;
}

.toast-enter-from {
    transform: translate(-50%, -100%);
    opacity: 0;
}

.toast-leave-to {
    transform: translate(-50%, -100%);
    opacity: 0;
}
</style>
