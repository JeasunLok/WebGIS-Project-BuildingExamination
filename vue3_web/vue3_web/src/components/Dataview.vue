<template>
  <div id="echart" width="100%">
    <div id="echart1" style="height: 450px; width: 100%;"></div>
    <div id="echart2" style="height: 450px; width: 100%;"></div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
var echarts = require('echarts');
export default defineComponent({
  // name: 'Navigation',
  components: {

  },

  name: 'diagramAll',
  mounted: function () {
    this.drawBarChart();
    this.drawpiechart();
  },
  methods: {
    drawBarChart() {
      // 基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(document.getElementById('echart1'));

      var liwannum = 0.206322;
      var yuexiu = 0.19984;
      var haizhu = 0.172562;
      var tianhe = 0.138179;
      var baiyun = 0.113508;
      var huangpu = 0.073792;
      var panyu = 0.115517;
      var huadu = 0.065492;
      var nansha = 0.044286;
      var conghua = 0.015447;
      var zengcheng = 0.035542;

      // 绘制基本图表
      var option = {
        title: {
          text: '广州市各区建成区密度'
        },
        tooltip: {},
        legend: {
          data: ['建成区密度']
        },
        gird: {
          left: "50px",
          right: "10px",
          top: 0,
          bottom: 0
        },
        toolbox: {
          show: true,
          feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        xAxis: {
          data: ['荔湾区', '越秀区', '海珠区', '天河区', '白云区', '黄浦区', '番禺区', '花都区', '南沙区', '从化区', '增城区']
        },
        yAxis: {},
        series: [
          {
            name: '建成区密度',
            type: 'bar',
            data: [liwannum, yuexiu, haizhu, tianhe, baiyun, huangpu, panyu, huadu, nansha, conghua, zengcheng]
          }
        ]
      };

      myChart.setOption(option); //option是一个详细的配置参数
    },
    drawpiechart() {
      // 基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(document.getElementById('echart2'));

      var liwannum = 0;
      var yuexiu = 0;
      var haizhu = 0;
      var tianhe = 0;
      var baiyun = 0;
      var huangpu = 0;
      var panyu = 0;
      var huadu = 0;
      var nansha = 0;
      var conghua = 0;
      var zengcheng = 0;



      // 绘制基本图表
      var option = {
        title: {
          text: '广州市土地利用情况'
        },
        tooltip: {},
        legend: {
          data: ['土地利用类型']
        },
        grid: {
          top: "20px",
          bottom: "0px",
          left: "0px",
          right: "0px",
          borderWidth: 1
        },
        toolbox: {
          show: true,
          feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        series: [
          {
            name: '土地利用类型',
            type: 'pie',
            data: [
              {
                value: 2669652,
                name: '耕地'
              },
              {
                value: 3940147,
                name: '林地'
              },
              {
                value: 457,
                name: '灌木'
              },
              {
                value: 3701,
                name: '草地'
              },
              {
                value: 508496,
                name: '水体'
              },
              {
                value: 1738,
                name: '裸地'
              },
              {
                value: 1622246,
                name: '不透水面'
              },
            ]
          }
        ]
      };

      myChart.setOption(option); //option是一个详细的配置参数
    }
  }
})
</script>
<style scoped >
#container {
  padding: 0px;
  margin: 0px;
  width: 100%;
  height: 800px;
}



.navigation {
  width: 100%;
  height: 100%;
  border: 0.5px solid black;
}
</style>

