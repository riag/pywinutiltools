
from . import powershell
import click

@click.command()
@click.argument('id_or_name', nargs=1, required=False)
def cli(id_or_name):
    # Get-CimInstance  -Query "select * from Win32_Process where name like '%java%' " |Format-list ProcessId , CommandLine
    # Get-CimInstance  -Query "select * from Win32_Process where ProcessId = 16632" |Format-list *
    cmd_list = ['Get-CimInstance', '-Query']
    sql = 'select * from Win32_Process'
    where = ''
    if id_or_name:
        if str.isdigit(id_or_name):
            where = 'ProcessId = %s' % id_or_name
        else:
            where = "name like '%%s%'" % id_or_name

    if where:
        sql = '%s where %s' % (sql, where)

    cmd_list.append('|')
    cmd_list.append('Format-Table -Property ProcessId, ProcessName, Path, CommandLine')
    powershell.exec_command(' '.join(cmd_list))

if __name__ == '__main__':
    cli()
