<!--主体-->
<template>
  <div class="monitor">
    <el-container class="low">
        <el-aside class="choice">
          <!-- <Choice @time="time_return" @url="url"></Choice> -->
          <Choice @url="url"></Choice>
        </el-aside>
        <el-main class="map_fill"><Map></Map></el-main>
      </el-container>
  </div>
</template>


<script lang="ts">
import { defineComponent, reactive, provide } from 'vue';
import Choice from '@/components/Choice.vue';
import Map from '@/components/Map.vue';
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
  name: 'Main',
  components: {
    Choice,
    Map
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
      time = value
      // console.log(time)
      // console.log(Date.now().toString())

      // result_URL.Image_URL = '1'
      // result_URL.Feature_URL = '2'
      // apiGetURL(time).then((res) => {
      //   console.log(res)
      // })
      // apiGetURL().then((res:any) => {
      //   var url=JSON.parse(res)
      //   console.log(url)
      //   result_URL.Image_URL=url.Image_URL
      //   result_URL.Feature_URL=url.Feature_URL
      //   console.log(result_URL)
      // }
      // )
    }

    const url = (value: IResult_URL) => {
      result_URL.Image_URL = value.Image_URL
      result_URL.Feature_URL = value.Feature_URL
      console.log(result_URL)
      // )
    }

    provide("result_URL", result_URL)

    return {
      time_return,
      url,
      time
    }
  }

  
   
});
</script>


s component only -->
<style scoped >
.monitor{
  width:100%;
}
.map_fill {
  width: auto;
  height: auto;
  border: 0.5px solid black;
}

.choice {
  width: 15%;
  border: 0.5px solid black;
}
</style>
