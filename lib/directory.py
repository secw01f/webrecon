import subprocess
import sys

def meg(directory):
    try:
        subprocess.call(('meg -X GET %s hosts' % (directory)), shell=True)

        print('[ + ] Directories enumerated!')
        print('[ + ] Find index for directory enumeration at out/index')
    except:
        print('[ERROR] Was not able to conduct directory enumeration')

        sys.exit()
