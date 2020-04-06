<template>
  <div id="app">
    <v-app>
      <Navbar />
      <router-view/>
    </v-app>
  </div>
</template>

<script>
  import Navbar from "./components/Navbar";

  export default {
    name: "app",
    components: {
      Navbar
    },
  }
</script>

<style lang="scss">
  #v-content { 
    height: 100vh;
    background-color: #fff;
  }
</style>
