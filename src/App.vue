<template>
  <v-app>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  data: () => ({
    //
  }),
};
</script>

<style>
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
  from{transition: translateX(-100%);}
  to{transition: translateX(0px);}
}

@keyframes leave {
  from{transition: translateX(0px);}
  to{transition: translateX(-100%);}
}
</style>
