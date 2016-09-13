# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 00:58:09 2016

@author: eduardo
"""

import requests
import json
import array

host_url = 'http://challenge.code2040.org/api/prefix'
return_url = 'http://challenge.code2040.org/api/prefix/validate'
tokenID = "45759240b3a76d3cc0dd0655eabbf28d"
github_url = 'https://github.com/etorresmontano/code2040-Tech-Assessment'

payload = {'token':tokenID}

r = requests.post(host_url, data=payload)

dictionary = r.json()
prefix = dictionary['prefix']
return_array = []

for string in dictionary['array']:
    if(string.find(prefix) != 0):
        return_array.append(str(string))
    print string
print return_array
print r
return_payload = {'token':tokenID, 'array':return_array}       
print json.dumps(return_payload)
headers = {'content-type': 'application/json'}

#expected output is a string array, not list. Need to convert from python list to json object and changed request header.
r = requests.post(return_url, data = json.dumps(return_payload), headers = headers)
print r.text