const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  devServer: {
    port: 8000, // 启动端口号
    open: false // 启动后是否自动打开网页
  }
})
