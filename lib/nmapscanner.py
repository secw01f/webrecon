import subprocess
import os

def nmapscan():
    os.chdir('./out')

    domains = os.listdir('.')

    exclude = ['nmap', 'index', 'searchsploit', 'aquatone', 'gf', 'list']

    for domain in domains:
        if domain not in exclude:
            try:
                os.mkdir(str(domain + '/nmap'))

                nmapfile = str(domain + '/nmap/initial')

                with open(os.devnull, 'w') as file:
                    subprocess.call(['nmap', '-T2', '-Pn', '-sS', '-sV', '-sC', '-f', '-oA', nmapfile, domain], stdout=file, stderr=file)

                print('[ + ] Nmap scan completed for %s' % (domain))
                print('[ + ] Results can be found in out/%s/nmap' % (domain))

            except:
                print('[ - ] No nmap scan completed for %s' % (domain))
                print('[ - ] Skipping scan for %s' % (domain))

    print('[ + ] Nmap scanning completed for all hosts')

    os.chdir('..')
