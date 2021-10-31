# -*- coding: utf-8 -*-

"""
 _____ _       _____                  _   
|  ___| |     /  __ \                | |  
| |__ | |_   _| /  \/_ __ _   _ _ __ | |_ 
|  __|| | | | | |   | '__| | | | '_ \| __|
| |___| | |_| | \__/\ |  | |_| | |_) | |_ 
\____/|_|\__, |\____/_|   \__, | .__/ \__|
          __/ |            __/ | |        
         |___/            |___/|_|        

By ElyDev#1124
File: cmd.py

Note:
"""

## Imports

# Libraries
from termcolor import cprint

# Project Files
from key import Key
from encryptor import Encryptor

## Functions

def Cmd():
	"""
	If you don't use arguments in bash, you can simply type "elycrypt" and this fonction is call.
	"""

	cprint("Key > ",color="red",end="")
	j = input()
	if j:
		myKey = Key(j)
		myKey.keyDeserialization()
	else:
		myKey = Key()
	
	cprint("\nYour current key is %s\n" %myKey.keySerialization(),color="yellow")

	encrypt = Encryptor()

	while True:
		cprint("Encode? (y,n) > ",color="blue",end="")
		k = input()
		
		if k == "y":
			cprint("> ",color="blue",end="")
			z = input()
			z = encrypt.fencode(z,myKey)
			cprint("\n"+z+"\n",color="green")

		elif k == "n":
			cprint("> ",color="blue",end="")
			z = input()
			z = encrypt.fdecode(z,myKey)
			cprint("\n"+z+"\n",color="green")

		else:
			break