## 语法介绍
`niuhe` 语法主要包括注释,常量(枚举), 数据类型(class/struct), 接口定义(路由), 数据成员定义五个部分。
idl 语法大致与 python 相通, 插件自定义了 `niuhe` 后缀的语法高亮和自动补全，也可选择 python 来做语法高亮

### 应用名称
应用名称需定义在入口文件(all.niuhe)最开始，使用 `#app=应用名` 来定义。
```python
#app=demo
```

### 注释
注释同 `python` 相同, 单行注释使用 `#`, 多行注释使用三个引号 `'''`, 类和常量的说明用注释的方式写在类定义的下一行。

### 常量(枚举)
```python
class Language(ConstGroup):
    '''语言枚举类'''
    ZH = Item("zh", "中文")
    EN = Item("en", "英文")

class LanguageType(ConstGroup):
    '''语言类型枚举'''
    ZH_CN = Item(1, "简体中文")
    ZH_TW = Item(2, "繁体中文")
```
常量定义以 `class` 开头, 继承 `ConstGroup`, 内部通过 `Item` 来定义具体的常量值。常量仅支持 `String` 和 `Integer` 类型，且必须指定一个唯一标识符和一个显示名称。上述定义生成后的代码(`src/demo/app/common/consts/gen_consts.go`)为
```go
package consts

// Generated by niuhe.idl

import "github.com/ma-guo/niuhe"

var Language struct {
	*niuhe.StringConstGroup
	ZH niuhe.StringConstItem `name:"中文" value:"zh"` // value: zh, name: 中文
	EN niuhe.StringConstItem `name:"英文" value:"en"` // value: en, name: 英文
}

// 语言类型枚举
var LanguageType struct {
	*niuhe.IntConstGroup
	ZH_CN niuhe.IntConstItem `name:"简体中文" value:"1"` // value: 1, name: 简体中文
	ZH_TW niuhe.IntConstItem `name:"繁体中文" value:"2"` // value: 2, name: 繁体中文
}

func init() {
	niuhe.InitConstGroup(&Language)
	niuhe.InitIntConstGroup(&LanguageType)
}
```
### 数据类型(class/struct)
在上一节的 hello world 示例中，我们定义了一个简单的 接口的入参和出参类
```python
class HelloReq():
    '''测试请求'''
    name = required.String(desc='用户名')

class HelloRsp(Message):
   '''测试响应'''
    greeting = required.String(desc='问候语')
```
数据类型定义以 `class` 开头, 继承 `Message`, `Message` 可不写, 类后跟随以注释形式的类说明(可选)和成员定义。
当类无成员时以 `pass` 做标记即可，可如下:
```python
class HelloReq():
    '''测试请求, 无参数'''
    pass
```
上述定义生成的 `struct` 代码为:
```go
package protos

// Generated by niuhe.idl
// 此文件由 niuhe.idl 自动生成, 请勿手动修改

// 测试请求
type HelloReq struct {
	Name string `json:"name" zpf_name:"name" zpf_reqd:"true"` //	用户名
}

// 测试响应
type HelloRsp struct {
	Greeting string `json:"greeting" zpf_name:"greeting" zpf_reqd:"true"` //	问候语
}
```
#### 类的继承
类继承自`Message`可以继承自自定义的其他类, 通过在类名后添加括号的方式实现:
```python
class NihaoReq(HelloReq):
    '''你好请求'''
    mingzi = required.String(desc='名字')

```
生成的 struct 代码为:
```go
// 你好请求
type NihaoReq struct {
	Name   string `json:"name" zpf_name:"name" zpf_reqd:"true"`     //	用户名
	Mingzi string `json:"mingzi" zpf_name:"mingzi" zpf_reqd:"true"` //	名字
}
```
### 成员定义
成员定于语法为:
```python
  member_name  = label.type(desc='', cls=..., group=...)
```
其中 
- `label` 可以是 `required`(必填的), `optional`(可选的), `repeated`(重复的/数组),
- `type` 可以是  `Integer`, `Decimal`, `Float`, `Long`, `String`, `Boolean`, `Message`, `Enum`,`StringEnum`, `File`, `Any` 11种数据类型。
- `desc`: 描述信息, 可选, 建议填写成员字段说明, 否则失去文档定义语言意义。
- `group`: 指定 `enum` 的 `group`, 仅当 `type` 为 `Enum` 和 `StringEnum` 时有效和必填, 如 `lang=required.Enum(desc='语言枚举', houp=LanguageType)`
- `cls`: 指定类的类型，仅当 `type` 为 `Enum` 和 `StringEnum` 时有效和必填，如 `message=optional.Message(desc='消息体',cls=HelloReq)`
这里 `required` 和 `optional` 仅对入参有意义, 出参在 `go` 中无此限制。 `repeated` 在入参中同`optional`

