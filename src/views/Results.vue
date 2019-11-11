<template>
  <v-content>
    <div class="background" style="position:absolute; display:inline"></div>
    <div class="holder">
      <!-- <v-layout row justify-space-around style="height:100%;"> -->
      <v-card class="card" style="border-radius:50px">
        <v-layout column align-center style="height:95%;">
          <v-card-title>
            <v-layout row align-content-center justify-center>
              <v-card-title class="cardTitle">
                Here is what we found:
              </v-card-title>
            </v-layout>
        </v-card-title>
          <div style="overflow-y:hidden; overflow-x:hidden;height: 75%; width: 100%">
          <v-card-text style="height: 50vh; overflow-y:scroll">
          <v-layout column align-content-center justify-space-around style="overflow-y:hidden;">
            <v-divider/>
            <div v-for="item in results">
              <span>
                <v-layout row style="margin-left:2px; margin-right:5px">
                <p style="display:inline;"> {{item.document.name}} </p>
                <v-spacer/>
                <p style="display:inline;"> score: {{item.score.toFixed(3)}}</p>
                </v-layout>
              </span>
              <p :class="item.document.name"></p>
              <v-divider/>
            </div>
          </v-layout>
          </v-card-text>
          </div>
        </v-layout>
      </v-card>

      <div class="switch">
      <v-layout row justify-space-around>
        <p style="color:white;font-size:21px;">Query for another document
          <u style="cursor:pointer;" @click="route_to_doc_upload">here</u>
        </p>
      </v-layout>
      </div>
  </div>
  </v-content>
</template>

<script>

import { mapState } from 'vuex'

export default {
  name: 'results',
  computed : { ...mapState( ['results'] ) },
  data () {
    return {
        query: "",
        results_for_page: this.results
    }
  },
  mounted(){
    console.log(this.results)

    for( let index in this.results){
      let item = this.results[index]
      let className = item.document.name

      item.document.text = item.document.text.replace('\n','<br/>')

      console.log(className)
      let containers = document.getElementsByClassName(className)
      console.log(containers)
      console.log(containers.length)
      console.log(containers[0])
      for(let index = 0; index < containers.length; index++){
        console.log("index: ", index)
        containers[index].innerHTML = item.document.text
      }
    }
  },
  methods: {
    submit_query(){
      const loader = document.querySelector('.background').animate([
        {filter: 'hue-rotate(0deg)'},
        {filter: 'hue-rotate(360deg)'}
      ],{
        duration: 2500,
        iterations: 4
      });
      console.log("the query is: " + this.query)
    },
    route_to_doc_upload(){
      console.log("routing to doc upload");
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>

@keyframes flow{
  0% {
      filter: hue-rotate(0deg);
    }
    100% {
      filter: hue-rotate(360deg);
    }
}

  .background{
    background: linear-gradient(to right top,#41A5D7,#00853E);
    height: 100vh;
    width: 100%;
    position: absolute;
    top: 0;
    left:0;
    /* z-index: -1; */

    /* animation: flow 1s ease-in-out infinite; */
  }

  .holder{
    height: 100vh;
    width: 100%;
    background-color: transparent;
    position: relative;
    align-items: center;
    align-content: center;
    justify-content: center;
    display: grid;
    grid-template-columns: 15% 70% 15%;
    grid-template-rows: 15% 65% 5% 15%;
  }

  .card{
    border-radius: 50px;
    width: 100%;
    height: 100%;
    display: grid;
    grid-column-start: 2;
    grid-row-start: 2;
  }

  .cardTitle{
    /* font-size: 4.3rem; */
    font-size: 4.3vw;
    font-family: 'Montserrat', sans-serif;
    font-weight: 100;
    color: #707070;
    margin-top: 1%;
  }

  .switch{
    display: grid;
    grid-column-start: 2;
    grid-row-start: 3;
    z-index: 4;
  }

</style>
