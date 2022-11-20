<template>
    <div id="UsuariosBotoes">
        <router-link :to="{ name: 'novoUsuario' }">
            <ButtonPrime label="Cadastrar" icon="pi pi-user-plus" iconPos="right" />
        </router-link>
        <router-link :to="{ name: 'loginUsuario' }">
            <ButtonPrime label="Já tenho cadastro" icon="pi pi-user" iconPos="right" />
        </router-link>
    </div>
</template>
<style>
#UsuariosBotoes{
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>