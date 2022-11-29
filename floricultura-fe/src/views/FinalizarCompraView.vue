<template>
  <div>
    <span class="p-float-label">
      <InputText id="nomeUsuario" type="text" />
      <label for="nomeUsuario">Nome</label>
    </span>
    <br />
    <span class="p-float-label">
      <InputText id="cpfUsuario" type="text" />
      <label for="cpfUsuario">CPF</label>
    </span>
    <br />

    <div>
      <h1>Endereço</h1>
      <div id="divSeuCep" class="carrinho">
        <span class="p-input-icon-left">
          <i class="pi pi-truck" />
          <InputText type="text" v-model="value" placeholder="Seu CEP" />
        </span>
      </div>
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
    <br />

    <div>
      <h1>Cartão</h1>
      <span class="p-float-label">
        <InputText id="numeroCartao" type="text" v-model="numeroCartao" />
        <label for="numeroCartao">Número</label>
      </span>
      <span class="p-float-label">
        <InputText id="mesExpiracao" type="text" v-model="mesExpiracao" />
        <label for="mesExpiracao">Mês Expiração</label>
      </span>
      <span class="p-float-label">
        <InputText id="anoExpiracao" type="text" v-model="anoExpiracao" />
        <label for="anoExpiracao">Ano Expiração</label>
      </span>
      <span class="p-float-label">
        <InputText id="codSeguranca" type="text" v-model="codSeguranca" />
        <label for="codSeguranca">Código de Segurança</label>
      </span>
      <span class="p-float-label">
        <InputText id="nomeCartao" type="text" v-model="nomeCartao" />
        <label for="nomeCartao">Nome no cartão</label>
      </span>
    </div>

    <ButtonPrime id="buttonPagamento" icon="pi-money-bill" label="Realizar Pagamento" @click="realizarPagamento()"/>


  </div>
</template>


<script>
import axios from 'axios'
export default {
  data() {
    return {
      value: '',
    }
  },
  methods: {
  realizarPagamento(){
    axios.post('https://sandbox.api.pagseguro.com/order')
    ({
     // json=data, 
    })
    headers={'Authorization': 'Bearer 540CD5FAE4074E4D87F9BA20A897A93E'}
  }
}
}
</script>