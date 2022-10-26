import base64

for i in range(99):
	for x in range(99):
		print 'O:8:"userdata":3:{s:4:"role";s:4:"user";s:2:"id";i:' + str(i) + ';s:3:"uid";i:'+ str(x) +';}'


with open('3rd.txt','r') as lines: 
	for line in lines:
		print(base64.b64encode(line))


with open('3rd_base64.txt','r') as lines:
	for line in lines:
		print(line[:128])
