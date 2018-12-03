
from enum import Enum
from CommonInterface import BaseType

class Pokemon():
	def __init__(self):
		self.pokemonName  = ""
		self.index = 0
		self.pokemonType = BaseType.UNDEFINED





#test
Gardevior = Pokemon()
Gardevior.index= 111
Gardevior.pokemonName = "Gardevior"
Gardevior.pokemonType = BaseType.UNDEFINED

print(Gardevior.pokemonName)
