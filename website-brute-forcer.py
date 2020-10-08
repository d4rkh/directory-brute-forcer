import socket
import sys
import requests

target = sys.argv[1]
wordlist = sys.argv[2]

try:	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target, 80))

except:
	print("[!] Can't Connect To Target : " + target)
	sys.exit()

try:
	with open(wordlist, 'r') as file:
		wlst = file.read().strip().split()

except:
	print('[!] can not read wordlist!')

def checkpath(path):
	try:
		response = requests.get('http://' + target + '/' + path).status_code
	
	except Exception:
		print('[!] Error : An Unexpected Error Occured')
		sys.exit()

	if response == 200:
		print('[*] Valid Path Found : ' + path)

try:
	print('\n[*] Beginning Scan...\n')
	for i in range(len(wlst)):
		checkpath(wlst[i])

except KeyboardInterrupt:
	print('\n [!] Error : User Interrupted Scan')
	sys.exit()	