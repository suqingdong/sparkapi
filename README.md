# SparkDesk API and Client

## Installation
```bash
python3 -m pip install sparkapi
```

## Configuration
```bash
cat > ~/.sparkapi.env << EOF
SPARK_APP_ID=<your-app-id>
SPARK_API_KEY=<your-api-key>
SPARK_API_SECRET=<your-api-secret>
SPARK_API_MODEL=<model_version>  # v1.5, v2.0
EOF
```

## Quickstart

### CommandLine
```bash
sparkapi --help

# start a chat session
sparkapi chat

sparkapi prompt "帮我编写一个Python的菲波那切数列"
```

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
