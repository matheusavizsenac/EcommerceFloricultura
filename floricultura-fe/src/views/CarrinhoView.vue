<template>
  <div>
      <CardProduto class="produto">
        <template #header>
          <ButtonPrime icon="pi pi-trash" style="margin-left: .5em"/>
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
  <div class="carrinho">
      <span class="p-input-icon-left">
            <i class="pi pi-truck"/>
            <InputText type="text" v-model="value" placeholder="Seu CEP" />
        </span>
    </div>
    <ButtonPrime label="Finalizar compra" icon="pi pi-check" iconPos="right" />
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