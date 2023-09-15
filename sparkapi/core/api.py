import json
from typing import List

import click
from websockets.sync.client import connect as ws_connect


from sparkapi.util import get_wss_url
from .query import QueryParams
from .model import MODEL_MAP


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
            self._wss_url = get_wss_url(api_url, self.api_secret, self.api_key)
        return ws_connect(self._wss_url)

    def build_query(self, messages, **kwargs):
        query = QueryParams(
            app_id=self.app_id,
            domain=MODEL_MAP[self.api_model]['domain'],
            text=messages,
            **kwargs
        )
        # print(query.dump_json())
        return query.dump_json()

    def get_completion(self, prompt: str, **kwargs):
        """get completion from prompt
        """
        messages = [{'role': 'user', 'content': prompt}]
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
            if res['header']['status'] == 2:
                break
            content = res['payload']['choices']['text'][0]['content']
            yield content

    def chat(self, **kwargs):
        """start a chat session with the model.
        """
        messages = []
        while True:
            prompt = click.prompt(click.style('>>> User', fg='yellow', italic=True))
            messages.append({'role': 'user', 'content': prompt})

            # print(messages)
            result = ''.join(self.get_completion_from_messages(messages, **kwargs))
        
            click.secho(f'>>> AI: {result}', fg='cyan', bold=True)
            messages.append({'role': 'assistant', 'content': result})
