<!--侧边栏1-->
<template>
    <div class="aside1">
      <el-scrollbar class="el-scrollbar">
        <p v-for="item in 20" :key="item" class="scrollbar-demo-item">{{ item }}</p>
      </el-scrollbar>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  //import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src
  
  export default defineComponent({
    name: 'Aside1',
    components: {
      //HelloWorld,
    },
  });
  </script>

<style scoped>
.aside1{
    top:90px;
}
.scrollbar-demo-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  margin: 10px;
  text-align: center;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
}
</style>