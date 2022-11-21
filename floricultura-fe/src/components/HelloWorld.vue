<template>
  <div> 
       <CarouselList :value="listaDeProdutos" :numVisible="3" :autoplayInterval="3000">
           <template #item="slotProps">
             <div class="item-produto">
               <p>{{slotProps.data.nome}}</p>
               <p>R$ {{slotProps.data.preco}}</p>
               <div v-if="slotProps.data.imagem">
                 <img :src="require('../assets/produtos' + slotProps.data.imagem)">
               </div>
             </div>
         </template>
       </CarouselList>
  </div>
 </template>
 
 <script>
 import axios from 'axios'
 export default {
   name: 'HelloWorld',
   props: {
     msg: String
   },
   data(){
     return {
      listaDeProdutos:[],
     }
   },
   components: {},
   mounted() {
    this.getProdutos()
   },
   methods: {
    getProdutos(){
      axios.get('floriculturaapp/').then(response => {this.listaDeProdutos = response.data})
    }
   }
 }
 </script>
 
 <!-- Add "scoped" attribute to limit CSS to this component only -->
 <style scoped>
 h3 {
   margin: 40px 0 0;
 }
 ul {
   list-style-type: none;
   padding: 0;
 }
 li {
   display: inline-block;
   margin: 0 10px;
 }
 a {
   color: #42b983;
 }
 .item-produto {
   padding: 100px; 
   box-shadow: 0 0 5px #ccc;
   border-radius: 10px;
   margin: 10px;
 }
 </style>
 