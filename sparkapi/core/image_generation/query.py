import json
from enum import Enum
from typing import Optional, List
from dataclasses import dataclass, asdict


class Role(Enum):
    USER = 'user'

    def __str__(self):
        return self.value


@dataclass
class Text:
    role: Role
    content: str


@dataclass
class QueryParams:
    app_id: str
    text: List[Text]
    domain: Text

    width: int = 512
    height: int = 512

    uid: Optional[str] = None

    temperature: float = 0.5
    max_tokens: int = 2048
    top_k: int = 1
    chat_id: Optional[str] = None

    def dump(self):
        text = [
            {'role': str(t.role), 'content': t.content}
            if isinstance(t, Text) else t
            for t in self.text
        ]
        data = {
            'header': {
                'app_id': self.app_id,
                'uid': self.uid,
            },
            'parameter': {
                'chat': {
                    'domain': str(self.domain),
                    'max_tokens': self.max_tokens,
                    'temperature': self.temperature,
                    'top_k': self.top_k,
                    'chat_id': self.chat_id,
                    'width': self.width,
                    'height': self.height,
                }
            },
            'payload': {
                'message': {
                    'text': text
                }
            }
        }
        return data

    def dump_json(self):
        return json.dumps(self.dump(), ensure_ascii=False)


if __name__ == '__main__':
    from pprint import pprint
    params = QueryParams(
        app_id='app_id',
        domain='general',
        # text=[Text(role=Role.USER, content='hello')],
        text=[{'role': 'user', 'content': 'hello'}],
    )
    pprint(params.dump())
    pprint(params.dump_json())
