import './assets/main.css'

import { createApp } from 'vue'
import router from './router'
import App from './App.vue'

import Window from './components/Window.vue'

let app=createApp(App)
app.use(router)

app.component('Window', Window)



app.mount('#app')
