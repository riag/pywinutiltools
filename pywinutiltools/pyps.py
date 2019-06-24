
from . import powershell

@click.command()
@click.argument('id_or_name', nargs=1, required=False)
def cli(id_or_name):
    cmd_list = ['Get-Process']
    if id_or_name:
        if str.isdigit:
            cmd_list.append('-Id')
        cmd_list.append(id_or_name)

    cmd_list.append('|')
    cmd_list = cmd_list.append('Format-Table -Property Id, ProcessName, StartTime, Parent, Path')
    powershell.exec_command(' '.join(cmd_list))

if __name__ == '__main__':
    cli()