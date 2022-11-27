<template>
    <div>
        <span class="p-float-label">
            <InputText id="nomeUsuario" type="text"/>
            <label for="nomeUsuario">Nome</label>
        </span>
        
        <span class="p-float-label">
                <InputText id="cpfUsuario" type="text"/>
                <label for="cpfUsuario">CPF</label>
        </span>

        <div id="divSeuCep" class="carrinho">
      <span class="p-input-icon-left">
            <i class="pi pi-truck"/>
            <InputText type="text" v-model="value" placeholder="Seu CEP" />
        </span>
    </div>
    </div>
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
