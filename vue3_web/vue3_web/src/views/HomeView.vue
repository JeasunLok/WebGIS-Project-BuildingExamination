<!--主页-->
<template>
  <div class="homeview">
    <el-container class="box">
      <el-header class="header_contain">
        <Header />
      </el-header>
      <el-container class="low">
        <tabs/>
      </el-container>
    </el-container>
  </div>
</template>


<script lang="ts">
import { defineComponent, reactive, provide } from 'vue';
// import axios from "axios";
import Menu from '@/components/Menu.vue';
import Header from '@/components/Header.vue';
import Choice from '@/components/Choice.vue';
import Map from '@/components/Map.vue';
import ToolBox from '@/components/ToolBox.vue';
import Footer from '@/components/Footer.vue';
import Monitor from'@/components/Monitor.vue';
import tabs from'@/components/tabs.vue'


export default defineComponent({
  name: 'HomeView',
  components: {
    ToolBox,
    Menu,
    Header,
    Choice,
    Map,
    Footer,
    Monitor,
    tabs
  },
  setup() {
    
  }
});
</script>

<style>
.homeview {
  border: 0.5px solid black;
}

.box {
  padding: 0px;
  height: 100%;
  margin: 0px;
}

.header_contain {
  height: 40px;
  border: 1px solid black;
  text-align: center;
  background-color: black;
}

</style>
