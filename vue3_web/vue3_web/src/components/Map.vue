<template>
  <el-container>
    <el-aside class="map_layers">
      <!-- {{ map_service }} -->
      <MapLayers @mapservice="mapservice"></MapLayers>
    </el-aside>
    <el-container>
      <el-header class="toolbox">
        <ToolBox />
      </el-header>
      <el-main>
        <div id="viewDiv"></div>
      </el-main>

    </el-container>
    <!-- <div id="viewDiv"></div>
      <Footer v-show="false"></Footer> -->
  </el-container>
  <el-footer class="footer">
    <Footer />
  </el-footer>
</template>

<script lang="ts" >
import { provide, onMounted, ref, reactive, defineComponent, watchEffect, inject } from 'vue';
import Sketch from "@arcgis/core/widgets/Sketch";
import { loadModules } from 'esri-loader';
import Footer from '@/components/Footer.vue';
import MapLayers from '@/components/MapLayers.vue';
import ToolBox from '@/components/ToolBox.vue';
import LayerList from "@arcgis/core/widgets/LayerList";

import MapImageLayer from "@arcgis/core/layers/MapImageLayer";
import KMLLayer from "@arcgis/core/layers/KMLLayer";
import VectorTileLayer from "@arcgis/core/layers/VectorTileLayer";
import ImageryTileLayer from "@arcgis/core/layers/ImageryTileLayer";
import ImageryLayer from "@arcgis/core/layers/ImageryLayer";
import WMSLayer from "@arcgis/core/layers/WMSLayer";
import WFSLayer from "@arcgis/core/layers/WFSLayer";
import Legend from "@arcgis/core/widgets/Legend";
import GroupLayer from "@arcgis/core/layers/GroupLayer";
import Slider from "@arcgis/core/widgets/Slider";

const modules = ["esri/Map", 'esri/WebMap', "esri/widgets/Locate",
  "esri/widgets/Track", "esri/layers/TileLayer", 'esri/views/MapView', "esri/Graphic",
  "esri/layers/GraphicsLayer", "esri/layers/FeatureLayer", "esri/widgets/Slider",
  "esri/PopupTemplate", "esri/widgets/Sketch",]

interface IMapService {
  URL: string;
  type: string;
}

