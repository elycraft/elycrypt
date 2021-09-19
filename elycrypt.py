#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:33:07 2021
@author: Elycraft
"""
import random
import string
from termcolor import cprint
import argparse

class Key():
	def __init__(self,serializeKey=None,keyNTB=3,keySPP=10,keyCESARD=3,keySYM_TONUM="$",keySYM_SPLIT="@@@@@"):

		self.version = "1.0"

		self.serializeKey = serializeKey

		self.keyNTB = keyNTB
		self.keySPP = keySPP
		self.keyCESARD = keyCESARD
		self.keySYM_TONUM = keySYM_TONUM
		self.keySYM_SPLIT = keySYM_SPLIT
	
	def keySerialization(self):
		u = []
		u.append(self.version)
		u.append(self.keyNTB)
		u.append(self.keySPP)
		u.append(self.keyCESARD)
		u.append(self.keySYM_TONUM)
		u.append(self.keySYM_SPLIT)
		return "|".join([str(i) for i in u])

	def keyDeserialization(self):
		y = self.serializeKey.split("|")
		self.version = y[0]
		self.keyNTB = int(y[1])
		self.keySPP = int(y[2])
		self.keyCESARD = int(y[3])
		self.keySYM_TONUM = y[4]
		self.keySYM_SPLIT = y[5]

class Encryptor():
	def __init__(self) -> None:
		pass

	def tonum(self,m,encode,sym="$"):
		u = []
		if encode:
			for p in m:
				u.append(str(ord(str(p))))
			return sym.join(u)
		else:
			y = m.split(sym)
			for i in y:
				u.append(str(chr(int(i))))
			return "".join(u)

	def split_de(self,m,encode,sym="@@@@@"):

		def insert_string(string,repl, index):
			return string[:index] + repl + string[index:]
			
		if encode:
			l = m
			e = 0
			for i in range(len(m)):
				if random.randint(0,10) == 0:
					l = insert_string(l,sym,i+e)
					e += len(sym)
				
			return l
		else:
			return "".join(m.split(sym))
			
	def cesar(self,m,encode,dec):
		JEUCAR = string.printable[:-5]
		CARBUSTI = JEUCAR[-dec:] + JEUCAR[:-dec]
		
		DICO_ENCRYP = {}
		DICO_DECRYPT = {}
		
		for i,k in enumerate(JEUCAR):
			v = CARBUSTI[i]
			DICO_ENCRYP[k] = v
			DICO_DECRYPT[v] = k
			
		#for c in string.printable[:-5]:
		#	DICO_ENCRYP[c] = c
		#	DICO_DECRYPT[c] = c
		
		#print(DICO_ENCRYP,DICO_DECRYPT)
			
		if encode:
			retour = []
			for k in m:
				v =  DICO_ENCRYP[k]
				retour.append(v)
			return "".join(retour)	
		else:
			retour = []
			for k in m:
				v =  DICO_DECRYPT[k]
				retour.append(v)
			return "".join(retour)	

	def fencode(self,m,key):
		m = self.tonum(m,True,key.keySYM_TONUM)
		for i in range(0,key.keyNTB):
				m = self.split_de(m,True,key.keySYM_SPLIT)
				m = self.cesar(m,True,key.keyCESARD)
		return m

	def fdecode(self,m,key):
		for i in range(0,key.keyNTB):
				m = self.cesar(m,False,key.keyCESARD)
				m = self.split_de(m,False,key.keySYM_SPLIT)
		m = self.tonum(m,False,key.keySYM_TONUM)
		return m

def cmd():
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

if __name__ == "__main__":

	my_parser = argparse.ArgumentParser()
	my_parser.add_argument('-eS', action='store', type=str)
	my_parser.add_argument('-eF', action='store', type=str)
	my_parser.add_argument('-dS', action='store', type=str)
	my_parser.add_argument('-dF', action='store', type=str)
	my_parser.add_argument('-k', action='store', type=str)
	my_parser.add_argument('-o', action='store', type=str)
	args = my_parser.parse_args()
	isargs = False
	if args.eS or args.eF or args.dS or args.dF or args.o or args.k:
		isargs = True
	if not isargs:
		cmd()
		exit()
	
	if args.eS:
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

	if args.dS:
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

	if args.eF:
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

	if args.dF:
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