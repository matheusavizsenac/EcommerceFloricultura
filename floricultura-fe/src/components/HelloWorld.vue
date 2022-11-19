<template>
  <div> 
       <CarouselList :value="produtos" :numVisible="3" :autoplayInterval="3000">
           <template #item="slotProps">
             <div class="item-produto">
               <p>{{slotProps.data.nome}}</p>
               <p>{{slotProps.data.precoUnidade}}</p>
               <div v-if="slotProps.data.imagem">
                 <img :src="require('../assets/produtos/' + slotProps.data.imagem)">
               </div>
             </div>
         </template>
       </CarouselList>
  </div>
 </template>
 
 <script>
 export default {
   name: 'HelloWorld',
   props: {
     msg: String
   },
   data(){
     return {
 
     produtos:[
       {id: 1, nome: 'Florzinha', precoUnidade: 'R$ 2,99'}, 
       {id: 2, nome: 'lírio-do-brejo', precoUnidade: 'R$ 2,99', imagem: 'lirio-do-brejo.jpeg'}, 
       {id: 3, nome: 'C', precoUnidade: 'R$ 2,99'},
       {id: 4, nome: 'D', precoUnidade: 'R$ 2,99'}, 
       {id: 5, nome: 'E', precoUnidade: 'R$ 2,99'}, 
       {id: 6, nome: 'F', precoUnidade: 'R$ 2,99'},
       {id: 7, nome: 'G', precoUnidade: 'R$ 2,99'}, 
       {id: 8, nome: 'H', precoUnidade: 'R$ 2,99'}, 
       {id: 9, nome: 'I', precoUnidade: 'R$ 2,99'},
     ]
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
 