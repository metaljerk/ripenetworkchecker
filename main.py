import argparse
import requests
from netaddr import IPAddress, IPSet

parser = argparse.ArgumentParser(description='Determine if a given IP is in the list of Ripe Network CIDRs.')
parser.add_argument('--ip', metavar='ip', type=str, required=True,
                    help="Checks the IP in a decimal format. e.g. 192.168.1.1")
args = parser.parse_args()
 
url = "https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix"
response = requests.get(url)
data = response.json()
def iplist(url):
    for ipv4 in data['data']['resources']['ipv4']:
        yield ipv4

with open("iplist.json", "w+") as file:
        file.writelines('\n'.join(iplist(file)))

def check_ip(ip=args.ip):
    with open("iplist.json", "r") as checkfile:
        cidr = checkfile.readlines()
        while True:
            if IPAddress(ip) in IPSet(cidr):
                print("IP: %s" % IPAddress(ip), "is in the list of cidrs")
                break
            else:
                print("IP: %s" % IPAddress(ip), "is not in the list of cidrs")
                break


if __name__ == "__main__":
    check_ip()
