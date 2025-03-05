## Hello World
在[第二部分第二节](../chapter2/section2.md)种们通过定义 `niuhe/all.niuhe` 实现了一个简单的 `Hello World` 示例。本节我们将介绍如何实现它。
我们将 `src/demo/app/api/views/hello_views.go` 中 `World_GET` 方法修改为如下:
```go
func (v *Hello) World_GET(c *niuhe.Context, req *protos.HelloReq, rsp *protos.HelloRsp) error {
	rsp.Greeting = "Hello World " + req.Name
	return nil
}
```
重新运行程序并访问如下链接 `http://localhost:9999/api/hello/world/?name=Tom`，即可看到返回的问候语。
```json
{
  "data": {
    "greeting": "Hello World Tom"
  },
  "result": 0
}
```
这里 `github.com/ma-guo/niuhe` 包提供了一些基础的功能，如上下文管理、请求参数解析等和返回结构包装。我们只关心具体业务逻辑即可。