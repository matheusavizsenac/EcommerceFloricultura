<template>
<div>
    <h1>Cadastro</h1>
    <span class="p-float-label">
        <InputText id="nomeUsuario" type="text" v-model="nome" />
        <label for="nomeUsuario">Nome</label>
    </span>
    
    <span class="p-float-label">
            <InputText id="senhaUsuario" type="text" v-model="senha" />
            <label for="senhaUsuario">Senha</label>
    </span>
</div>

<div>
    <p>Endereço</p>
    <span class="p-float-label">
        <InputText id="enderecoRua" type="text" v-model="rua" />
        <label for="enderecoRua">Rua</label>
    </span>
    <span class="p-float-label">
        <InputText id="enderecoBairro" type="text" v-model="bairro" />
        <label for="enderecoBairro">Bairro</label>
    </span>
    <span class="p-float-label">
        <InputText id="enderecoCidade" type="text" v-model="cidade" />
        <label for="enderecoCidade">Cidade</label>
    </span>
    <span class="p-float-label">
        <InputText id="enderecoEstado" type="text" v-model="estado" />
        <label for="enderecoEstado">Estado</label>
    </span>
    <span class="p-float-label">
        <InputText id="enderecoNumero" type="text" v-model="numero" />
        <label for="enderecoNumero">Número</label>
    </span>
    <span class="p-float-label">
        <InputText id="enderecoComplemento" type="text" v-model="complemento" />
        <label for="enderecoComplemento">Complemento</label>
    </span>
</div>

<ButtonPrime label="Cadastrar" />
</template>