Vscode niuhe 插件是一款面向 golang 的后端 IDL 定义翻译插件, 支持 go 程序的路由, 出入参定义；同时支持将 idl 翻译为 typescript 定义. 支持 xorm 代码生成, 其他语言协议生成等.

通过简明的 [niuhe 语法](chapter2/README.md), 定义 idl, 然后通过插件生成对应的代码, 提高开发效率.

## 支持的功能

| 功能 | 描述 |
| --- | --- |
| go | 支持 go 服务基本框架, 入参和出参, 文件和方法及路由 管理 |
| [ts](chapter3/section3.md) | 生成 小程序, web 前端 api 接口定义  |
| [docs](chapter3/section2.md) | 生成 swagger 文档, 支持 apifox, postman 等导入方便测试 |
| 其他语言 | 通过 protocol 生成json 格式完整协议, 自定义代码解析为其他语言 |

## go 服务支持的功能
| 功能 | 描述 |
| --- | --- |
| 路由 | 支持 go 服务的路由定义,文件名和方法即路由, 无需手动配置 |
| 参数管理 | 支持 go 服务的入参解析, 出参格式化, 只需关心具体逻辑实现, 无需关心参数解析 |
| [xorm](chapter4/section1.md) | 通过生成对应的 model,dao,service 文件, 支持生成基本的增删改查操作, 避免低效重复来动 |
| 常量定义 | 支持常量定义, 提高代码复用性 |

## 生态系统
开发配套的前后端管理系统模板库, 方便快速搭建企业级后台应用.

| 功能 | 描述 |
| --- | --- |
| [admin-core](chapter5/section1.md) | 提供后台管理核心功能, 包括用户管理、权限管理、菜单管理等, 通过简单配置即可
| [vue3-element-admin](chapter5/section4.md) | 基于 Vue3 和 Element Plus 的后台管理系统模板，开箱即用. 本插件支持生成对应的前端项目代码, 方便快速搭建企业级后台应用. |