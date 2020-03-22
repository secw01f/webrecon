import subprocess
import sys
import os

def aquatone():
    os.chdir('./out')

    domains = os.listdir('.')

    exclude = ['nmap', 'index', 'searchsploit', 'aquatone', 'gf']

    for domain in domains:
        if domain not in exclude:
            try:
                os.mkdir(str(domain + '/aquatone'))

                os.chdir(str(domain + '/aquatone'))

                subprocess.call(('echo %s > url & cat url | aquatone -ports small -silent' % (domain)), shell=True)

                print('[ + ] Completed aquatone scan for %s' % (domain))
                print('[ + ] Results can be found at out/%s/aquatone/' % (domain))

                os.chdir('../../')
            except:
                print('[ - ] Could not complete aquatone scan')
                print('[ - ] Skipping scan for %s' % (domain))

    os.chdir('..')
