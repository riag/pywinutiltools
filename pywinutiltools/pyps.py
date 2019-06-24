
from . import powershell
import click

@click.command()
@click.option('--list', 'show_as_list', is_flag=True, default=False)
@click.argument('id_or_name', nargs=1, required=False)
def cli(show_as_list, id_or_name):
    # Get-CimInstance  -Query "select * from Win32_Process where name like '%java%' " |Format-list ProcessId , CommandLine
    # Get-CimInstance  -Query "select * from Win32_Process where ProcessId = 16632" |Format-list *
    cmd_list = ['Get-CimInstance', '-Query']
    sql = 'select \* from Win32_Process'
    where = ''
    if id_or_name:
        if str.isdigit(id_or_name):
            where = 'ProcessId = %s' % id_or_name
        else:
            where = "name like '\"%%%s%%\"'" % id_or_name

    if where:
        sql = '%s where %s' % (sql, where)

    cmd_list.append("'\"%s\"'" % sql)
    cmd_list.append('|')
    if show_as_list:
        cmd_list.append('Format-List')
    else:
        cmd_list.append('Format-Table')

    cmd_list.append('ProcessId, ProcessName, Path, CommandLine')

    powershell.exec_command(' '.join(cmd_list))

if __name__ == '__main__':
    cli()
