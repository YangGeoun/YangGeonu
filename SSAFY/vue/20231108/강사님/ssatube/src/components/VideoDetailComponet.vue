<template>
  <div>
    <h1>여기는 디테일</h1>
    <div v-if="selectedVideo" class="box">
      <iframe :src="videoUrl" frameborder="0"></iframe>
    </div>
    <p v-else>
      선택된 비디오가 없습니다.
    </p>
  </div>
</template>

<script setup>
  import { computed } from 'vue'
  const props = defineProps({selectedVideo:Object})
  const videoUrl = computed(()=> {
    return `https://www.youtube.com/embed/${props.selectedVideo?.id.videoId}`
  })
  
</script>

<style scoped>
  .box {
    position: relative; /* absolute는 부모가 relative일 때 부모를 따라간다. */
    width: 100%;
    padding-bottom: 56.25%; /* 16:9 비율 */
  }

  iframe {
    position: absolute;
    width: 100%; /* 부모에 맞게 꽉 채운다. */
    height: 100%;
  }
</style>