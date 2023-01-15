<!--主页-->
<template>
    <div class="home">
      <el-container class="box">
        <el-header class="header_contain">
          <Header/>
        </el-header>
        <el-header class="menu_contain">
          <Menu/>
        </el-header>
        <el-container class="low">
        <el-aside width="400px" class="side">
          <Aside1/>
        </el-aside>
        <el-container>
          <el-header class="header_small">Header</el-header>
          <el-main class="map_fill">Main</el-main>
          <el-footer class="footer">Footer</el-footer>
        </el-container>
        </el-container>
      </el-container>
    </div>
  </template>
  
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  //import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src
  import Menu from '@/components/Menu.vue';
  import Header from '@/components/Header.vue';
  import Choice from '@/components/Choice.vue';
  
  export default defineComponent({
    name: 'HomeView',
    components: {
      //HelloWorld,
      Menu,
      Header,
      Choice
    },
  });
  </script>
  
  <style>
  .home,
  .box{
    padding:0px;
    height: 100%;
    margin:0px;
  }
  .header_contain{
    line-height:30px;
    border: 1px solid black;
    text-align: center;
    background-color: black;
  }
  .menu_contain{
    height:40px;
    text-align: center;
  }
  .low {
      height: calc(100vh - 80px);
      border: 0.5px solid black;
  }
  .header_small {
      line-height: 30px;
      background-color:coral;
      border: 0.5px solid black
  }
  .map_fill{
    background-color: bisque;
    border: 0.5px solid black;
  }
  .footer{
    background-color: aquamarine;
    border: 0.5px solid black;
    height: 30px !important;
  }
  </style>
  