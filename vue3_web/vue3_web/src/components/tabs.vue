<!--导航栏-->
<template>
  <div class="box">
    <el-tabs type="border-card" class="tabs">
        <!--<el-tab-pane label="监测系统" name="first"></el-tab-pane>-->
        <!--<el-tab-pane label="导航系统" name="second"></el-tab-pane>-->
        <router-link :to="a.url" :key="index" v-for="(a,index) in Data" class="item">{{a.title}}</router-link>
    </el-tabs>
    <div class="main">
      <router-view></router-view>
        <!--<Monitor v-if="activeName=='first'" /> -->   
        <!--<Navigation v-if="activeName=='second'" />-->
    </div>
 

  </div>
</template>
  
<script lang="ts">
import { defineComponent, ref } from 'vue';
import Monitor from './Monitor.vue'
import Navigation from './Navigation.vue'


export default defineComponent({
  name: 'Tabs',
  components: {
    Monitor,
    Navigation

  },
  setup() {
    /*const activeIndex = ref('1')
    const handleSelect = (key: string, keyPath: string[]) => {
      console.log(key, keyPath)
    }

    let activeName = ref('first')    //定义 activeName
        
     //将 activeName 存入 sessionStorage
    const handleClick = () => {
        sessionStorage.setItem('_crmCurrentTab', activeName.value);
        
    }*/
    const navData={
    "navData":[
    {
     "title":"监测系统",
     "url":"/homeview"
    },
    {
     "title":"探索系统",
     "url":"/homeview/nav"
    },
    {
     "title":"数据可视",
     "url":"/homeview/dataview"
    }
    ]
   }
   let Data=navData.navData;
    //将当前 activeName 设置成已经保存的 sessionStorage
   /* const changeTag = () => {
      const name = sessionStorage.getItem('_crmCurrentTab');
      if (name) {
        activeName.value = name;
      }
    }*/

    return {
      Data
    }
  }

});
</script>

<style scoped>
.box {
  padding: 0px;
  margin: 0px;
  width:100%;
}

.tabs {
  height: 40px;
}
.main{
  width:100%;
}

.item{
  text-align: center;
  padding-left:9px ;
  padding-right:9px ;
  text-decoration:none;
  color:black;
  border-right: 1px solid #000;

}
.item:hover {
  background-color: rgba(0, 0, 234, 0.2);
}

</style>