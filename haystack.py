# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 00:48:44 2016

@author: eduardo
"""

import requests
import json

host_url = 'http://challenge.code2040.org/api/haystack'
return_url = 'http://challenge.code2040.org/api/haystack/validate'
tokenID = "45759240b3a76d3cc0dd0655eabbf28d"
github_url = 'https://github.com/etorresmontano/code2040-Tech-Assessment'

payload = {'token':tokenID}

r = requests.post(host_url, data=payload)
dictionary = r.json()
needle = dictionary['needle']
index = 0
count =0
for string in dictionary['haystack']:
    if(string == needle):
        index = count
    count = count + 1

return_payload = {'token':tokenID, 'needle':index}

r = requests.post(return_url, data=return_payload)
print r.text