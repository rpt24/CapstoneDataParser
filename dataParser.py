# -*- coding: utf-8 -*-
import re
import csv

# function for parsing cloudflare kdig
def parseCloudflareKdig():
    dnsTiming = [] # list to store timings
    keyString = '(UDP) in' # key string for timing line
    with open('data/cloudflare/kdigDnsData.txt') as dataFile:
        for line in dataFile:
            if keyString in line:
                # get the number in between that sub string
                time = re.search('in (.*) ms',line)
                dnsTiming.append(time.group(1)) # add to timing list
    # write to output file
    output = open('kdigData_Cloudflare.csv', 'w+', newline='')
    writer = csv.writer(output)
    for row in dnsTiming:
        writer.writerow([row])

# function for parsing google kdig data
def parseGoogleKdig():
    dnsTiming = [] # list to store
    keyString = '(UDP) in' # key to use that line
    with open('data/google/kdigDnsData.txt') as dataFile:
        for line in dataFile:
            if keyString in line:
                time = re.search('in (.*) ms', line)
                dnsTiming.append(time.group(1))
    output = open('kdigData_Google.csv', 'w+', newline='')
    writer = csv.writer(output)
    for row in dnsTiming:
        writer.writerow([row])
   
def httpParser(filepath, httpList):
    keyString = 'time_total:'
    with open(filepath) as dataFile:
        for line in dataFile:
            if keyString in line:
                time = re.search('time_total: (.*)s',line)
                data = time.group(1)
                data = data.strip()
                httpList.append(data)
                
def httpWriter(filepath, httpList):
    with open(filepath, 'w+', newline='') as output:
        writer = csv.writer(output)
        for row in httpList:
            writer.writerow([row])
     
def parseCloudflareCurl():
    http1_0 = []
    http1_1 = []
    http2 = []
    http3 = []
    httpParser('data/cloudflare/http1-0Data.txt', http1_0)
    httpParser('data/cloudflare/http1-1Data.txt', http1_1)
    httpParser('data/cloudflare/http2Data.txt', http2)
    httpParser('data/cloudflare/http3Data.txt', http3)
    httpWriter('http1-0_Cloudflare.csv', http1_0)
    httpWriter('http1-1_Cloudflare.csv', http1_1)
    httpWriter('http2_Cloudflare.csv', http2)
    httpWriter('http3_Cloudflare.csv', http3)
                

# main
if __name__ == "__main__":
    # parse the kdig for cloudflare
    #parseCloudflareKdig()
    # parse the kdig for google
    #parseGoogleKdig()
    parseCloudflareCurl()