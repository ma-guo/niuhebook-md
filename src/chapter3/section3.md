## 生成 typescript api 定义
在开发前端应用时，通常需要根据后端的 API 接口定义来生成相应的 TypeScript 类型。niuhe 插件提供了便捷的方式来自动生成这些类型定义文件。以下是如何生成 TypeScript API 定义的步骤：
### 1. 添加 `ts` 语言支持
首先，在 `docs/.config.json5` 的 `langs` 中添加 `ts`。生成代码后会生成如下几个文件:
```tree
typings
├── api.ts - API 接口类型定义
├── event.d.ts - 部分公共属性定义
├── request.ts - 请求方法封装
└── types.d.ts - niuhe 中定义的类型定义
```
### 2. 自定义文件存储路径
上述生成的四个文件中 `event.d.ts` 和 `request.ts` 和 内容是不会变的, 将其复制到目标位置即可。`api.ts` 和 `types.d.ts` 需要根据实际情况进行调整。因此在 `docs/.config.json5` 中添加 `tstypes` 和 `tsapi` 两个配置项，分别指定文件存储路径。这两个文件的路径建议为绝对路径。 如配置项所言，可配置多个路径，同时生成多份文件。
