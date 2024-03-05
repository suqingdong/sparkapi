import click

from sparkapi.core.image_understanding.api import SparkAPI


@click.command(name='ImageUnderstanding', help=click.style('Understanding the image and engaging in conversation', fg='yellow'))
@click.option('-m', '--model', help='The model version to use', default='image_understanding', show_default=True)
@click.option('--chat', help='Start a chat', is_flag=True)
@click.option('-f', '--file', help='The image file to use', type=click.Path(exists=True))
@click.option('-p', '--prompt', help='The prompt to use', type=str)
@click.pass_obj
def image_understanding_cli(obj, **kwargs):
    api = SparkAPI(**{**obj['config'], 'api_model': kwargs['model']})
    if kwargs['chat']:
        api.chat(**obj['chat_config'])
    else:
        file = kwargs['file'] or click.prompt('Enter the image file path', type=click.Path(exists=True))
        prompt = kwargs['prompt'] or click.prompt('Enter the prompt', type=str)
        result = api.get_completion(file=file, prompt=prompt)
        print(''.join(result))
    