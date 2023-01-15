<template>
    <div class="collapse navbar-collapse" id="collapsibleNavbar">
        <div class="left">
            <div class="esri-widget esri-widget--button esri-interactive ms-1" title="默认选择" id="defaultTool">
                <span class="esri-icon-cursor curTool"></span>
            </div>
        </div>

        <div class="left">
            <div class="esri-widget esri-widget--button esri-interactive ms-1" title="画点" id="drawPoint">
                <span class="esri-icon-map-pin"></span>
            </div>
        </div>

        <div class="left">
            <div class="esri-widget esri-widget--button esri-interactive ms-1" title="画折线" id="drawPolyline">
                <span class="esri-icon-polyline"></span>
            </div>
        </div>

        <div class="left">
            <div class="esri-widget esri-widget--button esri-interactive ms-1" title="画多边形" id="drawPolygon">
                <span class="esri-icon-polygon"></span>
            </div>
        </div>

        <div class="left">
            <div class="esri-widget esri-widget--button esri-interactive ms-1" title="画圆" id="drawCircle">
                <span class="esri-icon-radio-unchecked"></span>
            </div>
        </div>

        <div class="left">
            <div class="esri-widget esri-widget--button esri-interactive ms-1" title="画矩形" id="drawRectangle">
                <span class="esri-icon-checkbox-unchecked"></span>
            </div>
        </div>

        <div class="left">
            <div class="esri-widget esri-widget--button esri-interactive ms-1" title="清除图形" id="eraseGraphics">
                <span class="esri-icon-erase"></span>
            </div>
        </div>

        <div class="left">
            <div class="esri-widget esri-widget--button esri-interactive ms-1" title="点选" id="pointSelect">
                <span class="esri-icon-north-navigation"></span>
            </div>
        </div>

        <div class="left">
            <div class="esri-widget esri-widget--button esri-interactive ms-1" title="框选" id="rectangleSelect">
                <span class="esri-icon-cursor-marquee"></span>
            </div>
        </div>

        <div class="left">
            <div class="esri-widget esri-widget--button esri-interactive ms-1" title="识别要素" id="identifyFeature">
                <span class="esri-icon-notice-round"></span>
            </div>
        </div>

        <div class="left">
            <div class="esri-widget esri-widget--button esri-interactive ms-2" title="属性列表" id="listTable">
                <span class="esri-icon-table"></span>
            </div>
        </div>

        <div class="left">
            <div class="esri-widget esri-widget--button esri-interactive ms-1" title="唯一值渲染" id="unqiueValue">
                <span class="esri-icon-maps"></span>
            </div>
        </div>

        <div class="left">
            <div class="esri-widget esri-widget--button esri-interactive me-1" title="分级渲染" id="classBreak">
                <span class="esri-icon-media"></span>
            </div>
        </div>
    </div>
</template>


<script lang="ts">

import { defineComponent } from 'vue';
export default defineComponent({
    name: 'Toolbox',
    components: {

    },
    setup() {
        
    }
})

</script>

<style>
.left {
    float: left;
}
</style>