import click

from sparkapi import version_info
from sparkapi.config import SparkConfig, ChatConfig
from sparkapi.bin._image_generation import image_generation_cli
from sparkapi.bin._image_understanding import image_understanding_cli
from sparkapi.bin._chat import chat_cli


CONTEXT_SETTINGS = dict(help_option_names=['-?', '-h', '--help'], max_content_width=200)

epilog = click.style('''

Contact: {author} <{author_email}>
''').format(**version_info)

@click.group(
    name=version_info['prog'],
    help=click.style(version_info['desc'], italic=True, fg='cyan', bold=True),
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
    epilog=epilog,
)
@click.version_option(version=version_info['version'], prog_name=version_info['prog'])
@click.option('-e', '--env-file', help='Environment file', default='~/.sparkapi.env', show_default=True)
@click.pass_context
def cli(ctx, **kwargs):
    config = SparkConfig(_env_file=kwargs['env_file']).model_dump()
    chat_config = ChatConfig(_env_file=kwargs['env_file']).model_dump()

    ctx.ensure_object(dict)
    ctx.obj['config'] = config
    ctx.obj['chat_config'] = chat_config


def main():
    cli.add_command(chat_cli)
    cli.add_command(image_generation_cli)
    cli.add_command(image_understanding_cli)
    cli()


if __name__ == '__main__':
    main()
