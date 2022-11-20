import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProdutosView from '../views/ProdutosView.vue'
import CarrinhoView from '../views/CarrinhoView.vue'
import UsuarioView from '../views/UsuarioView.vue'
import NovoUsuarioView from '../views/NovoUsuarioView.vue'
import LoginUsuarioView from '../views/LoginUsuarioView.vue'



const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/produtos',
    name: 'produtos',
    component: ProdutosView
  },
  {
    path: '/carrinho',
    name: 'carrinho',
    component: CarrinhoView
  },
  {
    path: '/usuario',
    name: 'usuario',
    component: UsuarioView
  },
  {
    path: '/novousuario',
    name: 'novoUsuario',
    component: NovoUsuarioView
  },
  {
    path: '/loginusuario',
    name: 'loginUsuario',
    component: LoginUsuarioView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
