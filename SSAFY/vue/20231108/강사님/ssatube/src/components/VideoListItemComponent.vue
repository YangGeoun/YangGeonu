<template>
  <li @click="onClick">
    <p>{{ video.snippet.title }}</p>
    <img :src="URL" alt="">
  </li>
</template>

<script setup>
  const props = defineProps({video:Object})
  const emit = defineEmits(['itemSelect'])
  const onClick = function () {
    emit('itemSelect', props.video)
  }
  const URL = props.video.snippet.thumbnails.medium.url
</script>

<style scoped>

</style>