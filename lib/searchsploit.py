import subprocess
import os

def searchsploit():

    os.chdir('./out')

    domains = os.listdir('.')

    exclude = ['nmap', 'index', 'searchsploit', 'aquatone', 'gf', 'list']

    for domain in domains:
        if domain not in exclude:
            if 'initial.xml' in os.listdir('%s/nmap' % (domain)):
                try:
                    filelocation = str(domain + '/searchsploit')

                    with open(filelocation, 'w') as results:
                        subprocess.call(('searchsploit -o --exclude="/dos/" --nmap %s/nmap/initial.xml' % (domain)), stdout=results)
                        results.close()

                    print('[ + ] Completed searchsploit enumeration for %s' % (domain))
                    print('[ + ] Results can be found at out/%s/searchsploit' % (domain))
                except:
                    pass
            else:
                print('[ - ] Could not complete searchsploit enumeration for %s' % (domain))
                print('[ - ] Skipping searchsploit enumeration for %s' % (domain))

    print('[ + ] Searchsploit results enumeration for all hosts complete!')

    os.chdir('..')
