<!--图层选项-->
<template>
    <div class="footer_coordinate">
        <b class="coordinate_text">坐标值:[{{ x }},{{ y }}]</b>
    </div>
</template>

<script lang="ts">

import { defineComponent, inject } from 'vue';
const modules = ["esri/Map", 'esri/WebMap', "esri/widgets/Locate",
    "esri/widgets/Track", "esri/layers/TileLayer", 'esri/views/MapView', "esri/Graphic",
    "esri/layers/GraphicsLayer", "esri/layers/FeatureLayer",
    "esri/PopupTemplate", "esri/widgets/Sketch"]

export default defineComponent({
    name: 'Footer',
    components: {
    },
    setup() {
        let x:any = inject("lon")
        let y:any = inject("lat")

        return {
            x,
            y
        }
    }
})
</script>

<style>
.footer_coordinate {
    /* margin-top: 5px; */
    height: 35px;
    float: right;
}
.coordinate_text{
    font-size: 20px;
}
</style>