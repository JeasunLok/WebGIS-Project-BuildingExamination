<!--登录-->
<template>
  <div class="register">
    <HomeHeader/>
  </div>
  <!--登录界面-->
    <div class="log_in">
      <user/>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import user from '@/components/User.vue';
  import HomeHeader from '@/components/HomeHeader.vue';
  
  export default defineComponent({
    name: 'Header',
    components: {
      HomeHeader,
      user
    },
  });
  </script>