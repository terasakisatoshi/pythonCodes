# hello.py
import click

"""
---- usage ----
> hello --home-directory tmp say -s world -i 3
>Home directory is tmp
>Hello world!
>Hello world!
>Hello world!
"""

class Config(object):
 
    def __init__(self):
        self.verbose = False
 
pass_config = click.make_pass_decorator(Config, ensure=True)
 
@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--home-directory', type=click.Path())
@pass_config
def cli(config, verbose, home_directory):
    config.verbose = verbose
    if home_directory is None:
        home_directory = '.'
    config.home_directory = home_directory
 
@cli.command()
@click.option('-s','--string', default='World',
              help='This is  the thing that is greeted.')
@click.option('-i','--iteration', default=1,
              help='How many times you should be greeted.')
@click.argument('out', type=click.File('w'), default='-',
                required=False)
@pass_config
def say(config, string, iteration, out):
    """This script greets you."""
    if config.verbose:
        click.echo('We are in verbose mode')
    click.echo('Home directory is %s' % config.home_directory)
    for x in range(iteration):
        click.echo( 'Hello %s!' % string, file=out)