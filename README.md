![PyPI - Version](https://img.shields.io/pypi/v/sparkapi-python)
![PyPI - Status](https://img.shields.io/pypi/status/sparkapi-python)
![PyPI - License](https://img.shields.io/pypi/l/sparkapi-python)

# Spark API and Client
> https://www.xfyun.cn/doc/spark/Web.html

***接口说明***
注意： 该接口可以正式使用。如您需要申请使用，请点击前往[产品页面 ](https://xinghuo.xfyun.cn/sparkapi?scr=price)

## 一 安装
```bash
python3 -m pip install -U sparkapi-python
```

## 二 配置
> 拷贝 `example.env` 到 `~/.sparkapi.env` 并修改成自己的配置
```
SPARK_APP_ID=<your-app-id>
SPARK_API_SECRET=<your-api-secret>
SPARK_API_KEY=<your-api-key>
SPARK_API_MODEL='v3.5'          # v1.5, v2.0, v3.0, v3.5
SPARK_CHAT_MAX_TOKENS=4096      # V1.5取值为[1,4096]， V2.0、V3.0和V3.5取值为[1,8192]，默认为2048。
SPARK_CHAT_TEMPERATURE=0.5      # 取值范围 (0，1] ，默认值0.5
SPARK_CHAT_TOP_K=4              # 取值为[1，6],默认为4
```

## 三 快速开始

### 3.1 命令行模式
```bash
sparkapi --help

"
Usage: sparkapi [OPTIONS] COMMAND [ARGS]...

  Spark API and Client

Options:
  --version            Show the version and exit.
  -e, --env-file TEXT  Environment file  [default: ~/.sparkapi.env]
  -?, -h, --help       Show this message and exit.

Commands:
  Chat                Chat with SparkDesk
  ImageGeneration     Generate images based on user input prompt
  ImageUnderstanding  Understanding the image and engaging in conversation

  Contact: suqingdong <suqingdong1114@gmail.com> 
"
```
#### 3.1.1. Chat [星火认知大模型]
```bash
sparkapi Chat --help

"
Usage: sparkapi Chat [OPTIONS]

  Chat with SparkDesk

Options:
  -m, --model [v1.5|v2.0|v3.0|v3.5]
                                  The model version to use
  --chat                          Star a chat
  -p, --prompt TEXT               Prompt to get completion from
  -h, -?, --help                  Show this message and exit.
"
```
***prompt模式***
```bash
# 使用默认模型
sparkapi Chat -p 你是谁？
"
您好，我是科大讯飞研发的认知智能大模型，我的名字叫讯飞星火认知大模型。我可以和人类进行自然交流，解答问题，高效完成各领域认知智能需求。
"

# 指定模型
sparkapi Chat -p 你是谁？ -m v1.5
"
作为一个认知智能模型，可以回答你的问题和提供帮助。
"
```

***chat模式***
```bash
sparkapi Chat --chat
```
<pre>
>>> User: 你是谁?
>>> AI: 您好，我是科大讯飞研发的认知智能大模型，我的名字叫讯飞星火认知大模型。我可以和人类进行自然交流，解答问题，高效完成各领域认知智能需求。
>>> User: 使用Python编写斐波那契数列函数, 仅输出代码块
>>> AI: ```python
def fibonacci(n):
    if n <= 0:
        return "输入错误，请输入大于0的整数"
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

# 测试
print(fibonacci(10))
>>> User: 
</pre>

#### 3.1.2. ImageGeneration [图像生成]
```bash
sparkapi ImageGeneration --help

"
Usage: python -m sparkapi.bin.cli ImageGeneration [OPTIONS]

  Generate images based on user input prompt

Options:
  -m, --model TEXT    The model version to use  [default: image_generation]
  -p, --prompt TEXT   The prompt to use
  -o, --outfile TEXT  The output file path  [default: out.png]
  -?, -h, --help      Show this message and exit.
"
```

***example***

```bash
sparkapi ImageGeneration -p 一只可爱的小狗在奔跑 -o dog.png
"save file: dog.png"

# 指定宽高
sparkapi ImageGeneration -p 一只可爱的小狗在奔跑 -o dog.1280x720.png --width 1280 --height 720 
"save file: dog.1280x720.png"
```

#### 3.1.3. ImageUnderstanding [图像理解]
```bash
sparkapi ImageUnderstanding --help
"
Usage: python -m sparkapi.bin.cli ImageUnderstanding [OPTIONS]

  Understanding the image and engaging in conversation

Options:
  -m, --model TEXT   The model version to use  [default: image_generation]
  --chat             Start a chat
  -f, --file PATH    The image file to use
  -p, --prompt TEXT  The prompt to use
  -h, -?, --help     Show this message and exit.
"
```
***prompt模式***
```bash
sparkapi ImageUnderstanding -f dog.png -p 描述下这张图片
"
这是一张非常可爱的小狗的图片。小狗看起来非常活泼和快乐，它的眼睛闪烁着好奇的光芒，嘴巴微微张开，仿佛在欢快地叫唤或是呼吸新鲜空气。
它的毛发呈现出金黄色，与背景中的阳光形成了和谐的对比。阳光从画面的上方斜射下来，为整个场景增添了一种温暖和明亮的感觉。
小狗的四肢健壮，正在奔跑中，尾巴高高翘起，显示出它的活力和快乐。
整体上，这张图片给人一种温馨、愉悦的感觉，仿佛是在一个美好的夏日午后拍摄的。
"
```
***chat模式***
```bash
sparkapi ImageUnderstanding --chat
"
>>> Image:./dog.png
>>> User: 描述一下这张图片
>>> AI: 这是一张非常可爱的小狗的图片。小狗呈现出金黄色，眼睛大而明亮，嘴巴微微张开，舌头伸出，看起来非常开心和活泼。它的耳朵长且柔软，尾巴高高翘起。背景是模糊的自然景色，阳光从背后照射下来，为整张图片增添了一种温暖和明亮的感觉。整体上，这张图片给人一种轻松愉快的感觉，仿佛小狗正在享受一个美好的下午时光。
>>> User: 精简成4点
>>> AI: 1. 图片展示了一只活泼的金黄色小狗在阳光明媚的自然背景下奔跑。
2. 小狗的眼睛大而明亮，嘴巴微微张开，舌头伸出，看起来非常开心和兴奋。
3. 背景是模糊的自然景色，阳光从背后照射下来，为整张图片增添了一种温暖和明亮的感觉。
4. 整体上，这张图片给人一种轻松愉快的感觉，仿佛小狗正在享受一个美好的下午时光。
>>> User: 
"
```

### 3.2 Python中使用
```python
from sparkapi.config import SparkConfig
from sparkapi.core.chat.api import SparkAPI as ChatAPI
from sparkapi.core.image_generation.api import SparkAPI as ImageGenerationAPI
from sparkapi.core.image_understanding.api import SparkAPI as ImageUnderstandingAPI

# Chat
api = ChatAPI(**SparkConfig().model_dump())
result = api.get_completion('你好')
print(''.join(result))

# ImageGeneration
api = ImageGenerationAPI(**SparkConfig(api_model='image_generation').model_dump())
result = api.get_completion('帮我生成一张二次元风景图', outfile='out.png')
print(result)

# ImageUnderstanding
api = ImageUnderstandingAPI(**SparkConfig(api_model='image_understanding').model_dump())
result = api.get_completion('out.png', '解释一下这张图片')
print(''.join(result))
```


## 四 Changelog

#### [1.0.7] - 2024-06-28
- Add support for model `v4.0`

#### [1.0.5] - 2024-03-05
- Add support for `ImageGeneration` and `ImageUnderstanding`

#### [1.0.4] - 2024-03-04
- Add support for model `v3.5`
- Bug fixed: `SparkAPI.get_completion_from_messages`

#### [1.0.3] - 2023-10-26
- Add support for model `v3.0`


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=suqingdong/sparkapi&type=Date)](https://star-history.com/#suqingdong/sparkapi&Date)
