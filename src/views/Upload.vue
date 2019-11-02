<template>
  <v-content>
    <div class="background"></div>
    <div class="holder">
      <!-- <transition name="router-anim"> -->
        <v-card class="card" style="border-radius:50px" v-if="showing">
          <v-layout column justify-space-between style="height:95%;">
            <v-card-title>
              <v-layout row align-content-center justify-center>
                <v-card-title class="cardTitle">
                  Select a document
                </v-card-title>
              </v-layout>
            </v-card-title>
            <v-card-text>
              <v-layout row align-content-center justify-center>
                <p class="cardInfo">
                  The document must be one of the
                  <br/>
                  following formats:
                  <br/>
                  .txt, .pdf, .docx
                </p>
              </v-layout>
            </v-card-text>
            <v-card-actions>
              <v-layout row justify-space-around :style="{'margin-left':'30%','margin-right':'30%'}">
                <v-file-input flat hide-details rounded dense color="" background-color="#41A5D7" :style="{'width':'40%','cursor':'pointer'}"
                label="Upload"
                >

                </v-file-input>
              </v-layout>
            </v-card-actions>
          </v-layout>
        </v-card>
      <!-- </transition> -->
        <div class="switch">
          <v-layout row justify-space-around>
            <p style="color:white;font-size:21px;">Or query for a document
              <u style="cursor:pointer;" @click="route_to_doc_upload">here</u>
            </p>
          </v-layout>
        </div>
    </div>
  </v-content>
</template>

<script>

export default {
  name: 'upload',
  data () {
    return {
        query: "",
        transitionName: 'slide',
        showing:true
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
      // this.showing = !this.showing
    },
    handleFiles(){
      console.log("handling!")
      console.log(files)
    }
  }
}
</script>

<style scoped>
.router-anim-enter-active{
  animation: enter 1s;
  animation-delay: .5s;
  opacity: 0;
}

.router-anim-leave-active{
  animation: leave 1s;
  animation-delay: .5s;
  opacity: 0;
}

@keyframes enter {
  from{
    transition: translateX(-100px);
    opacity: 0;
  }
  to{
    transition: translateX(0px);
    opacity: 1;
  }
}

@keyframes leave {
  from{
    transition: translateX(0px);
    /* opacity: 1; */
  }
  to{
    transition: translateX(100px);
    /* opacity: 0; */
  }
}

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

  .cardInfo{
    font-size: 1.6vw;
    font-family: 'Montserrat', sans-serif;
    font-weight: 100;
    color: #707070;
    margin-top: 1%;
    text-align: center;
  }

  .switch{
    display: grid;
    grid-column-start: 2;
    grid-row-start: 3;
  }

  .style{
    width: 0.1px;
	height: 0.1px;
	opacity: 0;
	overflow: hidden;
	position: absolute;
	z-index: -1;
  }

</style>
