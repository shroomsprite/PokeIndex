
from enum import Enum
from PokemonObject.CommonInterface import BaseType
from PokemonObject.CommonInterface import IndividualValues

# We only need battle related data, but keep as
# much info as possible for the current stage
class Pokemon():
	def __init__(self):
		self.pokemonName = ""
		self.index = 0
		self.pokemonType = BaseType.UNDEFINED
		self.SkillList = []
		self.IVs = IndividualValues()

	def __init__(self, name =  "", index = 0, typ=BaseType.UNDEFINED, skillList=[], ivs=IndividualValues()):
		self.pokemonName  = name
		self.index = index
		self.pokemonType = typ
		self.SkillList = skillList
		self.IVs = ivs
	
	def get_pokemonName(self):
		return self.pokemonName
	
	def get_index(self):
		return self.index

#test
# Gardevior = Pokemon()
# Gardevior.index= 111
# Gardevior.pokemonName = "Gardevior"
# Gardevior.pokemonType = BaseType.UNDEFINED

# assert 111 == Gardevior.get_index()
# assert "Gar" == Gardevior.get_pokemonName()

# print(Gardevior.pokemonName)
