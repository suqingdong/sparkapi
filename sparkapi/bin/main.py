import click


from sparkapi import version_info
from sparkapi.core.api import SparkAPI
from sparkapi.core.config import SparkConfig


CONTEXT_SETTINGS = dict(help_option_names=['-?', '-h', '--help'])


@click.command(
    name=version_info['prog'],
    help=click.style(version_info['desc'], italic=True, fg='cyan', bold=True),
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
)
@click.option('-e', '--env-file', help='Environment file', default='~/.sparkapi.env', show_default=True)
def cli(**kwargs):
    config = SparkConfig(_env_file=kwargs['env_file']).model_dump()
    print(config)
    sp = SparkAPI(**config)
    sp.chat()


def main():
    cli()


if __name__ == '__main__':
    main()
