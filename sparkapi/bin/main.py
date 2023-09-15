import click


from sparkapi import version_info
from sparkapi.core.api import SparkAPI
from sparkapi.core.config import SparkConfig


CONTEXT_SETTINGS = dict(help_option_names=['-?', '-h', '--help'])


@click.group(
    name=version_info['prog'],
    help=click.style(version_info['desc'], italic=True, fg='cyan', bold=True),
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
)
@click.option('-e', '--env-file', help='Environment file', default='~/.sparkapi.env', show_default=True)
@click.pass_context
def cli(ctx, **kwargs):
    config = SparkConfig(_env_file=kwargs['env_file']).model_dump()
    print(config)
    ctx.ensure_object(dict)
    ctx.obj['config'] = config


@click.command(name='chat', help='Start a chat session')
@click.pass_obj
def chat_cli(obj):
    api = SparkAPI(**obj['config'])
    api.chat()


@click.command(name='prompt', help='Get completion form your prompt')
@click.argument('prompt', nargs=-1, required=True)
@click.pass_obj
def prompt_cli(obj, prompt):
    api = SparkAPI(**obj['config'])
    result = api.get_completion(' '.join(prompt))
    for part in result:
        print(part, end='')


def main():
    cli.add_command(chat_cli)
    cli.add_command(prompt_cli)
    cli()


if __name__ == '__main__':
    main()
