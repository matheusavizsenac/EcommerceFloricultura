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
          Preço
          {{produto.preco}}
        </template>
        <template #footer>
            <ButtonPrime icon="pi pi-shopping-bag" label="Comprar"  @click="incrementCounter"/>
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
     counter: 0
    }
  },
  components: {},
  mounted() {
   this.getProdutos()
  },
  methods: {
    getProdutos(){
      axios.get('floriculturaapp/').then(response => {
        this.listaDeProdutos = response.data
      })
    },
   incrementCounter() {
      this.counter++;
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