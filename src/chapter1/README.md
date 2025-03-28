[Vscode niuhe](https://marketplace.visualstudio.com/items?itemName=dequan.niuhe) 插件是一款面向 golang 的后端 IDL 定义翻译插件, 旨在简化后端开发流程, 提高开发效率. 它可以通过简单的 [niuhe idl 语法](../chapter2/section3.md) 定义接口, 生成对应的 go 服务代码, 前端 api 定义, swagger 文档, 以及其他语言的协议定义. 让开发人员专注于业务逻辑, 而不是繁琐的代码生成工作.

## 核心功能

| 功能模块 | 核心能力 | 适用场景 |
| --- | --- | --- |
| Go语言支持 | 自动生成服务框架代码：包含路由配置、请求参数解析、响应格式处理等基础代码 | 后端开发 |
| [TypeScript支持](../chapter3/section3.md) | 一键生成前端API调用代码，支持Web/小程序/React Native等场景 | 前端开发 |
| [文档生成](../chapter3/section2.md) | 自动生成Swagger文档，支持导入Postman/Apifox等测试工具, [接入 MCP](../chapter3/section4.md) 等 | 接口测试 |
| [多语言协议](../chapter4/section2.md) | 生成标准化协议文件，支持自定义转换到其他编程语言 | 跨语言协作 |

## Go服务核心特性
| 功能 | 优势 |
| --- | --- |
| 智能路由 | 自动根据文件结构生成路由配置，无需手动维护 |
| 参数处理 | 内置请求参数校验和响应格式化，专注业务逻辑开发 |
| [XORM集成](../chapter4/section1.md) | 自动生成数据库操作代码（表结构定义、DAO层、服务层） |
| 常量管理 | 统一管理业务常量，提升代码可维护性 |

## 配套解决方案
开提供开箱即用的管理系统模板，加速企业级应用开发：

| 解决方案 | 亮点 |
| --- | --- |
| [Admin-Core](../chapter5/section1.md) | 内置RBAC权限体系，快速实现用户/角色/菜单管理 |
| [Vue3管理模板](../chapter5/section4.md) | 基于流行技术栈（Vue3+Element Plus），提供完整后台功能组件 |

## 实践案例
- [admin-core-niuhe](https://github.com/ma-guo/admin-core-niuhe) 完整示例项目（后端）
- [admin-core-test](https://github.com/ma-guo/admin-core-test) 前端框架接入示例 
- [在线演示](http://admindemo.zuxing.net) Vue3管理后台演示（账号: admin / 123456）

