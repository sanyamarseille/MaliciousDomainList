#!/usr/bin/env python
#coding:UTF-8

##### NOTE ######
# data format
# === URLhaus ===
# field[0] = ID
# field[1] = dateadded
# field[2] = URL
# field[3] = URL status
# field[4] = threat
# field[5] = tags
# field[6] = urlhaus_link
# === Malware domain list
# field[0] = blank
# field[1] = blank
# field[2] = domain
# field[3] = type
# field[4] = original_reference-why_it_was_listed
# field[5] = databaseadded
#################

## set constant
# Database Server URL
URL = 'https://urlhaus.abuse.ch/downloads/csv/'
URL2 = 'http://mirror1.malwaredomains.com/files/domains.txt'
## download file path and filename
download_path = './'
download_filename = 'malicious_list.txt'

## import module
import urllib2

## main code
file = open(download_path + download_filename,'w')

## ==================================
## URLhaus part
## ==================================
response = urllib2.urlopen(URL)
for line in response:
    if line.find('#') == 0 or line.find('offline') > -1:
        continue
    field = [x.strip('"') for x in line.split(',')]
    if field[4] == "":
        continue
    if field[4] == "malware_download":
        field[4] = "malware"
    file.write(field[4] + ',' + field[2] + ',' + field[1] + '\n')

response = ""
## ==================================
## Malware domain list part
## ==================================
response = urllib2.urlopen(URL2)
for line in response:
    if line.find('#') == 0:
        continue
    line = line.replace('\r\n','')
    field = [x for x in line.split('\t')]
    file.write(field[3] + ',' + field[2] + ',' + field[5] + '\n')
file.close()