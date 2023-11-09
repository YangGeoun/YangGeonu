<template>
  <div>
    <h1>Userview</h1>
    <h2>{{ $route.params.id }}번 User 페이지</h2>
    <p>{{userId}}</p>
    <button @click="goHome">홈으로</button>
    <button @click="goAnotherUser">100번 유저 페이지로</button>
  </div>
</template>

<script setup> 
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router';
import { ref } from 'vue'

const router = useRouter()
const route = useRoute()

const userId = ref(route.params.id)

onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('정말 떠나실 건가요?')
  if (answer === false) {
    return false
  }
})

const goAnotherUser = function () {
  router.push({name:'user',params:{id:100}})
}

onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.id
})

const goHome = function() {
  // router.push({ name: 'home'})
  router.replace({ name:'home'})
}
</script>

<style scoped>

</style>