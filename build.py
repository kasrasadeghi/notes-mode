import os
from subprocess import Popen, PIPE, check_output

def powershell(cmd):
    return check_output(f'powershell.exe -c "{cmd}"').decode('latin-1')

def bash(cmd):
    return check_output(f'bash -c "{cmd}"').decode('latin-1')

def main():
    os.chdir('client')
    print(powershell("npm run-script build"))
    os.chdir('..')
    print(bash('rm -rf static'))
    print(bash('cp -r client/build/static .'))
    print(bash('cp client/build/index.html static'))


if __name__ == '__main__':
    main()