### 接口定义(路由)
接口定义以 `with services(): ` 为开始标记, 后面跟随一个或多个路由定义，每个路由定义如下:
```go
http_method('接口说明', 'api_path(/mode/view/method/)', 入参类名（可选), 出参类名(可选))
```
其中 
- `http_method` 可以是 `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, `OPTIONS` 等 http method
- `接口说明`: 接口的简要描述, 如 `'获取用户信息'`
- `api_path`: 必须是三段式 api 的路径, 如 `/api/hello/world/`
- `入参类名`: 可选, 如 `HelloReq` 当不填写时，得自己处理入参和出参的解析, 入参和出参得同时可选或同时必填。
- `出参类名`: 可选, 如 `HelloRsp` 当不填写时，得自己处理入参和出参的解析, 入参和出参得同时可选或同时必填。
本章节第二小节定义的路由如下:
```python
with services():
    GET('示例接口', '/api/hello/world/', NihaoReq, HelloRsp)
```
生成的代码在 `src/demo/app/api/views/[gen_]hello_views.go` 文件中。
### RPC 方式定义接口
在定义接口时，可以通过 `RPC` 关键字来定义一个接口。语法如下:
```python
RPC('接口说明', [http_method/url=]'api_path(/mode/view/method/)')[].args(...)][.returns(...)][.codes(...)]
```
其中:
- `http_method/url=`: 可选，指定 http 方法和路径，如 `get='/api/hello/world/'`, `url='/api/hello/world/'` 或者直接写 `'/api/hello/world/'`, 此时 `http_method` 为 `GET` 和 `POST`
- `.args(...)`: 可选，指定接口的入参，如 `.args(name=required.String(desc='用户名'),...)`
- `.returns(...)`: 可选，指定接口的出参，如 `.returns(greeting=required.String(desc='问候语'),...)`
- `.codes(...)`: 可选，指定接口的状态码和描述, 可用于约束 api 可返回的错误状态码范围，如 `.codes(LanguageType.ZH_CN, LanguageType.ZH_TW)`, `codes` 中为定义的 `Integer` 枚举值
> `RPC` 方式同 `GET`, `POST` 的差异是不用直接定义一个 `class`, 在一个文件中定义过多 `class` 时不便于一目了然地查阅接口的入参和出参。
>
>同时 `RPC` 方式支持只定义入参和出参的情况, 此时会生成一个空结构来填补另一个未定义的参数结构
### include 其他文件
在定义类时，可以通过 `include` 关键字引入其他文件中的类.
如在 comm.niuhe 文件中定义了如下内容:
```python
# 公共类型定义

class NoneResp():
    '''空响应'''
    pass

class NoneReq():
    '''空请求'''
    pass
```
此时可在 all.niuhe 文件中通过 include 引入:
```python
include('comm.niuhe')
# 然后通过 comm.NoneReq, comm.NoneResp 来使用这些类
```

### 其他说明
入参参数中, 并不支持解析复杂结构, 如 `Message`, `Any`, `Dict` 等. 而出参则无此限制, 可以自由定义返回的 `json` 数据格式。
