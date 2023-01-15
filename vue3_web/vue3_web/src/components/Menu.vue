<!--菜单栏-->
<template>
  <div class="menu">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" router @select="handleSelect">
      <el-menu-item index="/">>首页</el-menu-item>
      <el-tabs type="border-card">
        <el-tab-pane label="监测系统" name="monitor"></el-tab-pane>
        <el-tab-pane label="导航系统" name="navigation"></el-tab-pane>
      </el-tabs>
      <el-button class="analysis" type="primary">叠加分析</el-button>
      <router-view />
    </el-menu>

  </div>
</template>
  
<script lang="ts">
import { defineComponent, ref } from 'vue';


export default defineComponent({
  name: 'Menu',
  components: {

  },
  setup() {
    const activeIndex = ref('1')
    const handleSelect = (key: string, keyPath: string[]) => {
      console.log(key, keyPath)
    }
    return {
      activeIndex,
      handleSelect,
    }
  }

});
</script>

<style scoped>
.menu {
  line-height: 38px;
  padding: 0px;
  margin: 0px;
}

.el-menu-demo {
  height: 40px;
}

.analysis {
  margin-top: 4.3px;
  margin-left: 20px;
  float: right;
}
</style>