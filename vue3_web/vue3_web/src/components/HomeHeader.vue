<template>
    <el-affix :offset="0">
        <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        background-color="#000000"
        text-color="#fff"
        router
        :ellipsis="false"
        @select="handleSelect"
        fixed
        > <span class="acronym"><router-link to="/" class="router">DSTS</router-link></span>
        <!--<el-menu-item index="0"></el-menu-item>-->
        <div class="flex-grow" />
        <el-menu-item index="/homeview">体验功能</el-menu-item>
        </el-menu>
    </el-affix>
  </template>
  
  <script lang="ts" setup>
  import { ref } from 'vue'
  
  const activeIndex = ref('1')
  const handleSelect = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
  }
  </script>
  
  <style>
 
  .flex-grow {
    flex-grow: 1;
  }
  .acronym{
    height: 50px;
    width: 90px;
    left:20px;
    top:15px;
    text-align: center;
    line-height: 50px;
    font-weight: bolder;
    font-size: 30px;
  }
  .router{
    text-decoration: none;
    color: aliceblue;

  }
  </style>