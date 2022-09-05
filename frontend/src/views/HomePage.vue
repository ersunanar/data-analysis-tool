<template>
  <div id="app">
    <h1></h1>
  </div>
</template>

<!----------------------------- SCRIPT ---------------------------------------------------------->

<script>


export default {
  name: 'HomePage',

  data() {
    return {

    };
  },

  methods: {

  },

  mounted() {

  },
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

  menu {
    width: 25%;
    float: left;
    padding: 5px;

  }

  main {
    width: 75%;
    float: left;
    padding: 5px;

  }


.container {
  background: aqua;

  padding: 10px;
}

.one {
  width: 100%;
  background: white;
}

.two {
  width: 100%;
  background: grey;
}
</style>
