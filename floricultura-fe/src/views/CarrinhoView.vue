<template>
  <div>
    <CardProduto class="produto" v-for="(carrinho) in listaCarrinho" :key="carrinho.id">
        <template #header>
          <ButtonPrime id="buttonDeletar" icon="pi pi-trash" @click="DeleteItemCarrinho(carrinho.id)" />
        </template>
        <template #title>
          {{carrinho.idProduto.nome}}
        </template>
        <template #content>
          <p>Quantidade {{carrinho.quantidade}}</p>
          <br/> 
          Preço R$ {{carrinho.idProduto.preco * carrinho.quantidade}}
        </template>
    </CardProduto>
  </div>
  <CardProduto class="produto">
        <template #title>
          Total:   {{valorTotal}}
        </template>
        <template #content>
          <p>valor final</p>
          <router-link :to="{ name: 'FinalizarCompraView'}">
               <ButtonPrime id="buttonFinalizarCompra" label="Finalizar compra" icon="pi pi-check" iconPos="right" />
          </router-link>
        </template>
    </CardProduto>
  </template>
  
<script>
import axios from 'axios'
  export default {
    data() {
      return {
        value: '',
        listaCarrinho: []
      }
    },
    components: {},
      mounted() {
      this.getCarrinho()
      },
    methods: {
      getCarrinho(){
        axios.get('floriculturaapp/carrinho').then(response => {
          this.listaCarrinho = response.data
        })
    },
      DeleteItemCarrinho(id){
          axios.delete('floriculturaapp/carrinho/'+ id).then(() => {
            this.getCarrinho();
          })
      }
  },
  computed: {
    valorTotal() {
      var valorFinal = 0;
      for (let i = 0; i < this.listaCarrinho.length; i++) {
        if (this.listaCarrinho[i].idUsuario.id == 1) {
          valorFinal = valorFinal + (this.listaCarrinho[i].idProduto.preco * this.listaCarrinho[i].quantidade);
        }
      }
      return valorFinal
    }
  }
}
</script>

<style scoped>
 #buttonDeletar {
  float: right;
}
#divSeuCep{
  margin-top: 15px;
}
#buttonFinalizarCompra{
  margin-top: 15px;
}
 </style>