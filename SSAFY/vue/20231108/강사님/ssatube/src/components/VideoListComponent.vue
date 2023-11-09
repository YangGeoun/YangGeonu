<template>
  <div>
    <h1>여기는 리스트</h1>
    <ul>
      <VideoListItemComponent
      v-for="video of videoList"
      :key="video.id"
      :video="video"
      @item-select="onItemSelect"/>

    </ul>
    
  </div>
</template>

<script setup>
  import VideoListItemComponent from './VideoListItemComponent.vue';
  defineProps(
    {videoList:Array},
  )
  const emit = defineEmits(['itemSelect'])
  const onItemSelect = function(video) {
    emit('itemSelect',video)
  }
</script>
  
<style scoped>

</style>