## 2. Hello World 实战
> 本教程代码库为 [niuhe-mdbook](https://github.com/ma-guo/niuhe-mdbook)

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