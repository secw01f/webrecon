import subprocess
import sys
import os

def assetfinder(domain):
    try:
        with open('subs', 'a') as subs:
            subprocess.call(['assetfinder', '-subs-only', domain], stdout=subs)

            print('[ + ] Subdomains enumerated with assetfinder!')

            subs.close()

    except:
        print('[ERROR] Subdomains were not enumerated. Verify the domain is valid.')

        try:
            os.remove('subs')
        except:
            pass

        sys.exit()

def amass(domain):
    try:
        with open(os.devnull, 'w') as file:
            subprocess.call(str('amass enum -d ' + domain + ' -o subs -nocolor'), shell=True, stdout=file, stderr=file)

            print('[ + ] Subdomains enumerated with AMASS!')

    except:
        print('[ERROR] Subdomains were not enumerated. Verify the domain is valid.')

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
