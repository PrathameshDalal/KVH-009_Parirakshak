# script by Heath Stewart 20 Nov 2020
# get the geolocation of an IP address or a file containing a list of addresses
# data gathered: lat/long coordinates, organization name, country, state, city, isp, and as number/organization
# the data is queried from http://ip-api.com/json, see documentation at https://ip-api.com/docs/api:json#test
# no api key is needed

import requests
import argparse
from tabulate import tabulate
from operator import itemgetter
from time import sleep


# define a function for the arguments we will accept, can be a single IP or a file with a list
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip-address', dest='ip', help='IP address to locate.')
    parser.add_argument('-f', '--file', dest='file', help='File with IP addresses to locate.')
    options = parser.parse_args()

    return options


options = get_args()
located_list = []


# define a function for geolocation given an IP address
def locate(obj):
    ip = options.ip

    # store our request in response
    response = requests.get(f"http://ip-api.com/json/{ip}" + "?fields=org,country,regionName,city,lat,lon,isp,as")
    resp_data = response.json()       # store the data in json format in resp_data
    ip_data = {'ip_address': options.ip}    # create new dict for ip address
    results = {**ip_data, **resp_data}      # create results dict with ip address first
    located_list.append(results)
    sleep(2)


# define a function to handle the file processing if the '-f' option is used
def process_file(file):
    # initialize an empty list to store the IP addresses
    ip_list = []

    # open the file for reading and append the lines to ip_list
    with open(options.file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            ip_list.append(line.strip())    # strip \n for the input to be correct in locate() function
        for i in ip_list:
            options.ip = i
            locate(options.ip)      # call the locate() function and get the geolocation data for the ip_list item


# if the '-i' option for a single IP is used, call locate(), otherwise call process_file() for '-f' option
if options.ip:
    locate(options.ip)
elif options.file:
    process_file(options.file)

# print the final results nicely in a table
print(tabulate(sorted(located_list, key=itemgetter(
        "ip_address",
        "country",
        "regionName",
        "city",
        "isp",
        "org",
        "as")), headers="keys"))