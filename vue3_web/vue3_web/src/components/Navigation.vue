<template>
  <div id="myPageTop">
    <table>
      <tr>
        <td>
          <label>请输入关键字：</label>
        </td>
      </tr>
      <tr>
        <td>
          <input id="tipinput" />
        </td>
      </tr>
    </table>
  </div>
  <div id="container"></div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { shallowRef } from '@vue/reactivity'
import AMapLoader from '@amap/amap-jsapi-loader';

export default defineComponent({
  name: 'Navigation',
  components: {

  },
  setup() {
    const map: any = shallowRef(null);
    var autoOptions = {
      input: "tipinput"
    };

    AMapLoader.load({
      key: "9faf74f12342532d9ffbce4cdab68959",             // 申请好的Web端开发者Key，首次调用 load 时必填
      version: "2.0",      // 指定要加载的 JSAPI 的版本，缺省时默认为 1.4.15
      plugins: [''],       // 需要使用的的插件列表，如比例尺'AMap.Scale'等
    }).then((AMap) => {
      AMap.plugin(['AMap.PlaceSearch', 'AMap.AutoComplete'], function () {
        var auto = new AMap.AutoComplete(autoOptions);
        var placeSearch = new AMap.PlaceSearch({
          map: map
        });  //构造地点查询类
        auto.on("select", select);//注册监听，当选中某条记录时会触发
        function select(e: any) {
          placeSearch.setCity(e.poi.adcode);
          placeSearch.search(e.poi.name);  //关键字查询查询
        }
      });
    })

    return {
      map,
    }
  },
  methods: {
    initMap() {
      AMapLoader.load({
        key: "9faf74f12342532d9ffbce4cdab68959",             // 申请好的Web端开发者Key，首次调用 load 时必填
        version: "2.0",      // 指定要加载的 JSAPI 的版本，缺省时默认为 1.4.15
        plugins: ['AMap.Scale'],       // 需要使用的的插件列表，如比例尺'AMap.Scale'等
      }).then((AMap) => {
        this.map = new AMap.Map("container", {  //设置地图容器id
          viewMode: "3D",    //是否为3D地图模式
          zoom: 8,           //初始化地图级别
          center: [113.3, 23.1], //初始化地图中心点位置
        });
          
      }).catch(e => {
        console.log(e);
      })
    },
  },
  mounted() {
    //DOM初始化完成进行地图初始化
    this.initMap();

  }
})
</script>
<style scoped >
#container {
  padding: 0px;
  margin: 0px;
  width: 100%;
  height: 900px;
}

#tip {
  background-color: #fff;
  padding-left: 10px;
  padding-right: 10px;
  position: absolute;
  font-size: 12px;
  right: 10px;
  top: 20px;
  border-radius: 3px;
  border: 1px solid #ccc;
  line-height: 30px;
}


#myPageTop {
  position: absolute;
  top: 5px;
  right: 10px;
  background: #fff none repeat scroll 0 0;
  border: 1px solid #ccc;
  margin: 10px auto;
  padding: 6px;
  font-family: "Microsoft Yahei", "微软雅黑", "Pinghei";
  font-size: 14px;
}

#myPageTop label {
  margin: 0 20px 0 0;
  color: #666666;
  font-weight: normal;
}

#myPageTop input {
  width: 170px;
}

</style>

