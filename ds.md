# Niuhe 插件使用指南

---

## 第一部分：介绍
### 什么是 IDL？
接口定义语言（IDL）是用于描述服务接口、数据结构及通信协议的核心工具。在分布式系统开发中，IDL 可以实现**"一次定义，跨语言使用"**的愿景，避免前后端、多语言模块间的重复定义工作。

Niuhe 插件通过 `niuhe` IDL 语法的支持和拓展，支持如下功能：
- 自动生成 Golang 路由代码, 结构化路由定义
- 生成 TypeScript 类型定义
- 生成 Swagger2.0 接口文档
- 数据库模型生成（XORM）
- 多语言协议支持（Kotlin 等）
- 快速接入 Vue3-Element-Admin 前端框架

IDL "一生万物"的特性，让开发者在一次定义后，就能自动获得完整的前后端代码、接口文档和数据库模型，避免多次重复定义的繁琐工作。提升开发效率 300% 以上。

---

## 第二部分：Get Start
### 1. 安装与激活
1. VSCode 插件市场搜索 `niuhe`
2. 点击安装后，资源管理器顶部出现 `</>` 图标[3](@ref)
3. 或快捷键 `Command + Shift + P` 输入 `niuhe idl` 激活

### 2. Hello World 实战
在项目根目录创建：
```python
#app=demo

class HelloReq():
    '''测试请求'''
    name = required.String(desc='用户名')

class HelloResp(Message):
   '''测试响应'''
    greeting = required.String(desc='问候语')

with services():
    GET('示例接口', '/api/hello/world/', HelloReq, HelloResp)
```

点击 `</>` 生成代码后，将自动创建如下文件：
```tree
.
├── README.md // 项目说明
├── conf
│   └── demo.yaml // 配置文件
├── makefile // linux/unix makefile 脚本
├── niuhe
│   └── all.niuhe // 项目入口文件
├── niuhe.log
└── src
    └── demo
        ├── app
        │   ├── api
        │   │   ├── protos
        │   │   │   └── gen_protos.go // 自定生成的 go 请求和响应结构定义文件
        │   │   └── views
        │   │       ├── gen_hello_views.go // 自定义生成的 go 路由处理器文件
        │   │       ├── hello_views.go // hello 香港 view 的实现文件
        │   │       └── init.go
        │   └── common
        │       └── consts
        │           └── gen_consts.go // 常量定义文件
        ├── config
        │   └── config.go // 配置文件定义, 读取 conf/demo.yaml 内容
        ├── go.mod
        ├── main.go // 项目入口
        └── xorm
            ├── daos
            │   └── init.go // dao 层基本定义定义
            ├── models
            │   └── models.go // model 层定义示例
            └── services
                └── init.go // service 层基本定义
```
接下来我们跟随 README.md 指引，执行下列命令运行项目
```sh
cd src/demo && go mod init demo && go mod tidy && go mod vendor && cd ../../ && make run
```
此时我们在浏览器访问链接: http://localhost:19999/api/hello/world/, 即可看到返回的问候语。
```json
{"message":"Name（必填）","result":-1}
```
由此我们完成了一个简单的 `Hello World` 示例。

Golang 路由处理器
TypeScript 类型定义
Swagger 文档骨架
3. 核心语法速览
语法元素	示例	功能
项目定义	#app=project	定义项目根命名空间
结构体	class User(Message):	生成跨语言数据结构
接口定义	POST(...)	生成路由和接口文档
常量组	class Status(ConstGroup):	生成枚举常量
第三部分：入门
1. Swagger 文档生成
在 all.niuhe 添加：

python
#langs=docs
生成 swagger.json 后，可通过两种方式使用：

​Apifox 导入：直接拖拽文件到 Apifox 接口管理平台
​API 自描述：集成到 Golang 项目的 /swagger 端点
2. TypeScript 集成
配置生成路径：

python
#ts_path=src/api/types.ts
生成的类型定义可直接用于 Axios 请求：

typescript
interface SysTestReq {
    say: string;
}
// 自动生成 API 请求函数
export function getSysTest(params: SysTestReq) {
    return request.get('/api/sys/test', {params})
}
第四部分：进阶操作
1. XORM 代码生成
定义数据库模型：

python
# xorm/user.niuhe
class User(Model):
    id = Int(pk=True)
    name = String(50)
生成 Go 结构体：

go
// gen_xorm.go
type User struct {
    Id   int64  `xorm:"pk autoincr"`
    Name string `xorm:"varchar(50)"`
}
2. 多语言支持
生成 Kotlin 协议：

python
#langs=kotlin
#kotlin_package=com.demo.protocol
将生成：

数据类（Data Class）
序列化注解
接口请求模板
3. Vue3 快速接入
在 vue3-element-admin 项目中：

复制生成的 api/types.ts 到 src/api
配置 axios 基础路径
直接调用自动生成的 API 函数
第五部分：FAQ
1. 生成失败排查
现象	解决方案
未识别 .niuhe 文件	检查文件语法高亮是否为 Python 模式
Swagger 文档缺失	确认 #langs 包含 docs
2. 高频问题
​时间类型处理：使用 datetime 字段类型自动转换时区
​嵌套结构：通过 include('common.niuhe') 引入共享定义
3. 加群交流
遇到复杂问题？立即加入技术交流群：
QQ群：12345
https://via.placeholder.com/150x150

第六部分：致谢
本插件基于以下杰出开源项目构建：

niuhe：Golang 代码生成核心引擎
zpform：表单验证与协议转换神器
youlaitech：前端框架集成解决方案
特别感谢 @思无邪2100 等贡献者的持续优化，欢迎通过 GitHub Sponsor 支持开源事业。您的每一份捐赠都是我们前进的动力！

联系我们：niuhe@example.com | 微信: niuhe_dev