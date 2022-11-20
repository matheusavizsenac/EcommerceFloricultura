<template>
<div>
    <h1>Acessar conta</h1>
    <span class="p-float-label">
        <InputText id="nomeUsuario" type="text" v-model="nome" />
        <label for="nomeUsuario">Nome</label>
    </span>
    
    <span class="p-float-label">
            <InputText id="senhaUsuario" type="text" v-model="senha" />
            <label for="senhaUsuario">Senha</label>
    </span>

    <ButtonPrime label="Login" />

</div>
</template>