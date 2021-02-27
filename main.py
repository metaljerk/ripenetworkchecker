from ipaddress import ip_network, ip_address
import argparse, requests
import ipaddress
from netaddr import IPNetwork, IPAddress
import json

parser = argparse.ArgumentParser(description='Determine if a given IP is in the list of Ripe Network CIDRs.')
parser.add_argument('--ip', metavar='ip', type=str,
                    help="Enter the IP in decimal format. e.g. 192.168.1.1")
args = parser.parse_args()


# ip = input('Whats the IP?')
# net = ip_network(ip)
# print(ip_address("1.1.2.2") in net)
 
url = "https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix"
response = requests.get(url)
data = response.json()
def iplist(url):
    for ipv4 in data['data']['resources']['ipv4']:
        yield ipv4

with open("iplist.json", "w+") as file:
        file.writelines('\n'.join(iplist(file)))

def check_ip():
    with open("iplist.json", "r") as checkfile:
        iplist = checkfile.readline()
        if str(IPAddress("2.56.32.1")) in IPNetwork(iplist):
            print(True)
        else:
            print(False)
        # if IPAddress("2.56.164.1") in IPNetwork(str(iplist)):
        #     print(True)
        # else:
        #     print(False)
    # if IPAddress(iplist(url)) in IPNetwork("64.190.60.0/23"):
    #     print(True)
    # else: 
    #     print(False)

if __name__ == "__main__":
    check_ip()
    # iplist(url)