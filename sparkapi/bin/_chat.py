import click

from sparkapi import MODELS
from sparkapi.core.chat.api import SparkAPI


@click.command(name='Chat', help=click.style('Chat with SparkDesk', fg='magenta'))
@click.option('-m', '--model', help='The model version to use',
              type=click.Choice([v for v in MODELS.keys() if v.startswith('v')]),
              show_choices=True)
@click.option('--chat', help='Star a chat', is_flag=True)
@click.option('-p', '--prompt', help='Prompt to get completion from')
@click.pass_obj
def chat_cli(obj, **kwargs):
    api = SparkAPI(**obj['config'])
    if kwargs['model']:
        api.api_model = kwargs['model']                   

    if kwargs['chat']:
        api.chat(**obj['chat_config'])
    else:
        prompt = kwargs['prompt'] or click.prompt('Prompt')
        result = api.get_completion(prompt, **obj['chat_config'])
        print(''.join(result))

