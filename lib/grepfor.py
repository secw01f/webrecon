import subprocess
import os

def grepfor():
    os.chdir('./out')

    domains = os.listdir('.')

    exclude = ['nmap', 'index', 'searchsploit', 'aquatone', 'gf']

    for domain in domains:
        if domain not in exclude:
            try:
                os.mkdir(str(domain + '/gf'))

                os.chdir(domain)

                with open('list', 'w') as paterns:
                    subprocess.call('gf -list', shell=True, stdout=paterns)
                    paterns.close()

                with open('list', 'r') as paternlist:
                    for patern in paternlist:
                        with open(('gf/' + patern), 'w') as output:
                            subprocess.call(('gf %s' % (patern)), shell=True, stdout=output)
                            output.close()

                        paterns.close()

                os.remove('list')

                print('[ + ] Completed greping for interesting information!')
                print('[ + ] Results can be found under out/%s/gf' % (domain))
            except:
                print('[ - ] No grep completed for %s' % (domain))
                print('[ - ] Skipping grep for %s' % (domain))

    os.chdir('../../')
