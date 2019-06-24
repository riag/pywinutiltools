from pywinutiltools import powershell
import click

def list_service(winsudo_bin, name_pattern):
    cmd_list = ['get-service']
    if name_pattern:
        cmd_list.append(name_pattern)
    cmd_list.append('|')
    cmd_list.append('sort-object status')
    powershell.exec_command(' '.join(cmd_list))


def stop_service(winsudo_bin, name):
    powershell_bin = powershell.get_powershell_bin()

    cmd_list = [
        winsudo_bin,
        powershell_bin,
        '-NoProfile',
        '-Command',
        '"& {stop-service %s}"' % name
    ]
    powershell.call(
        cmd_list
    )


def start_service(winsudo_bin, name):

    powershell_bin = powershell.get_powershell_bin()
    cmd_list = [
        winsudo_bin,
        powershell_bin,
        '-NoProfile',
        '-Command',
        '"& {start-service %s}"' % name
    ]
    powershell.call(
        cmd_list
    )


@click.group()
@click.pass_context
@click.option('--winsudo-bin', required=True)
def cli(ctx, winsudo_bin):
    ctx.ensure_object(dict)
    ctx.obj['winsudo_bin'] = winsudo_bin


@cli.command('list')
@click.pass_context
@click.argument('name_pattern', nargs=1, required=False)
def list_command(ctx, name_pattern):
    winsudo_bin = ctx.obj['winsudo_bin']
    list_service(winsudo_bin, name_pattern)


@cli.command('stop')
@click.pass_context
@click.argument('name', nargs=1)
def stop_command(ctx, name):
    winsudo_bin = ctx.obj['winsudo_bin']
    stop_service(winsudo_bin, name)


@cli.command('start')
@click.pass_context
@click.argument('name', nargs=1)
def start_command(ctx, name):
    winsudo_bin = ctx.obj['winsudo_bin']
    start_service(winsudo_bin, name)


if __name__ == '__main__':
    cli(obj={})
