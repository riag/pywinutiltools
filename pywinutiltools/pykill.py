
from . import powershell

import click

@click.command()
@click.option('--winsudo-bin', required=True)
@click.argument('id_or_name', nargs=1, required=True)
def cli(winsudo_bin, id_or_name):
    powershell_bin = powershell.get_powershell_bin()

    arg = ''
    if str.isdigit(id_or_name):
        arg = '-Id %s' % id_or_name
    else:
        arg = '-Name %s' % id_or_name

    cmd_list = [
        winsudo_bin,
        powershell_bin,
        '-NoProfile',
        '-Command',
        '"& {stop-process %s}"' % arg
    ]
    powershell.call(
        cmd_list
    )


if __name__ == '__main__':
    cli()