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
File: encryptor.py

Note:
"""

## Imports

# Libraries
import string, random

## Classes

class Encryptor():
	"""
	The object that deal with the process of encryption/decryption. Methods :
	self.fencode --> Encode a string, need a Key Object
	self.fdecode --> Decode a string, need a Key Object
	"""
    
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