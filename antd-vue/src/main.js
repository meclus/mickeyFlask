import Vue from "vue";
import Button from "ant-design-vue/lib/button";
import "ant-design-vue/dist/antd.css";
// import { Button } from 'ant-design-vue';
import App from "./App";

Vue.component(Button.name, Button);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App)
}).$mount("#app");