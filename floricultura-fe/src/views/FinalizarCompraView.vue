<template>
  <div>
    <span class="p-float-label">
      <InputText id="nomeUsuario" type="text" v-model="nomeUsuario"/>
      <label for="nomeUsuario">Nome</label>
    </span>
    <br />
    <span class="p-float-label">
      <InputText id="cpfUsuario" type="text" v-model="cpfUsuario"/>
      <label for="cpfUsuario">CPF</label>
    </span>
    <br />

    <div>
      <h1>Endereço</h1>
      <div id="divSeuCep" class="carrinho">
        <span class="p-input-icon-left">
          <i class="pi pi-truck" />
          <InputText type="text" v-model="cep" placeholder="Seu CEP" />
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
      nomeUsuario: '',
      cpfUsuario:'',
      cep: '',
      rua:'',
      bairro: '',
      cidade:'',
      estado:'',
      numero:'',
      complemento: '',
      numeroCartao: '',
      mesExpiracao: '',
      anoExpiracao: '',
      codSeguranca: '',
      nomeCartao: '',
      listaCarrinho: []
    }
  },
  mounted() {
      this.getCarrinho()
  },
  methods: {
  realizarPagamento(){
    let dados ={
      "reference_id": (Math.random() + 1).toString(36).substring(2),
      "customer": {
          "name": this.nomeUsuario,
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
      "items": [],
      "qr_code": {
          "amount": {
              "value": 500
          }
      },
      "shipping": {
          "address": {
              "street": this.rua,
              "number": this.numero,
              "complement": this.complemento,
              "locality": this.bairro,
              "city": this.cidade,
              "region_code": this.estado, //usuario precisa informar estado como codigo (UF)
              "country": "BRA",
              "postal_code": this.cep
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
                      "number": this.numeroCartao,
                      "exp_month": this.mesExpiracao,
                      "exp_year": this.anoExpiracao,
                      "security_code": this.codSeguranca,
                      "holder": {
                          "name": this.nomeCartao
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
    let total = 0;
    for (let i = 0; i < this.listaCarrinho.length; i++) {
      dados.items.push(          {
              "reference_id": this.listaCarrinho[i].idProduto.id,
              "name": this.listaCarrinho[i].idProduto.nome,
              "quantity": this.listaCarrinho[i].quantidade,
              "unit_amount": this.listaCarrinho[i].idProduto.preco
          })
      total= this.listaCarrinho[i].idProduto.preco *  this.listaCarrinho[i].quantidade + total 
    }

    dados.charges[0].amount.value = total

    console.log(dados)
    axios.post('floriculturaapp/compra/finalizar', dados)

   this.LimparCarrinho()
  },

  getCarrinho(){
        axios.get('floriculturaapp/carrinho').then(response => {
          this.listaCarrinho = response.data
        })
  },

  LimparCarrinho(){
      for (let i = 0; i < this.listaCarrinho.length; i++) {
        axios.delete('floriculturaapp/carrinho/'+ this.listaCarrinho[i].id).then(() => {
          })
      }
      this.getCarrinho()
    }
  
}
}
</script>