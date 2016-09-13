# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 02:58:50 2016

@author: eduardo
"""

import requests
import json

host_url = 'http://challenge.code2040.org/api/register'
tokenID = "45759240b3a76d3cc0dd0655eabbf28d"
github_url = 'https://github.com/etorresmontano/code2040-Tech-Assessment'

payload = {'token':tokenID, 'github':github_url}

r = requests.post(host_url, data=payload)

#verify response status
print r.text 