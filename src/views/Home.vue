<template>
  <v-content>
    <div class="background" style="position:absolute; display:inline"></div>
    <div class="holder">
      <!-- <v-layout row justify-space-around style="height:100%;"> -->
      <v-card class="card" style="border-radius:50px">
        <v-layout column justify-space-between style="height:95%;">
          <v-card-title>
            <v-layout row align-content-center justify-center>
              <v-card-title class="cardTitle">
                Enter a query to search
              </v-card-title>
            </v-layout>
        </v-card-title>
          <v-card-text>
          <v-layout row align-content-center justify-center>
            <v-text-field v-model="query" placeholder="Sample text..." style="padding-left:18%; padding-right:18%; font-size:calc(10% + 2.2vw);"></v-text-field>
          </v-layout>
          </v-card-text>
          <v-card-actions>
            <v-layout row justify-space-around>
              <v-btn class="btn" rounded :style="{'color':'#ffffff', 'background-color':'#5997AE', 'width':'40%'}" @click="submit_query">
                query
              </v-btn>
            </v-layout>
          </v-card-actions>
        </v-layout>
      </v-card>
      <div class="switch">
      <v-layout row justify-space-around>
        <p style="color:white;font-size:21px;">Or upload a document
          <u style="cursor:pointer;" @click="route_to_doc_upload">here</u>
        </p>
      </v-layout>
      </div>
  </div>
  </v-content>
</template>

<script>

export default {
  name: 'home',
  data () {
    return {
        query: "",
    }
  },
  methods: {
    submit_query(){
      const loader = document.querySelector('.background').animate([
        {filter: 'hue-rotate(0deg)'},
        {filter: 'hue-rotate(360deg)'}
      ],{
        duration: 2500,
        iterations: Infinity
      });

      let context = this
      console.log("the query is: " + this.query)
      setTimeout(function(){
        context.$router.push('/results')
      }, 5000)
    },
    route_to_doc_upload(){
      console.log("routing to doc upload");
      this.$router.push('/upload')
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

    /* animation: flow 2s ease-in-out infinite; */
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
  }

</style>
