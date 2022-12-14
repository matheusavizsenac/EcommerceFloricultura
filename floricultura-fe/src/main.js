import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';
import TabMenu from 'primevue/tabmenu';
import InputText from 'primevue/inputtext';
import Carousel from 'primevue/carousel';
import ImagePrime from 'primevue/image';
import Card from 'primevue/card';
import Button from 'primevue/button';
import axios from 'axios';


import 'primevue/resources/themes/lara-light-indigo/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';


axios.defaults.baseURL = 'http://127.0.0.1:8000'
createApp(App).use(router, axios).mount('#app')

const app = createApp(App);
app.use(router)
app.use(PrimeVue);

app.component('TabMenu', TabMenu);
app.component('InputText', InputText);
app.component('CarouselList', Carousel);
app.component('CardProduto', Card);
app.component('ButtonPrime', Button);
app.component('ImagePrime', ImagePrime);

app.mount('#app')