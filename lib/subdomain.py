import subprocess
import sys
import os

def assetfinder(domain):
    try:
        with open('subs', 'w') as subs:
            subprocess.call(['assetfinder', '-subs-only', domain], stdout=subs)

            print('[ + ] Subdomains enumerated!')

            subs.close()

        with open('subs', 'r') as subs:
            count = 0
            lines = subs.readlines()
            for line in lines:
                count += 1

            subs.close()

            print('[ + ] Found a total of %d subdomains' % (count))
    except:
        print('[ERROR] Subdomains were not enumerated. Verify the domain is valid.')

        os.remove('subs')

        sys.exit()

def httprobe():
    try:
        with open('hosts', 'w') as hosts:
            subprocess.call('cat subs | httprobe', shell=True, stdout=hosts)

            print('[ + ] Hosts enumerated!')

            hosts.close()

        with open('hosts', 'r') as hosts:
            count = 0
            lines = hosts.readlines()
            for line in lines:
                count += 1

            hosts.close()

            print('[ + ] Found a total of %d hosts' % (count))
    except:
        print('[ - ] No hosts were identified')
        print('[ - ] Exiting...')
        
        os.remove('hosts')

        sys.exit()
