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
File: elycrypt.py

Note: Hey GCA =)
"""

## Imports

# Libraries
from termcolor import cprint
import argparse

# Project Files
from bin.key import Key
from bin.encryptor import Encryptor
from bin.cmd import Cmd

## Main

if __name__ == "__main__":

	argParser = argparse.ArgumentParser()

	argParser.add_argument('-eS', action='store', type=str) # Add args to the parser...
	argParser.add_argument('-eF', action='store', type=str)
	argParser.add_argument('-dS', action='store', type=str)
	argParser.add_argument('-dF', action='store', type=str)
	argParser.add_argument('-k', action='store', type=str)
	argParser.add_argument('-o', action='store', type=str)

	args = argParser.parse_args() # Parse...

	isargs = False #Decide to execute cmd or print directly
	if args.eS or args.eF or args.dS or args.dF or args.o or args.k:
		isargs = True
	if not isargs:
		Cmd()
		exit()
	
	if args.eS: #Encryption From String
		if args.k:
			myKey = Key(args.k)
			myKey.keyDeserialization()
		else:
			myKey = Key()
		encrypt = Encryptor()
		z = encrypt.fencode(args.eS,myKey)
		if args.o:
			with open(args.o,"w") as filename:
				filename.write(z)
			exit()
		cprint(z,color="green")
		exit()

	if args.dS: #Decryption From String
		if args.k:
			myKey = Key(args.k)
			myKey.keyDeserialization()
		else:
			myKey = Key()
		encrypt = Encryptor()
		z = encrypt.fdecode(args.dS,myKey)
		if args.o:
			with open(args.o,"w") as filename:
				filename.write(z)
			exit()
		cprint(z,color="green")
		exit()

	if args.eF: #Encryption From File
		if args.k:
			myKey = Key(args.k)
			myKey.keyDeserialization()
		else:
			myKey = Key()
		encrypt = Encryptor()
		with open(args.eF,"r") as filename:
			temp = filename.read()
		z = encrypt.fencode(temp,myKey)
		if args.o:
			with open(args.o,"w") as filename:
				filename.write(z)
			exit()
		cprint(z,color="green")
		exit()

	if args.dF: #Decryption From File
		if args.k:
			myKey = Key(args.k)
			myKey.keyDeserialization()
		else:
			myKey = Key()
		encrypt = Encryptor()
		with open(args.dF,"r") as filename:
			temp = filename.read()
		z = encrypt.fdecode(temp,myKey)
		if args.o:
			with open(args.o,"w") as filename:
				filename.write(z)
			exit()
		cprint(z,color="green")
		exit()