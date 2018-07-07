import os
from subprocess import Popen, PIPE, check_output

def bash(cmd):
    return check_output(['bash', '-c', cmd]).decode('latin-1')

def main():
    os.chdir('client')
    # print(bash('pwd'))
    print(bash("npm run-script build-css"))
    print(bash("npm run-script build"))
    os.chdir('..')
    print(bash('rm -rf static'))
    print(bash('cp -r client/build/static .'))
    print(bash('cp client/build/index.html static'))


if __name__ == '__main__':
    main()