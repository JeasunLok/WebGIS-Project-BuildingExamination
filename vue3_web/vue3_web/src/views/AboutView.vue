<!--主页-->
<template>
  <div class="homeview">
    <el-container class="box">
      <el-header class="header_contain">
        <Header />
      </el-header>
      <el-header class="menu_contain">
        <Menu />
      </el-header>
      <el-container class="low">
        <Monitor></Monitor>
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
import { apiGetURL } from '../apis/getURL'

interface ITime_Return {
  Date_start: string;
  Date_end: string;
}

interface IResult_URL {
  Image_URL: string;
  Feature_URL: string;
}

export default defineComponent({
  name: 'HomeView',
  components: {
    ToolBox,
    Menu,
    Header,
    Choice,
    Map,
    Footer,
    Monitor
  },
  setup() {
    var time: ITime_Return = reactive({
      Date_start: " ",
      Date_end: " "
    })
    var result_URL: IResult_URL = reactive({
      Image_URL: " ",
      Feature_URL: " "
    })
    const time_return = (value: ITime_Return) => {
      // time.Date_start = value[0]
      // time.Date_end = value[1]
      time = value

      console.log(time)
      // console.log(Date.now().toString())

      result_URL.Image_URL = '1'
      result_URL.Feature_URL = '2'
      // apiGetURL(time).then((res) => {
      //   console.log(res)
      // })
      apiGetURL().then((res) => {
        console.log(res)
      })
    }
    provide("result_URL", result_URL)
    return {
      time_return,
      time
    }
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

.menu_contain {
  height: 40px !important;
  text-align: center;
}

.low {
  height: calc(100vh - 98px);
  border: 0.5px solid black;
}

</style>