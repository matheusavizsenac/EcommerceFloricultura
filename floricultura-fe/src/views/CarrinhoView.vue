<template>
  <div>
      <CardProduto class="produto">
        <template #header>
          <ButtonPrime id="buttonDeletar" icon="pi pi-trash" />
        </template>
        <template #title>
            Teste Produto
        </template>
        <template #content>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt
            quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!
        </template>
    </CardProduto>
  </div>
  <div id="divSeuCep" class="carrinho">
      <span class="p-input-icon-left">
            <i class="pi pi-truck"/>
            <InputText type="text" v-model="value" placeholder="Seu CEP" />
        </span>
    </div>
    <ButtonPrime id="buttonFinalizarCompra" label="Finalizar compra" icon="pi pi-check" iconPos="right" />
  </template>
  
<script>
  export default {
    data() {
      return {
        value: '',
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