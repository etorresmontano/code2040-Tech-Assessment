# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 23:56:27 2016

@author: eduardo
"""

import requests
import json

host_url = 'http://challenge.code2040.org/api/reverse'
tokenID = "45759240b3a76d3cc0dd0655eabbf28d"
github_url = 'https://github.com/etorresmontano/code2040-Tech-Assessment'

payload = {'token':tokenID}

r = requests.post(host_url, data=payload)
string = r.text
reverse_string = ""

#builds string backwards by continuously appending new characters to the front, making the first character last and so on.
for char in string:
    reverse_string = char + reverse_string

return_payload = {'token':tokenID, 'string':reverse_string}
return_url = 'http://challenge.code2040.org/api/reverse/validate'


r = requests.post(return_url, data=return_payload)
print r.text
