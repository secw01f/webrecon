import nmap
import os

def nmapscan():
    os.chdir('./out')

    domains = os.listdir('.')

    exclude = ['nmap', 'index', 'searchsploit', 'aquatone', 'gf']

    nm = nmap.PortScanner()

    for domain in domains:
        if domain not in exclude:
            try:
                os.mkdir(str(domain + '/nmap'))

                nmapdir = str(domain + '/nmap')

                nm.scan(hosts=domain, arguments=('-T2 -Pn -sS -sV -sC -f -oA ' + nmapdir + '/initial'))

                print('[ + ] Nmap scan completed for %s' % (domain))
                print('[ + ] Results can be found in out/%s/nmap' % (domain))
            except:
                print('[ - ] No nmap scan completed for %s' % (domain))
                print('[ - ] Skipping scan for %s' % (domain))

    print('[ + ] Nmap scanning completed for all hosts')

    os.chdir('..')
