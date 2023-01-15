<!--侧边栏:相关设置-->
<template>
  <div class="set">
    <el-form ref="ruleFormRef" :model="form" :rules="rules" label-width="100px" class="demo-ruleForm" :size="formSize"
      status-icon>
      <div class="time">
        <el-form-item label="起始时间" required>
          <el-col :span="20">
            <el-form-item prop="date1">
              <el-date-picker v-model="form.dateStart" type="date" label="Pick a date" placeholder="Pick a date"
                format="YYYY/MM/DD" value-format="YYYY-MM-DD" style="width: 100%" />
            </el-form-item>
          </el-col>
        </el-form-item>
        <el-form-item label="终止时间" required>
          <el-col :span="20">
            <el-form-item prop="date2">
              <el-date-picker v-model="form.dateEnd" type="date" label="Pick a date" placeholder="Pick a date"
                format="YYYY/MM/DD" value-format="YYYY-MM-DD" style="width: 100%" />
            </el-form-item>
          </el-col>
        </el-form-item>
      </div>
      <!--算法选择-->
      <el-form-item label="算法" prop="algorithm" class="algorithm">
        <el-radio-group v-model="form.algorithm">
          <el-radio label="SVM" />
          <el-radio label="其它" disabled="true" />
        </el-radio-group>
      </el-form-item>

    </el-form>
    <!--是否确定-->
    <div class="buttonContain">
      <el-form-item>
        <el-button type="primary" @click="submitForm(ruleFormRef)"
          v-loading.fullscreen.lock="fullscreenLoading">确定</el-button>
        <el-dialog v-model="dialogVisible" title="Tips" width="30%" :before-close="handleClose">
          <span>时间选择错误，请重新选择！</span>
          <template #footer>
            <span class="dialog-footer">
              <el-button type="primary" @click="dialogVisible = false">确认</el-button>
            </span>
          </template>
        </el-dialog>
        <el-button class="reset" @click="resetForm(ruleFormRef)">重置</el-button>
      </el-form-item>
    </div>
  </div>

</template>
  
<script lang="ts">
import { defineComponent, reactive, ref } from 'vue';
import { ElMessageBox, FormInstance, FormRules, ElLoading } from 'element-plus'
import { apiSendTime } from '../apis/sendTime'

interface ITime_Return {
  Date_start: string;
  Date_end: string;
}

interface IResult_URL {
  Image_URL: string;
  Feature_URL: string;
}

export default defineComponent({
  name: 'DataChoice',
  components: {
    //HelloWorld,
  },
  setup(props, context) {
    const formSize = ref('default')
    const ruleFormRef = ref<FormInstance>()
    const form = reactive({
      dateStart: '',//起始日期
      dateEnd: '',//终止日期
      algorithm: '',//算法选择
    })

    //输入约束
    const rules = reactive<FormRules>({
      date1: [
        {
          type: 'date',
          required: false,
          message: 'Please pick a date',
          trigger: 'change',
        },
      ],
      date2: [
        {
          type: 'date',
          required: false,
          message: 'Please pick a date',
          trigger: 'change',
        },
      ],
      algorithm: [
        {
          required: true,
          message: 'Please select algorithm',
          trigger: 'change',
        },
      ],

    })
    //提交时
    const dialogVisible = ref(false)

    const fullscreenLoading = ref(false)

    const submitForm = async (formEl: FormInstance | undefined) => {
      if (!formEl) return
      await formEl.validate((valid, fields) => {
        if (valid) {
          console.log('提交成功！')
          var now_date = new Date().toISOString().slice(0, 10)
          if (form.dateStart >= form.dateEnd || form.dateEnd > now_date) {
            console.log("时间选择错误！")
            dialogVisible.value = true
          }
          else {
            const time: ITime_Return = {
              Date_start: form.dateStart,
              Date_end: form.dateEnd
            }

            const url: IResult_URL = {
              Image_URL: " ",
              Feature_URL: " "
            }


            apiSendTime(time).then((res: any) => {
              // console.log("传输成功！")
              // console.log(res)
              var test_url = JSON.parse(res)
              // console.log(url)
              url.Image_URL = test_url.Image_URL
              url.Feature_URL = test_url.Feature_URL
              console.log(url)
              context.emit("url", url)
            })

            // context.emit("time", [form.dateStart, form.dateEnd])
            context.emit("time", time)
            // context.emit("url", url)

            fullscreenLoading.value = true
            setTimeout(() => {
              fullscreenLoading.value = false
            }, 5000)

          }
        } else {
          console.log('error submit!', fields)
        }
      })
    }

    const resetForm = (formEl: FormInstance | undefined) => {
      if (!formEl) return
      formEl.resetFields()
    }

    const handleClose = (done: () => void) => {
      ElMessageBox.confirm('Are you sure to close this dialog?')
        .then(() => {
          done()
        })
        .catch(() => {
          // catch error
        })
    }

    return {
      form,
      ruleFormRef,
      rules,
      formSize,
      submitForm,
      resetForm,
      dialogVisible,
      handleClose,
      fullscreenLoading,
      // openFullScreen1
    }
  }
});
</script>

<style scoped>
.set {
  display: flex;
  width: 100%;
  padding-top: 20px;
  flex-wrap: wrap;
}

.time {
  margin: 5px 5px 5px 5px;
  width: 100%-10px;
}

.block {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  flex: 1;
}

.buttonContain {
  padding-top: 30px;
  padding-left: 30px;
}

.reset {
  margin-left: 45px;
}

.algorithm {
  width: 20px;
}
</style>