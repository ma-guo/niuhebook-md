## vue3-element-admin 项目搭建指南
### 简介
[vue3-element-admin](https://github.com/ma-guo/vue3-element-admin) 是基于 Vue3 + Vite5+ TypeScript5 + Element-Plus + Pinia 等主流技术栈构建的免费开源的后台管理前端模板（配套后端源码 [admin-core](https://github.com/ma-guo/admin-core)）

### 项目启动
```sh
# 克隆代码
git clone https://github.com/ma-guo/vue3-element-admin.git

# 切换目录
cd vue3-element-admin

# 安装 pnpm
npm install pnpm -g

# 安装依赖
pnpm install

# 启动运行
pnpm run dev
```

### 生成新页面代码
在 `niuhe/.config.json5` 配置项 `langs` 中添加 `vite`, 结合 `niuhe/.model.niuhe` 配置, 在生成代码时会在 `vite` 目录下生成对应的 `vue` 文件。 将生成的文件内容复制到对应的 vue 文件中即可