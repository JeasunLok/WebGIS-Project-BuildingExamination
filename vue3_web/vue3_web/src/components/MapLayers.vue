<!--图层选项-->
<template>
    <link rel="stylesheet" href="https://darun.gd.cn/arcgis/4.23/esri/themes/light/main.css">
    <div class="maplayer_label">
        <h3 class="layer_text">图层</h3>
    </div>
    <div class="load_map">
        <el-button @click="mapservice_dialogFormVisible = true" type="primary">加载地图服务</el-button>
        <el-dialog v-model="mapservice_dialogFormVisible" title="加载地图服务">
            <el-form :model="mapservice_form">
                <el-form-item label="地图服务资源URL" :label-width="140">
                    <el-input v-model="mapservice_form.URL" autocomplete="off" />
                </el-form-item>
                <el-form-item label="地图服务类型" :label-width="140">
                    <el-select v-model="mapservice_form.type" placeholder="请选择一种地图服务类型">
                        <el-option label="MapImageLayer" value="1" />
                        <el-option label="TileLayer" value="2" />
                        <el-option label="VectorTileLayer" value="3" />
                        <el-option label="ImageryLayer" value="4" />
                        <el-option label="ImageryTileLayer" value="5" />
                        <el-option label="FeatureLayer" value="6" />
                        <el-option label="KMLLayer" value="7" />
                        <el-option label="WMSLayer" value="8" />
                        <el-option label="WFSLayer" value="9" />
                    </el-select>
                </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="mapservice_dialogFormVisible = false">取消</el-button>
                    <el-button type="primary" @click="mapservice_dialogFormVisible = false;mapservice()">确认</el-button>
                </span>
            </template>
        </el-dialog>
    </div>
    <div class="tab-pane fade" id="layersDiv" role="tabpanel" aria-labelledby="layers-tab">
        <div class="scroll-vectical" id="layersList">
        </div>
    </div>
</template>


<script lang="ts">

import LayerList from "@arcgis/core/widgets/LayerList";
import { defineComponent, ref, reactive } from 'vue';

export default defineComponent({
    emits: ["mapservice"],
    name: 'MayLayers',
    components: {

    },
    setup(props, context) {
        const mapservice_dialogFormVisible = ref(false)
        const mapservice_form = reactive({
            URL: '',
            type: '',
        })
        const mapservice = () => {
            context.emit("mapservice",mapservice_form)
        }
        return {
            mapservice_dialogFormVisible,
            mapservice_form,
            mapservice
        }
        
    }
    
})

</script>

<style>
.maplayer_label {
    padding: 0;
    margin-top: -5px;
    text-align: center;
}

.layer_text {
    font-size: 20px;
}

.load_map {
    text-align: center;
    margin-bottom: 15px;
}
</style>