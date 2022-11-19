<template>
  <div>
    <div class="header">
      <img class="logo-header" alt="Floricultura logo" src="@/assets/logo-floricultura.png">
      <div>
        <span class="p-input-icon-left">
            <i class="pi pi-search"/>
            <InputText type="text" v-model="value" placeholder="O que você procura?" />
        </span>
      </div>
    </div>
    <TabMenu class="tab-menu-geral" :model="items" />
    <router-view/>
  </div>
</template>

<script>
export default {
	data() {
		return {
			items: [
        {label: 'Home', icon: 'pi pi-fw pi-home', to: '/'},
        {label: 'Produtos', icon: 'pi pi-fw pi-heart-fill', to: '/produtos'},
        {label: 'Carrinho', icon: 'pi pi-fw pi-shopping-cart', to: '/carrinho'},
      ],
      value: '',
		}
	}
}
</script>

<style>

body {
  background: #eff3f8;
}

.logo-header{
  height: 100px;
  position: absolute;
  top: 10px;
  left: 10px;
}

.header {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 120px;
  background-color: #fff;
}
.tab-menu-geral {
  margin-bottom: 10px;
}


</style>
