import subprocess
import os
import shutil

def grepfor():
    os.chdir('./out')

    domains = os.listdir('.')

    exclude = ['nmap', 'index', 'searchsploit', 'aquatone', 'gf', 'list']

    for domain in domains:
        if domain not in exclude:
            try:
                os.mkdir(domain + '/gf')
                os.mkdir('gf')
                os.chdir(domain)

                with open('../list', 'w') as paterns:
                    subprocess.call('gf -list', shell=True, stdout=paterns)
                    paterns.close()

                with open('../list', 'r') as paternlist:
                    paterns = paternlist.readlines()
                    paternlist.close()

                for patern in paterns:
                    outfile = str('../gf/' + patern.rstrip())
                    with open(outfile, 'w') as file:
                        with open(os.devnull, 'w') as out:
                            subprocess.call(str('gf ' + patern.rstrip()), shell=True, stdout=file, stderr=out)
                        file.close()

                for patern in paterns:
                    shutil.copy(('../gf/' + patern.rstrip()), ('./gf/' + patern.rstrip()))

                shutil.rmtree('../gf')

                os.remove('../list')

                os.chdir('../')

                print('[ + ] Completed greping for interesting information!')
                print('[ + ] Results can be found under out/%s/gf' % (domain))
            except:
                print('[ - ] No grep completed for %s' % (domain))
                print('[ - ] Skipping grep for %s' % (domain))

                os.remove('../list')
                shutil.rmtree('../gf')

    os.chdir('../')
