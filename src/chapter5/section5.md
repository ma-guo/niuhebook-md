## admin-core FAQ
admin-core 是一个基于 Vue3 + Element Plus 的后端管理系统模板，它提供了一套完整的后台解决方案。在使用过程中，可能会遇到一些常见问题。以下是一些常见问题的解答和解决方案。
### 首次登录密码问题
登录失败时会将请求的密码生成的加密字符串 log 出来，首次登录时将字符串替换到表中对应用户的密码字段即可。

### OSS 路径问题
admin-core 中添加了文件存储功能, 默认为本地存储，本地存储需要在配置文件中添加 host 字段, 当前 `conf/demo.yaml` 内容为:
```yaml
serveraddr: :19999
loglevel: INFO
db:
  showsql: false
  debug: true
  sync: true
  main: user:pwd@tcp(host:port)/database_name?charset=utf8mb4
secretkey: 123456
host: http://localhost:19999
```
### 自定义协议处理
本插件生成的入参和出参处理定义在 [niuhe](https://github.com/ma-guo/niuhe/blob/master/protocol.go) 库中, 具体代码为:
```go

type IApiProtocol interface {
	Read(*Context, reflect.Value) error
	Write(*Context, reflect.Value, error) error
}

type DefaultApiProtocol struct{}

func (self DefaultApiProtocol) Read(c *Context, reqValue reflect.Value) error {
	if err := zpform.ReadReflectedStructForm(c.Request, reqValue); err != nil {
		return NewCommError(-1, err.Error())
	}
	return nil
}

func (self DefaultApiProtocol) Write(c *Context, rsp reflect.Value, err error) error {
	rspInst := rsp.Interface()
	if _, ok := rspInst.(isCustomRoot); ok {
		c.JSON(200, rspInst)
	} else {
		var response map[string]interface{}
		if err != nil {
			if commErr, ok := err.(ICommError); ok {
				response = map[string]interface{}{
					"result":  commErr.GetCode(),
					"message": commErr.GetMessage(),
				}
				if commErr.GetCode() == 0 {
					response["data"] = rsp.Interface()
				}
			} else {
				response = map[string]interface{}{
					"result":  -1,
					"message": err.Error(),
				}
			}
		} else {
			response = map[string]interface{}{
				"result": 0,
				"data":   rspInst,
			}
		}
		c.JSON(200, response)
	}
	return nil
}
```
如果需要自行实现为其他协议, 可以参考上述代码进行自定义实现。
### 总结
通过以上步骤，您可以将 [admin-core](https://github.com/ma-guo/admin-core) 引入到您的项目中，并根据实际需求进行定制化开发。希望这些信息对您有所帮助！
