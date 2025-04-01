<template>
  <div id="app">
    <OperadorasList />
  </div>
</template>

<script>
import OperadorasList from './components/OperadorasList.vue';

export default {
  name: 'App',
  components: {
    OperadorasList,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
