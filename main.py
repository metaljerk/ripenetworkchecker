from ipaddress import ip_network, ip_address
import argparse, requests
import json

parser = argparse.ArgumentParser(description='Determine if a given IP is in the list of Ripe Network CIDRs.')
parser.add_argument('--ip', metavar='ip', type=str,
                    help="Enter the IP in decimal format. e.g. 192.168.1.1")
args = parser.parse_args()


# ip = input('Whats the IP?')
# net = ip_network(ip)
# print(ip_address("1.1.2.2") in net)
 
url = "https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix"
