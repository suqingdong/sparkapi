# SparkDesk API and Client
> https://www.xfyun.cn/doc/spark/Web.html

***接口说明***
注意： 该接口可以正式使用。如您需要申请使用，请点击前往[产品页面 ](https://xinghuo.xfyun.cn/sparkapi?scr=price)

计费说明：
| 服务引擎               | 单价              |
|--------------------|-----------------|
| 讯飞星火认知大模型V1.5 | 0.18元/万tokens   |
| 讯飞星火认知大模型V2.0 | 0.36元/万tokens   |
| 讯飞星火认知大模型V3.0 | 0.36元/万tokens   |

## Installation
```bash
python3 -m pip install -U sparkapi-python
```

## Configuration
> copy `example.env` to `~/.sparkapi.env` and edit the file with your credentials.
```
SPARK_APP_ID=<your-app-id>
SPARK_API_SECRET=<your-api-secret>
SPARK_API_KEY=<your-api-key>
SPARK_API_MODEL='v3.0'          # v1.5, v2.0, v3.0
SPARK_CHAT_MAX_TOKENS=4096      # v1.5: 1-4096, v2.0: 1-8192
SPARK_CHAT_TEMPERATURE=0.5      # 0-1
SPARK_CHAT_TOP_K=4              # 1-6
```

## Quickstart

### CommandLine
```bash
sparkapi --help

# start a chat session
sparkapi chat
```
![](https://suqingdong.github.io/sparkapi/src/cmd_chat.png)

```bash
# get completion from your prompt
sparkapi prompt 详细介绍一下科大讯飞，输出Markdown结果
```
![](https://suqingdong.github.io/sparkapi/src/cmd_prompt.png)

### Python
```python
from sparkapi.core.api import SparkAPI
from sparkapi.core.config import SparkConfig
config = SparkConfig().model_dump()
api = SparkAPI(**config)

# start a chat session
api.chat()

# get completion from prompt
res = api.get_completion('hello')
print(''.join(res))

# get completion from messages
messages = [
    {'role': 'user', 'content': 'hello'},
    {'role': 'assistant', 'content': 'Hello! How can I assist'},
    {'role': 'user', 'content': 'write me a Python script of BubbleSort'},
]
res = api.get_completion_from_messages(messages)
print(''.join(res))
```

### Changelog

#### [1.0.3] - 2023-10-26
- Add support for `v3.0`