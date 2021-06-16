#input - City, WW#, 911 Caller ID,  CFB can only be 15 chars
import sys
import jinja2
from build_configs import BuildConfigs
import csv
import os
config = BuildConfigs('templates')

city = input ("What is the City?: ")
while " " in city:
    city = input ("Please Re-enter the City without spaces: ")

ww = input ("What is the Site Number?: ")
emergency = input ("What is the 911 Caller ID?:")


while len(emergency) != 10:
    emergency = input ("Please re-enter the 911 Caller ID")
    


dir_path="./configs/WW" + ww + " " + city+'/'

os.makedirs(dir_path)


cfb = 'WW' + ww + '-' + city
while len(cfb)>15:
    print (cfb + ":ERROR CFB Too long Max City Length 10 Characters")
    stub_city = input ("Please shorten the City: ")
    cfb = 'WW' + ww + '-' + stub_city



print ("Conference Bridge is: " + cfb)
site_dict = {
    'jcity' : city,
    'jww' : ww,
    'jemergency' : emergency,
    'jcfb' : cfb
}

config.build_config(dir_path  + "header.txt" , site_dict, 'header.j2')
config.build_config(dir_path  + "partition.csv" , site_dict, 'Partition.j2')
config.build_config(dir_path  + "callmanagergroup.csv" , site_dict, 'callmanagergroup.j2')
config.build_config(dir_path  + "callpark.csv" , site_dict, 'callpark.j2')
config.build_config(dir_path  + "conferencebridge.csv" , site_dict, 'conferencebridge.j2')
config.build_config(dir_path  + "css.csv" , site_dict, 'css.j2')
config.build_config(dir_path  + "datetimegroup.csv" , site_dict, 'datetimegroup.j2')
config.build_config(dir_path  + "devicepool.csv" , site_dict, 'devicepool.j2')
config.build_config(dir_path  + "huntpilot.csv" , site_dict, 'huntpilot.j2')
config.build_config(dir_path  + "location.csv" , site_dict, 'location.j2')
config.build_config(dir_path  + "mediaresourcegroup.csv" , site_dict, 'mediaresourcegroup.j2')
config.build_config(dir_path  + "mediaresourcegrouplist.csv" , site_dict, 'mediaresourcegrouplist.j2')
config.build_config(dir_path  + "region.csv" , site_dict, 'region.j2')
config.build_config(dir_path  + "routepattern.csv" , site_dict, 'routepattern.j2')
config.build_config(dir_path  + "translationpattern.csv" , site_dict, 'translationpattern.j2')
