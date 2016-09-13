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
print r
dictionary = r.json()
print dictionary
interval_seconds = dictionary['interval']
date = dictionary['datestamp'].split('T')[0].split('-')
time = dictionary['datestamp'].split('T')[1].split(':')
print date
print time

stamp = datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]), int(time[2][0:2]))
print stamp
stampy = stamp + timedelta(seconds = int(interval_seconds))
dating = str(stampy.isoformat()) + "Z"

print type(dating)
payload = {'token':tokenID, 'datestamp':dating}
print payload

r = requests.post(return_url, data=payload)
print r.text

