# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 01:15:41 2016

@author: eduardo
"""

import requests
import json
import datetime
from datetime import timedelta

host_url = 'http://challenge.code2040.org/api/dating'
return_url = 'http://challenge.code2040.org/api/dating/validate'
tokenID = "45759240b3a76d3cc0dd0655eabbf28d"
github_url = 'https://github.com/etorresmontano/code2040-Tech-Assessment'

payload = {'token':tokenID}

r = requests.post(host_url, data=payload)
dictionary = r.json()
interval_seconds = dictionary['interval']

#split up date and time for easier formating
date = dictionary['datestamp'].split('T')[0].split('-')
time = dictionary['datestamp'].split('T')[1].split(':')

#create a datetime object, minus time zone information. split the second portion to get rid of 'Z'
stamp = datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]), int(time[2][0:2]))

#add time to date
stampy = stamp + timedelta(seconds = int(interval_seconds))

#python does not include tz info in the format needed
dating = str(stampy.isoformat()) + time[2][2]

payload = {'token':tokenID, 'datestamp':dating}

r = requests.post(return_url, data=payload)
print r.text

