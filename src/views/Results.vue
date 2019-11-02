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
          <v-card-text style="overflow-y: scroll; height: 65%">
          <v-layout column align-content-center justify-space-around>
            <v-divider/>
            <div v-for="item in results">
              <p>{{item.title}}</p>
              <p>{{item.text}}</p>
              <v-divider/>
            </div>
          </v-layout>
          </v-card-text>
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

export default {
  name: 'results',
  data () {
    return {
        query: "",
        results: [
          {
            title:"doc1",
            text:"lorem lipsm"
          },
          {
            title:"doc2",
            text:"lorem lipsm also"
          },
          {
            title:"doc3",
            text:"lorem lipsm also"
          },
          {
            title:"doc4",
            text:"lorem lipsm also"
          },
          {
            title:"doc5",
            text:"lorem lipsm also"
          },
          {
            title:"doc6",
            text:"lorem lipsm also"
          },
          {
            title:"doc2",
            text:"lorem lipsm also"
          },
        ]
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
