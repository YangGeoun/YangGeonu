<template>
  <div>
    <h1>여기는 서치바</h1>
    <input type="text" v-model="searchText">
    <button @click="search">검색</button>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  const searchText = ref('') 
  const emit = defineEmits(['search'])
  const search = function () {
    emit('search',searchText.value)
  }

</script>

<style scoped>

</style>