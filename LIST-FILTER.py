#!/usr/bin/python
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
import time

# ( -- LOGO * INFO -- ) #
bugs = '''
   ____  _     ___ ____ _____     _____ ___ _   _____ _____ ____  
  / __ \| |   |_ _/ ___|_   _|   |  ___|_ _| | |_   _| ____|  _ \ 
 / / _` | |    | |\___ \ | |_____| |_   | || |   | | |  _| | |_) |
| | (_| | |___ | | ___) || |_____|  _|  | || |___| | | |___|  _ < 
 \ \__,_|_____|___|____/ |_|     |_|   |___|_____|_| |_____|_| \_\
  \____/                                                          
\n [$] BUGS LIST DOMAINS FIL9ER.
 [$] URL = ('https://www.Brazzers.com/').
 [$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''
#################################
# ( -- PROGRAMMED BY @BUGS -- ) #
#################################

										# ( -- FULL API SCRIPT -- ) #
# -------------------------------- ## --------------------------------- ## -------------------------------- #
print bugs
# -------------------------------- ## --------------------------------- ## -------------------------------- #
list = raw_input(' [X] ENTER YOUR LIST PATH .TXT X> ')
# -------------------------------- ## --------------------------------- ## -------------------------------- #
print ' [X] SCRIPT STARTED NOW .. \n'; time.sleep(1)
# -------------------------------- ## --------------------------------- ## -------------------------------- #

for email in open(list, 'r'):
	email = email.strip()
	if '@gmail' in email:
		gmail = open('gmail.txt','a+')
		gmail.write(email + '\n')
		gmail.close()
		print '[GMAIL] ',email
	elif '@yahoo' in email:
		yahoo = open('yahoo.txt','a+')
		yahoo.write(email + '\n')
		yahoo.close()
		print '[YAHOO] ',email
	elif '.ru' in email:
		ru = open('ru.txt','a+')
		ru.write(email + '\n')
		ru.close()
		print '[RU] ',email
	elif '@aol' in email:
		aol = open('aol.txt','a+')
		aol.write(email + '\n')
		aol.close()
		print '[AOL] ',email
	elif '@hotmail' in email:
		hotmail = open('hotmail.txt','a+')
		hotmail.write(email + '\n')
		hotmail.close()
		print '[HOTMAIL] ',email
	elif '@outlook' in email:
		outlook = open('outlook.txt','a+')
		outlook.write(email + '\n')
		outlook.close()
		print '[OUTLOOK] ',email
	elif '.cz' in email:
		cz = open('cz.txt','a+')
		cz.write(email + '\n')
		cz.close()
		print '[CZ] ',email
	elif '@edu' in email:
		edu = open('edu.txt','a+')
		edu.write(email + '\n')
		edu.close()
		print '[EDU] ',email
	else:
		others = open('others.txt','a+')
		others.write(email + '\n')
		others.close()
		print '[OTHERS] ',email
print '[X] DONE SUCCESSFUL ', len(open(list, 'r').readlines()), ' .'