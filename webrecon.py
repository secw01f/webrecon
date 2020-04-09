#!/usr/bin/env python

import sys
import getopt
import os
from lib import subdomain,  directory, grepfor, nmapscanner, searchsploit, aquatone

Output = ''
Domain = ''
Directory = '/'
Subdomains = ''

def banner():
    print(' __      __      ___.  __________                             ')
    print('/  \    /  \ ____\_ |__\______   \ ____   ____  ____   ____   ')
    print('\   \/\/   // __ \| __ \|       _// __ \_/ ___\/  _ \ /    \  ')
    print(' \        /\  ___/| \_\ \    |   \  ___/\  \__(  <_> )   |  \ ')
    print('  \__/\  /  \___  >___  /____|_  /\___  >\___  >____/|___|  / ')
    print('       \/       \/    \/       \/     \/     \/           \/  ')

def usage():
    banner()
    print('Big thanks to @tomnomnom, @Fyodor, @offensive-security, and @michenriksen for creating the underlying tools')
    print('')
    print('')
    print('Usage:')
    print('')
    print('Optional:')
    print('-h   help       Prints this usage message')
    print('-o   output     Name of the directory you would like created and have output stored (Default: current directory)')
    print('-D   direnum    Single directory or file of directories to enumerate agains identified hosts (Default: / "root directory")')
    print('-s   subs       Skips subdomain enumeration and uses defined file of subdomains')
    print('')
    print('Required:')
    print('-d   domain     Domain in which to conduct reconnaissance against')
    print('')
    print('')
    print('Example:')
    print('')
    print('python webrecon.py -o example -d example.com -D /wp-admin')
    print('python webrecon.py -d example.com -D /path/to/directories.txt')
    print('\n')

def main():

    global Output
    global Domain
    global Directory
    global Subdomains

    if not sys.argv[1:]:
        usage()
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'ho:d:D:s:', ['help', 'output', 'domain', 'direnum'])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit()

    for o,a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit()
        elif o in ('-o', '--output'):
            Output = a
        elif o in ('-d', '--domain'):
            Domain = a
        elif o in ('-D', '--direnum'):
            Directory = a
        elif o in ('-s', '--subs'):
                Subdomains = a

    banner()
    print('\n')

    if len(Output) > 0:
        os.makedirs(Output)
    else:
        pass

    if len(Subdomains) == 0:
        print('[ + ] Enumerating subdomains for %s' % (Domain))

        os.chdir(Output)

        subdomain.assetfinder(Domain)
    else:
        print('[ + ] Creating subs file with list from %s' % (Subdomains))
        with open(Subdomains, 'r') as subs:
            list = subs.readlines()

            os.chdir(Output)

            with open('subs', 'w') as newsubs:
                for x in list:
                    newsubs.write(x)
                newsubs.close()

            subs.close()

    print('[ + ] Enumerating HTTP and HTTPS web hosts from the discovered subdomains')

    subdomain.httprobe()

    print('[ + ] Enumertating directorie(s) for each host')
    print('[ ! ] This may take some time!')

    directory.meg(Directory)

    print('[ + ] Greping for interesting info')

    grepfor.grepfor()

    print('[ + ] Beginning nmap scanning for each host')
    print('[ ! ] This may take some time!')

    nmapscanner.nmapscan()

    print('[ + ] Running nmap results through Searchsploit to possibly find some low hanging fruit')

    searchsploit.searchsploit()

    print('[ + ] Running aquatone scan to gather screenshots')

    aquatone.aquatone()

main()
