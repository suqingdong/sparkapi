import os
import click

from sparkapi.core.image_generation.api import SparkAPI


@click.command(name='ImageGeneration', help=click.style('Generate images based on user input prompt', fg='green'))
@click.option('-m', '--model', help='The model version to use', default='image_generation', show_default=True)
@click.option('-p', '--prompt', help='The prompt to use')
@click.option('-o', '--outfile', help='The output file path', default='out.png', show_default=True)
@click.option('--width', help='The output image width', type=int, default=512, show_default=True)
@click.option('--height', help='The output image height', type=int, default=512, show_default=True)
@click.pass_obj
def image_generation_cli(obj, **kwargs):
    api = SparkAPI(**{**obj['config'], 'api_model': kwargs['model']})
    prompt = kwargs['prompt'] or click.prompt('Enter a prompt', type=str)
    result = api.get_completion(prompt=prompt, outfile=kwargs['outfile'], height=kwargs['height'], width=kwargs['width'])
    if os.path.isfile(result):
        click.secho(f'save file: {result}', fg='green')
    elif isinstance(result, str):
        print(result)
