## 生成 Swagger 文档
`Swagger` 文档是一种以特定格式（如 `JSON` 或 `YAML`）编写的文件，用于对 RESTful API 进行详细的描述和说明。它提供了一种标准化的方式来定义 API 的端点、请求和响应的结构、参数、身份验证机制等信息，使得开发人员、测试人员、文档编写者以及其他相关人员能够全面了解 API 的功能和使用方法，从而更高效地进行开发、集成和测试等工作。

在 `niuhe/.config.json5` 文件 `langs` 配置中添加 `docs` 即可在生成文件时生成协议的 `swagger` 文档。
生成的文档位于 `docs/swagger.json`, 同时生成了 `niuhe/.docs.json5` 自定义文件, 可在自定义文件中定制输出内容。

生成的 `docs/swagger.json` 文件可直接导入到 [apifox](https://apifox.com/) 等支持 `Swagger` 协议的测试工具中进行测试和使用。也可读取 `niuhe/.docs.json5` 生成 url 输出到网页上, 具体配置如下:
### 示例
假设我们有一个简单的 API，包含以下内容：
```python
with services():
    GET('示例接口', '/api/hello/world/', HelloReq, HelloRsp)
    GET('协议文档', '/api/hello/docs/')
```
通过如下代码即可将协议文档输出到网页上：[http://localhost:9999/api/hello/docs/](http://localhost:9999/api/hello/docs/)
```go
// 协议文档
func (v *Hello) Docs_GET(c *niuhe.Context) {
	docs, err := os.ReadFile("./docs/swagger.json")
	if err != nil {
		niuhe.LogError("read docs file failed: %v", err)
		return
	}
	data := make(map[string]any)
	json.Unmarshal(docs, &data)
	c.JSON(http.StatusOK, data)
}
```