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
    let data = {
      "reference_id": "ex-00004",
      "customer": {
          "name": "Jose da Silva",
          "email": "email@test.com",
          "tax_id": "12345678909",
          "phones": [
              {
                  "country": "55",
                  "area": "11",
                  "number": "999999999",
                  "type": "MOBILE"
              }
          ]
      },
      "items": [
          {
              "reference_id": "referencia do item",
              "name": "nome do item",
              "quantity": 1,
              "unit_amount": 500
          }
      ],
      "qr_code": {
          "amount": {
              "value": 500
          }
      },
      "shipping": {
          "address": {
              "street": "Avenida Brigadeiro Faria Lima",
              "number": "1384",
              "complement": "apto 12",
              "locality": "Pinheiros",
              "city": "São Paulo",
              "region_code": "SP",
              "country": "BRA",
              "postal_code": "01452002"
          }
      },
      "notification_urls": [
          "https://meusite.com/notificacoes"
      ],
      "charges": [
          {
              "reference_id": "referencia do pagamento",
              "description": "descricao do pagamento",
              "amount": {
                  "value": 500,
                  "currency": "BRL"
              },
              "payment_method": {
                  "type": "CREDIT_CARD",
                  "installments": 1,
                  "capture": true,
                  "card": {
                      "number": "4111111111111111",
                      "exp_month": "12",
                      "exp_year": "2026",
                      "security_code": "123",
                      "holder": {
                          "name": "Jose da Silva"
                      },
                      "store": false
                  }
              },
              "notification_urls": [
                  "https://meusite.com/notificacoes"
              ]
          }
      ]
    }

    axios.post('floriculturaapp/compra/finalizar', data)

  }
}
}
</script>