import base64
import json
from typing import List

import click
from websockets.sync.client import connect as ws_connect

from sparkapi import MODELS as MODEL_MAP
from sparkapi.util import get_auth_url
from .query import QueryParams


class SparkAPI(object):
    def __init__(self, app_id: str, api_key: str, api_secret: str, api_model: str, **kwargs):
        self.app_id = app_id
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_model = api_model
        self._wss_url = None

    def create_wss_connection(self):
        if self._wss_url is None:
            api_url = MODEL_MAP[self.api_model]['url']
            self._wss_url = get_auth_url(api_url, self.api_secret, self.api_key)
        return ws_connect(self._wss_url)

    def build_query(self, messages, **kwargs):
        query = QueryParams(
            app_id=self.app_id,
            domain=MODEL_MAP[self.api_model]['domain'],
            text=messages,
            **kwargs
        )
        return query.dump_json()

    def get_completion(self, file, prompt: str, **kwargs):
        """get completion from prompt
        """
        image_base64 = base64.b64encode(open(file, 'rb').read()).decode()
        messages = [
            {'role': 'user', 'content': image_base64, 'content_type': 'image'},
            {'role': 'user', 'content': prompt, 'content_type': 'text'},
        ]
        return self.get_completion_from_messages(messages, **kwargs)

    def get_completion_from_messages(self, messages: List[dict], **kwargs):
        """get completion from messages
        """
        # new connection for each request
        wss = self.create_wss_connection()

        query = self.build_query(messages, **kwargs)
        wss.send(query)

        while True:
            res = json.loads(wss.recv())
            content = res['payload']['choices']['text'][0]['content']
            yield content
            if res['header']['status'] == 2:
                break

    def chat(self, **kwargs):
        """start a chat session with the model.
        """
        messages = []
        while True:
            if messages == []:
                file = click.prompt(click.style('>>> Image', fg='yellow', italic=True), type=click.Path(exists=True))
                image_base64 = base64.b64encode(open(file, 'rb').read()).decode()
                messages.append({'role': 'user', 'content': image_base64, 'content_type': 'image'},)

            prompt = click.prompt(click.style('>>> User', fg='yellow', italic=True))
            messages.append({'role': 'user', 'content': prompt})

            # print(messages)
            result = ''.join(self.get_completion_from_messages(messages, **kwargs))
        
            click.secho(f'>>> AI: {result}', fg='cyan', bold=True)
            messages.append({'role': 'assistant', 'content': result})


if __name__ == '__main__':
    from sparkapi.core.image_understanding.api import SparkAPI
    from sparkapi.config import SparkConfig
    api = SparkAPI(**SparkConfig(api_model='image_understanding').model_dump())
    file = open('out.png', 'rb')
    print(''.join(api.get_completion('out.png', '解释一下这张图片')))
    api.chat()
