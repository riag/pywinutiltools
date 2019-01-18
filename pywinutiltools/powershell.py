
import os
import subprocess


def get_powershell_bin():
    return os.environ.get('POWERSHELL_BIN', 'powershell.exe')


def call(cmd_list, check=True, **kwargs):
    kwargs['shell'] = True
    cmd = cmd_list
    if isinstance(cmd, (list, tuple)):
        cmd = ' '.join(cmd)
    if check:
        return subprocess.check_call(cmd, **kwargs)
    else:
        return subprocess.call(cmd, **kwargs)


def get_output(cmd_list, check=True, **kwargs):

    kwargs['shell'] = True
    kwargs['capture_output'] = True
    kwargs['check'] = check
    cmd = cmd_list
    if isinstance(cmd, (list, tuple)):
        cmd = ' '.join(cmd)

    return subprocess.run(cmd, **kwargs)


def start_process(process: str, *argv, **kwargs):
    powershell_bin = get_powershell_bin()
    cmd_list = [
            powershell_bin,
            '-NoProfile',
    ]
    args = [
        'Start-Process',
        '-FilePath', '\\"%s\\"' % process,
    ]
    if len(argv) > 0:
        args.append('-ArgumentList')
        v_list = ['\\"%s\\"' % v for v in argv]
        args.append(', '.join(v_list))

    cmd_list.append(
            '"%s"' % ' '.join(args)
        )
    call(cmd_list, **kwargs)


def start(filepath: str, **kwargs):
    powershell_bin = get_powershell_bin()
    cmd_list = [
            powershell_bin,
            '-NoProfile',
            '"%s"' % filepath
    ]
    call(cmd_list, **kwargs)


def exec_command(cmd, capture=False, **kwargs):
    powershell_bin = get_powershell_bin()
    cmd_list = [
            powershell_bin,
            '-NoProfile',
            '-Command',
            '"& {%s}"' % cmd
    ]
    if capture:
        return get_output(cmd_list, **kwargs)
    else:
        call(cmd_list, **kwargs)
