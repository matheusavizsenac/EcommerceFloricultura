<template>
  <div class="content">
    <CardProduto class="produto">
        <template #title>
            Teste Produto
        </template>
        <template #content>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt
            quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!
        </template>
        <template #footer>
            <ButtonPrime icon="pi pi-shopping-bag" label="Comprar"/>
            <ButtonPrime icon="pi pi-eye" label="Espiar" class="p-button-secondary" style="margin-left: .5em" />
        </template>
    </CardProduto>
  </div>
</template>

<style>
.produto{
  width: 75%;
}

.content {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>