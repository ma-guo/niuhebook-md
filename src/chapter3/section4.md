## niuhe 接入 MCP,  让 API 文档也智能
API 文档的未来：`MCP`，让协作像聊天一样简单. `MCP` 是 `Model Context Protocol`(模型上下文协议)的缩写，是 2024 年 11 月 Claude 的公司 Anthropic 推出并开源的一个新标准。简单来说， 它就是让 AI 助手能够连接到各种第三方数据源的桥梁 ，包括你的内容库、业务工具和开发环境等等。说白了，就是让 AI 变得更聪明、回答更准确的一种方式！

利用 `apifox-mcp-server` 将在线文档、`Swagger/OpenAPI` 文件提供给 AI 使用, 从而让 AI 智能体能够更好地理解和使用你的 API, 从而提高工作效率。


`niuhe` 插件生成的 `swagger.json` 文档，能够完美借助 `apifox-mcp-server` 实现 `MCP` 功能。这意味着开发者可以轻松让 AI 智能体更深入、精准地理解和运用 API，大幅提升工作效率，让 API 开发与协作变得更加顺畅高效。

<video controls>
  <source src="https://img.footprint.gyzuxing.com/video/202503191817472.mp4" type="video/mp4">
  你的浏览器不支持视频播放。
</video>

## 配置 MCP 客户端
### 前置条件
- 已安装 `Node.js` 环境（版本号 >= 18，推荐最新的 LTS 版本）
- 任意一个支持 `MCP` 的 IDE：
    - `Cursor`
    - `VSCode + Cline` 插件
    - 其它
### 基本步骤
1. 确保你有 `docs/swagger.json` 本地路径或 url 地址

2. 在 IDE 中配置 `MCP`

将下面 JSON 配置添加到 IDE 对应的 `macOS/Linux` `MCP` 配置文件如下：
```json
{
  "mcpServers": {
    "API 文档": {
      "command": "npx",
      "args": [
        "-y",
        "apifox-mcp-server@latest",
        "--oas=<oas-url-or-path>"
      ]
    }
  }
}
```
windows MCP 配置文件如下：
```json
{
  "mcpServers": {
    "API 文档": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "apifox-mcp-server@latest",
        "--oas=http://{your domain}/api/hello/docs/"
      ]
    }
  }
}
```
> 其中 `<oas-url-or-path>` 可以是:
> - 远程 URL，如：`http://{your domain}/api/hello/docs/`
> - 本地文件路径，如：`~/Projects/docs/swagger.json`

通过上述操作，你就可以在 IDE 中使用 MCP 连接到你的 API 文档了。如有其他疑问，请查阅下列参考链接或[加官方支持群](../chapter6/section2.md)  咨询。

## 参考链接
- [Apifox MCP Server](https://docs.apifox.com/apifox-mcp-server)
- [通过 MCP 使用 OpenAPI/Swagger 文档](https://docs.apifox.com/6327891m0)
- [生成 Swagger 文档](./section2.md)
- [Model Context Protocol](https://modelcontextprotocol.io/introduction)