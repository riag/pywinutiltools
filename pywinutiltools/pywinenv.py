from pywinutiltools import powershell
from pywinutiltools.util import ask_yes_or_no
import click


def list_env(name):
    if name:
        powershell.exec_command('(get-childitem  Env:%s).Value' % name)
    else:
        powershell.exec_command('get-childitem  Env:')


def set_env(name, value):
    powershell.exec_command(
    '[Environment]::SetEnvironmentVariable(\\"%s\\", \\"%s\\", \\"User\\")' % (
        name, value
    ))


def get_env(name):
    powershell.exec_command(
        '[environment]::GetEnvironmentVariable(\\"%s\\", \\"User\\")' % name
    )


def append_env(name, value):
    p = powershell.exec_command(
        '[environment]::GetEnvironmentVariable(\\"%s\\", \\"User\\")' % name,
        capture=True
    )
    old_value = None
    if p.stdout:
        old_value = p.stdout.decode('utf-8').rstrip('\r\n')

    if old_value:
        m = '%s;%s' % (old_value, value)
        value = m

    set_env(name, value)


def delete_env(name):
    powershell.exec_command(
    '[Environment]::SetEnvironmentVariable(\\"%s\\", \\$null, \\"User\\")' % name
    )


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)


@cli.command('list')
@click.pass_context
@click.argument('name', nargs=1, required=False)
def list_command(ctx, name):
    list_env(name)


@cli.command('get')
@click.pass_context
@click.argument('name', nargs=1)
def get_command(ctx, name):
    get_env(name)


@cli.command('set')
@click.pass_context
@click.argument('name', nargs=1)
@click.argument('value', nargs=1)
def set_command(ctx, name, value):
    set_env(name, value)


@cli.command('append')
@click.pass_context
@click.argument('name', nargs=1)
@click.argument('value', nargs=1)
def append_command(ctx, name, value):
    append_env(name, value)


@cli.command('delete')
@click.pass_context
@click.option('-f', '--force', is_flag=True, default=False)
@click.argument('name_list', nargs=-1)
def delete_command(ctx, force, name_list):
    for name in name_list:
        if not force:
            answer = ask_yes_or_no('delete env name %s ?' % name)
            if not answer:
                continue

        delete_env(name)


if __name__ == '__main__':
    cli(obj={})
