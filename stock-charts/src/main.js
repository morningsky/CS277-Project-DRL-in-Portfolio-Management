import Vue from 'vue';
import { Button, Slider } from 'view-design';
import 'view-design/dist/styles/iview.css';
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;
Vue.component('Button', Button);
Vue.component('Slider', Slider);
new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
