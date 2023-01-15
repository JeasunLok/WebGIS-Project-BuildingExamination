<template>
    <div class="layout">
      <el-tabs type="border-card">
        <el-tab-pane label="登录">
          <el-form
            label-position="right"
            label-width="60px"
            style="max-width: 460px"
            class="loginForm"
          >
            <el-form-item label="邮箱：">
              <el-input v-model="Email" />
            </el-form-item>
            <el-form-item label="密码：">
              <el-input type="password" v-model="password" />
            </el-form-item>
            <!--不同意无法登录-->
             <el-checkbox
                class="checkBox"
                v-model="isAgree"
                label="同意用户使用准则"
                name="type"
              />
              <br/>

            <el-button
              v-if="isAgree"
              type="primary"
              class="loginBtn"
              @click="login"
            >
              登录
            </el-button>
          </el-form>
        </el-tab-pane>
  
        <el-tab-pane label="注册">
          <el-form
            label-position="right"
            label-width="100px"
            style="max-width: 460px"
            class="loginForm"
          >
            <el-form-item label="邮箱：">
              <el-input v-model="rEmail" />
            </el-form-item>
            <el-form-item label="密码：">
              <el-input type="password" v-model="rPassword" />
            </el-form-item>
            <el-form-item label="确认密码：">
              <el-input
                type="password"
                v-model="confirmPassword"
                @blur="confirmFunc"
              />
            </el-form-item>
            <!--不同意无法注册-->
            <el-checkbox
                class="checkBox"
                v-model="rAgree"
                label="同意用户使用准则"
                name="type"
              />
              <br/>
  
            <el-button
              v-if="rAgree"
              type="primary"
              class="loginBtn"
              @click="register"
            >
              注册
            </el-button>
          </el-form>
        </el-tab-pane>
      </el-tabs>
    </div>
  </template>
  <script lang="ts">
  import { reactive, toRefs } from "vue";
  import { ElMessage } from "element-plus";
  export default {
    setup() {
      const form = reactive({
        Email: "",
        password: "",
        isAgree: 0,
      });
      const registerForm = reactive({
        rEmail: "",
        rPassword: "",
        confirmPassword: "",
        identifyCode: "",
        rAgree: 0,
      });
  
      // 方法
      // 登录
      function login() {
        console.log(form);
        //这里应该有与后端数据的交互，只作测试
        //符合则跳转，不符合则弹出消息（如：ElMessage.error("无用户信息.");）
      }
      // 注册
      function register() {
        console.log("注册", registerForm);
        //应该将数据读入数据库
      }
      // 确认密码
      const confirmFunc = () => {
        if (registerForm.confirmPassword !== registerForm.rPassword)
          ElMessage.error("密码与确认密码不一致.");
      };
      return {
        ...toRefs(form),
        ...toRefs(registerForm),
        login,
        register,
        confirmFunc,
      };
    },
  };
  </script>
  
  <style scoped>
  .layout {
    position: absolute;
    left: calc(50% - 200px);
    top: 20%;
    width: 400px;
  }
  .loginBtn {
    width: 100px;
  }
  .loginForm {
    text-align: center;
  }
  .checkBox {
    margin-left: 7px;
  }
  .inpWidth {
    width: 165px;
  }
  </style>
