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
          <div class="col-12 md:col-4">
              <div class="p-inputgroup">
                  <ButtonPrime icon="pi pi-minus" @click="updateQuantidade(carrinho, carrinho.quantidade - 1)" />
                  <InputText readonly v-model="carrinho.quantidade" placeholder="Quantidade"/>
                  <ButtonPrime icon="pi pi-plus" @click="updateQuantidade(carrinho, carrinho.quantidade + 1)" />
              </div>
          </div>

          <br/> 
          Preço R$ {{carrinho.idProduto.preco}}
        </template>
    </CardProduto>
  </div>
  <CardProduto class="produto" v-if="listaCarrinho.length > 0">
        <template #title>
          Total: R$  {{valorTotal}}
        </template>
        <template #content>
          <router-link :to="{ name: 'FinalizarCompraView'}">
               <ButtonPrime id="buttonFinalizarCompra" label="Finalizar compra" icon="pi pi-check" iconPos="right"/>
          </router-link>
        </template>
  </CardProduto>
  <div class="CarrinhoVazio" v-if="listaCarrinho.length == 0">
    <CardProduto>
        <template #title>
          Adicione itens ao seu carrinho
        </template>
        <template #content>
          <router-link :to="{ name: 'produtos'}">
               <ButtonPrime id="buttonVisualizarProdutos" label="Continuar Comprando" icon="pi-shopping-bag" iconPos="right" />
          </router-link>
        </template>
  </CardProduto>
  </div>
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
      this.updateListCarrinho()
      },
    methods: {
      updateListCarrinho(){
        axios.get('floriculturaapp/carrinho').then(response => {
          this.listaCarrinho = response.data
        })
    },
      DeleteItemCarrinho(id){
          axios.delete('floriculturaapp/carrinho/'+ id).then(() => {
            this.updateListCarrinho();
          })
      },
      updateQuantidade(carrinho, novaQuantidade) {
        
        if (novaQuantidade == 0) {
          this.DeleteItemCarrinho(carrinho.id)
        } else {
          axios.put('floriculturaapp/carrinho/'+ carrinho.id, {   
            quantidade: novaQuantidade
          }, {
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            }
          }).then(() => {
            this.updateListCarrinho();
          })
        }
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
.CarrinhoVazio{
  text-align: center;
}
 </style>