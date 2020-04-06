import Vue from 'vue'
import VueRouter from 'vue-router'
import Todo from "../components/Todo";
import Menu from "../components/Menu";

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'menu',
    component: Menu
  },
  {
    path: '/todo',
    name: 'todo',
    component: Todo
  }
];

const router = new VueRouter({
  routes,
  mode: "history",
});

export default router
