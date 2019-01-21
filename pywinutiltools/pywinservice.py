from pywinutiltools import powershell
import click
import platform
import pkg_resources

machine = platform.machine()
if machine == 'amd64':
    machine = 'x86_64'

sudo_bin = pkg_resources.resource_filename(__name__, 'bin/%s/sudo.exe' % machine)


def list_service(name_pattern):
    cmd_list = ['get-service']
    if name_pattern:
        cmd_list.append(name_pattern)
    cmd_list.append('|')
    cmd_list.append('sort-object status')
    powershell.exec_command(' '.join(cmd_list))


def stop_service(name):
    powershell_bin = powershell.get_powershell_bin()
    cmd_list = [
        sudo_bin,
        powershell_bin,
        '-NoProfile',
        '-Command',
        '"& {stop-service %s}"' % name
    ]
    powershell.call(
        cmd_list
    )


def start_service(name):

    powershell_bin = powershell.get_powershell_bin()
    cmd_list = [
        sudo_bin,
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
def cli(ctx):
    ctx.ensure_object(dict)


@cli.command('list')
@click.pass_context
@click.argument('name_pattern', nargs=1, required=False)
def list_command(ctx, name_pattern):
    list_service(name_pattern)


@cli.command('stop')
@click.pass_context
@click.argument('name', nargs=1)
def stop_command(ctx, name):
    stop_service(name)


@cli.command('start')
@click.pass_context
@click.argument('name', nargs=1)
def start_command(ctx, name):
    start_service(name)


if __name__ == '__main__':
    cli(obj={})
