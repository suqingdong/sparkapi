import base64
from io import BytesIO

import requests
from PIL import Image

from sparkapi import MODELS as MODEL_MAP
from sparkapi.util import get_auth_url
from .query import QueryParams


class SparkAPI(object):
    def __init__(self, app_id: str, api_key: str, api_secret: str, api_model: str, **kwargs):
        self.app_id = app_id
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_model = api_model
        self._auth_url = None

    @property
    def auth_url(self):
        if self._auth_url is None:
            api_url = MODEL_MAP[self.api_model]['url']
            self._auth_url = get_auth_url(api_url, self.api_secret, self.api_key, method='POST')
        return self._auth_url

    def build_query(self, messages, **kwargs):
        query = QueryParams(
            app_id=self.app_id,
            domain=MODEL_MAP[self.api_model]['domain'],
            text=messages,
            **kwargs
        )
        return query.dump()

    def get_completion(self, prompt: str, outfile=None, **kwargs):
        """get completion from prompt

        注： 文生图目前仅开放单轮交互，单轮交互只需要传递一个user角色的数据
        """
        messages = [{'role': 'user', 'content': prompt}]
        query = self.build_query(messages, **kwargs)

        response = requests.post(self.auth_url, json=query, headers={'content-type': "application/json"})
        data = response.json()

        if data['header']['code'] != 0:
            print(f'[ERROR]：{data}')
            return None

        image_data = data['payload']['choices']['text'][0]['content']

        if outfile:
            return self.save_image(image_data, outfile)

        return data
    
    @staticmethod
    def save_image(image_data, outfile):
        if outfile == 'data_url':
            uri = f'data://image/png;base64,{image_data}'
            return uri
        im = Image.open(BytesIO(base64.b64decode(image_data)))
        im.save(outfile)
        return outfile


if __name__ == '__main__':
    from sparkapi.core.image_generation.api import SparkAPI
    from sparkapi.config import SparkConfig
    api = SparkAPI(**SparkConfig(api_model='image_generation').model_dump())
    # res = api.get_completion('帮我生成一张二次元风景图', outfile='data_url')
    res = api.get_completion('帮我生成一张二次元风景图', outfile='out.png')
    print(res)

