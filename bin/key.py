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
File: key.py

Note:
"""

## Classes

class Key():
	"""
	The Key of the encryption/decryption. It's a object with :
	self.keySerialization --> Return a string with the key serialize
	self.keyDeserialization --> Use the self.serializeKey for deserialize the key
	"""
	
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