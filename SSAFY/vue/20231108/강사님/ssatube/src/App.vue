<template>
  <div class="container">
    <header>
      <SearchBarComponent 
      @search="updateList"/>
    </header>
    <main>
      <div class="d-flex row">
        <div class="col-8">
          <VideoDetailComponet 
          :selected-video="selectedVideo"
          />
        </div>
        <div class="col-4">
          <VideoListComponent 
          :video-list="videoList"
          @item-select="onItemSelect"
        />
        </div>
      </div>
    </main>
  </div>
  
</template>

<script setup>
  import axios from 'axios'
  import SearchBarComponent from './components/SearchBarComponent.vue';
  import VideoDetailComponet from './components/VideoDetailComponet.vue';
  import VideoListComponent from './components/VideoListComponent.vue';

  import { ref, onMounted } from 'vue'

  const url = 'https://www.googleapis.com/youtube/v3/search'
  
  onMounted(() => {
   
  })

  const updateList = function (searchText) {
    console.log(searchText)
    axios({
      url:url,
      params:{
        type : 'video',
        part : 'snippet',
        key : 'AIzaSyBzTwrrgnQjmnDFnKRkRlLrQvG8_apTpuQ',
        q : `${searchText}`
      }
    })
    .then((response) => {
    console.log(response.data.items)
    videoList.value = response.data.items
    })
    .catch((error)=> {
    console.log(error)
    })

  }

  const onItemSelect = function (video) {
    
    console.log("다 올라옴")
    console.log(video)
    selectedVideo.value = video
  }
  const videoList = ref([
  ])
  const selectedVideo = ref(null)
  const keyword = ref('')
</script>

<style scoped>
</style>