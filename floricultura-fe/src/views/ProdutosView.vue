<template>
  <div class="content">
    <CardProduto class="produto" v-for="(produto) in listaDeProdutos" :key="produto.id">
        <template #header>
          <ImagePrime class="imagemProduto" :src="require('../assets/produtos' + produto.imagem)" :preview="true">
            <template #indicator>
              Visualizar produto
            </template>
          </ImagePrime>
        </template>
        <template #title>
          {{produto.nome}}
        </template>
        <template #content>
          {{produto.descricao}}
          <br/>
          Preço R$
          {{produto.preco}}
        </template>
        <template #footer>
            <ButtonPrime icon="pi pi-shopping-bag" label="Comprar"  @click="AdicionarCarrinho(produto.id)" />
        </template>
    </CardProduto>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data(){
    return {
     listaDeProdutos:[],
    }
  },
  components: {},
  mounted() {
   this.getProdutos()
  },
  methods: {
    getProdutos(){
      axios.get('floriculturaapp/produto').then(response => {
        this.listaDeProdutos = response.data
      })
    },
    AdicionarCarrinho(produto){
      //post de produto pro carrinho
      axios.post('floriculturaapp/carrinho', {
        quantidade: 1,
        idUsuario: 1,
        idProduto: produto
       }, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
      })
      //mostrar mensagem de adicionado
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });     
    }
  }
}
</script>

<style>
.produto{
  width: 75%;
  margin: 2%;
}

.content {
  display: flex;
  align-items: center;
  justify-content: center;
}

.imagemProduto {
  width: 100%;
  height: 200px;
  display: flex !important;
}

</style>