export default defineComponent({
  name: 'Map',
  components: {
    Footer,
    MapLayers,
    ToolBox
  },

  setup(props, { emit }) {
    //用于获取鼠标的经纬度坐标
    var lon = ref(0)
    var lat = ref(0)
    var map_service: IMapService = {
      URL: " ",
      type: " "
    }
    var result: any = reactive(inject("result_URL"))
    console.log(result)
    var imap: any
    var iview: any
    var layerList: any

    loadModules(modules, { css: true }).then(
      ([Map, WebMap, Locate, Track, TileLayer, MapView, Graphic,
        GraphicsLayer, FeatureLayer, PopupTemplate, SketchViewModel]) => {
        // esriConfig.apiKey = "YOUR_API_KEY";
        const graphicsLayer = new GraphicsLayer({
          title: "绘制图层",
        }
        );
        // const chinamap_layer = new FeatureLayer({
        //   url: "https://localhost:6443/arcgis/rest/services/map_1/china_map/FeatureServer",
        //   title: "中国地图"
        // });

        const USALayer = new MapImageLayer({
          url: "http://sampleserver6.arcgisonline.com/arcgis/rest/services/USA/MapServer",
          title: "美国行政"
        });

        const censusLayer = new MapImageLayer({
          url: "http://sampleserver6.arcgisonline.com/arcgis/rest/services/Census/MapServer",
          title: "美国人口",
        });

        const demographicGroupLayer = new GroupLayer({
          title: "美国示例",
          visible: true,
          visibilityMode: "exclusive",
          layers: [USALayer, censusLayer],
          opacity: 0.75
        });

        // const ourLayer = new GroupLayer({
        //   title: "图层",
        //   visible: true,
        //   visibilityMode: "exclusive",
        //   layers: [chinamap_layer, chinamap_layer],
        //   opacity: 0.75
        // });

        var map = new Map({
          basemap: 'streets-vector',
          ground: 'world-elevation',
          layers: [graphicsLayer, demographicGroupLayer]
        });

        var view = new MapView({
          map: map,
          center: [113.3, 23.4], // Longitude, latitude 
          zoom: 12, // Zoom level
          container: "viewDiv" // Div element
        });

        // provide('view', view); // 此处是为了让view能够跨组件通信，
        // 后代组件只需要通过 const view = inject('view')来获取到view，然后进行操作
        //开始监听鼠标移动事件（得到经纬度）
        view.on("click", function (e: any) {
          lon.value = Math.round(e.mapPoint.longitude * 1000) / 1000
          lat.value = Math.round(e.mapPoint.latitude * 1000) / 1000
        })

        async function defineActions(event: any) {
          const item = event.item;
          await item.layer.when();
          item.actionsSections = [
            [
              {
                title: "全局显示",
                className: "esri-icon-zoom-out-fixed",
                id: "full-extent"
              },
              {
                title: "图层信息",
                className: "esri-icon-description",
                id: "information"
              }
            ]
          ];
        }

        view.when(() => {
          layerList = new LayerList({
            view: view,
            container: "layersList",
            listItemCreatedFunction: defineActions
          });

          // 在view右上角添加sketch微件，用于绘制图形
          const sketch = new Sketch({
            layer: graphicsLayer,
            view: view,
            // graphic will be selected as soon as it is created
            creationMode: "update"
          });
          view.ui.add(sketch, "top-right");

          const legend = new Legend({
            view: view,
            layerInfos: [
              {
                layer: graphicsLayer,
                title: "Legend"
              }
            ]
          });

          view.ui.add(legend, "bottom-right");

          layerList.on("trigger-action", (event: any) => {
            const visibleLayer = USALayer.visible ? USALayer : censusLayer;
            console.log(visibleLayer)
            const id = event.action.id;
            if (id === "full-extent") {
              view.goTo(visibleLayer.fullExtent).catch((error: any) => {
                if (error.name != "AbortError") {
                  console.error(error);
                }
              });
            } else if (id === "information") {
              window.open(visibleLayer.url);
            }
          });

        })
        imap = map
        iview = view
      }
    )

    map_service = reactive(map_service)
    const mapservice = (value: IMapService) => {
      map_service.URL = value.URL
      map_service.type = value.type
      loadModules(modules, { css: true }).then(
        ([Map, WebMap, Locate, Track, TileLayer, MapView, Graphic,
          GraphicsLayer, FeatureLayer, PopupTemplate, SketchViewModel]) => {
          if (map_service.URL !== ' ') {
            let layer = null
            switch (map_service.type) {
              case "0":
                break;

              case "1":
                layer = new MapImageLayer({
                  url: map_service.URL,
                  id: (Date.now() + Math.random()).toString() + "_MapImage",
                  opacity: 0.9
                });
                imap.add(layer);
                break;

              case "2":
                layer = new TileLayer({
                  url: map_service.URL,
                  id: (Date.now() + Math.random()).toString() + "_Tile",
                  opacity: 0.5
                });
                imap.add(layer);
                break;

              case "3":
                layer = new VectorTileLayer({
                  url: map_service.URL,
                  id: (Date.now() + Math.random()).toString() + "_VectorTile"
                });
                break;

              case "4":
                layer = new ImageryLayer({
                  url: map_service.URL,
                  id: (Date.now() + Math.random()).toString() + "_Imagery"
                });
                imap.add(layer);
                break;

              case "5":
                layer = new ImageryTileLayer({
                  url: map_service.URL,
                  id: (Date.now() + Math.random()).toString() + "_ImageryTile",
                  opacity: 0.5
                });
                imap.add(layer);
                break;

              case "6":
                layer = new FeatureLayer({
                  url: map_service.URL,
                  id: (Date.now() + Math.random()).toString() + "_Feature",
                });
                imap.add(layer);
                break;

              case "7":
                layer = new KMLLayer({
                  url: map_service.URL,
                  id: (Date.now() + Math.random()).toString() + "_KML"
                });
                break;

              case "8":
                layer = new WMSLayer({
                  url: map_service.URL,
                  id: (Date.now() + Math.random()).toString() + "_WMS"
                });
                break;

              case "9":
                layer = new WFSLayer({
                  url: map_service.URL,
                  id: (Date.now() + Math.random()).toString() + "_WFS"
                });
                break;
            }
          }
        }
      )
    }
    provide("lon", lon)
    provide("lat", lat)

    const watch = watchEffect(() => {
      if (result.Image_URL !== " " && result.Feature_URL !== " ") {
        console.log(result)
        var image:string = result.Image_URL
        var feature:string = result.Feature_URL
        loadModules(modules, { css: true }).then(
          ([Map, WebMap, Locate, Track, TileLayer, MapView, Graphic,
            GraphicsLayer, FeatureLayer, PopupTemplate, SketchViewModel]) => {
            let image_layer = new TileLayer({
              url: image,
              id: (Date.now() + Math.random()).toString() + "_Tile",
              title: "开发变化图层",
              opacity: 0.5
            });
            imap.add(image_layer);
            let feature_layer = new FeatureLayer({
              url: feature,
              id: (Date.now() + Math.random()).toString() + "_Feature",
              title: "开发地区"
            });
            imap.add(feature_layer);
          })
        result.Image_URL = " "
        result.Feature_URL = " "
      }
    })

    return {
      mapservice,
      map_service,
    }
  },

});
</script>


s component only -->
<style scoped >
.mapView {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}

.toolbox {
  margin-top: -10px;
  margin-left: 25px;
  padding: 0;
  height: 35px;

}

#viewDiv {
  margin-top: -15px;
  margin-left: 1%;
  margin-right: -1%;
  width: 98%-5px;
  height: 76vh;
  border: 2px solid black;
}

.map_layers {
  width: 15%;
  border: 2px solid black;
  margin-bottom: -1.5%;
  background-color: #f2f2f2;
}

.footer {
  /* background-color: aquamarine; */
  background-color: rgb(255, 255, 255);
  height: 20px !important;
  margin-top: -5px;

}
</style>
