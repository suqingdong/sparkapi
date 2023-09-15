import json
from enum import Enum
from typing import Optional, List, Union, Dict
from dataclasses import dataclass, asdict


class Domain(Enum):
    GENERAL = 'general'
    GENERAL_V2 = 'generalv2'


class Role(Enum):
    USER = 'user'
    ASSISTANT = 'assistant'


@dataclass
class Header:
    app_id: str
    uid: Optional[str] = None


@dataclass
class Chat:
    domain: Domain
    temperature: float = 0.5
    max_tokens: int = 2048
    top_k: int = 4
    chat_id: Optional[str] = None


@dataclass
class Parameter:
    chat: Chat


@dataclass
class Text:
    role: Role
    content: str


@dataclass
class Message:
    text: List[Text]


@dataclass
class Payload:
    message: Message


@dataclass
class QueryParams:
    """example:
    ```python
    QueryParams(
        header=Header(app_id='app_id'),
        parameter=Parameter(chat=Chat(domain=Domain.GENERAL.value)),
        payload=Payload(message=Message(text=[
            Text(role=Role.USER.value, content='你好，你是谁'),
            Text(role=Role.ASSISTANT.value,
                 content='你好，我是星火大模型'),
        ]))
    )
    ```
    """
    header: Header
    parameter: Parameter
    payload: Payload

    def as_dict(self):
        return asdict(self)

    def as_json(self):
        return json.dumps(self.as_dict(), ensure_ascii=False)


if __name__ == '__main__':
    from pprint import pprint
    params = QueryParams(
        header=Header(app_id='app_id'),
        parameter=Parameter(chat=Chat(domain=Domain.GENERAL.value)),
        payload=Payload(message=Message(text=[
            Text(role=Role.USER.value, content='你好，你是谁'),
            Text(role=Role.ASSISTANT.value,
                 content='你好，我是星火大模型'),
        ]))
    )
    pprint(params.__dict__)
    pprint(params.as_dict())
    pprint(params.as_json())
