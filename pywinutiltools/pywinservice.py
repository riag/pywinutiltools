from pywinutiltools import powershell
import click


def list(name_pattern):
    cmd_list = ['get-service']
    if name_pattern:
        cmd_list.append(name_pattern)
    cmd_list.append('|')
    cmd_list.append('sort-object status')
    powershell.exec_command(' '.join(cmd_list))


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)


@cli.command('list')
@click.pass_context
@click.argument('name_pattern', nargs=1, required=False)
def list_command(ctx, name_pattern):
    list(name_pattern)


if __name__ == '__main__':
    cli(obj={})
