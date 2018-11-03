#!/usr/bin/python
import urllib2


class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


def banner():
	os.system('clear')
	file1 = open('banner', 'r')
	print(' ')
	print bcolors.OKGREEN + file1.read() + bcolors.ENDC
	file1.close()
	
	
def fblg():
	os.system('clear')
	print bcolors.OKGREEN + '''
	$$$$$$$$$$$$$$$$$$$$$$
	$$$$$$$$$$$$$_____$$$$
	$$$$$$$$$$$$__$$$$$$$$
	$$$$$$$$$$$$__$$$$$$$$
	$$$$$$$$$$$$__$$$$$$$$
	$$$$$$$$$________$$$$$
	$$$$$$$$$$$$__$$$$$$$$
	$$$$$$$$$$$$__$$$$$$$$
	$$$$$$$$$$$$__$$$$$$$$
	$$$$$$$$$$$$__$$$$$$$$
	$$$$$$$$$$$$$$$$$$$$$$
	''' + bcolors.ENDC


try:
	try:
		import requests
		import re
		import os
	except ImportError:
		print ('''There was an error
		Please install the requirements:
		pip install -r requirements.txt''')
		
	banner()
	url = raw_input(bcolors.WARNING + "[i]-Enter the Profile URL: " + bcolors.ENDC)
	idre = re.compile('"entity_id":"([0-9]+)"')
	page = requests.get(url)
	fblg()
	id = str(idre.findall(page.content))
	idp = id[2:-2]
	print bcolors.OKGREEN + "[+]-The Profile ID is: " + bcolors.ENDC + idp
	print bcolors.OKGREEN + "[+]-The Profile Picture: " + bcolors.ENDC + "https://graph.facebook.com/" + idp + "/picture?width=800"
except KeyboardInterrupt:
		print(bcolors.FAIL + '\nCancelled' + bcolors.ENDC)
