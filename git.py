#!usr/bin/python3.7
#Author: KANG-NEWBIE
#Contact: t.me/kang_nuubi
try:
	from requests import get, post
	import json, os, subprocess as sp, sys
except Exception as ff:
	exit("[ModuleErr] %s"%(ff))
if sys.version[0] in '2':
   exit("[sorry] Kamu menggunakan python2 silahkan install python3")
os.system('clear')
print("""
  __ ___ ___    _     _        _ 
 /__  |   |    /  |  / \ |\ | |_ 
 \_| _|_  |    \_ |_ \_/ | \| |_ 
                                 """)
try:
	u=input("[!] input username github: ")
	if u == '':
		exit("[?] anda waras")
	print()
	re=get('https://api.github.com/users/'+u+'/repos')
	a=json.loads(re.text)
except Exception as ef:
	exit("[Err] %s"%(ef))

items = []
try:
	for item in a:
	    items.append(item['name'])
except TypeError: exit("[user:Not Found] username tidak ada")

s=len(items)
if s <= 0:
	exit("[repo:Not Found] username tersebut tidak memiliki repostory apapun")
elif s > 0:
	print("[!] found:",s,"repostory")

c=int(1)
while c < s:
	for i in range(s):
		print("\t["+str(c)+"] Clone",items[i])
		c+=1
try:
	asu=int(input("\n[?] Clone yang mana: "))
	if asu <= 0:
		exit("[?] anda waras")
	os.system('git clone https://github.com/'+u+'/'+items[asu-1])
	sp.call('mv '+str(items[asu-1])+' ..',shell=True,stdout=sp.DEVNULL, stderr=sp.STDOUT)
	print("[!] success installed",items[asu-1])
	print("[!] check the folder type 'cd'")
except KeyboardInterrupt: exit("[!] key interrupt: exit")
except Exception as F: exit("[?: anda waras] %s"%(F))
