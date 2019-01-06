from enum import Enum
from PokemonObject.Pokemon import Pokemon as pm
from PokemonObject.CommonInterface import BaseType
from PokemonObject.CommonInterface import IndividualValues

class TestPokemons():

    def test_Gardevior(self):
        Gardevior = pm
        Gardevior.index= "111"
        Gardevior.pokemonName = "Gardevior"
        Gardevior.pokemonType = BaseType.UNDEFINED
        assert "111" == Gardevior.index
        assert "Gardevior" ==  Gardevior.pokemonName

    def test_Pikachu(self):
        Pikachu = pm
        Pikachu.index= "025"
        Pikachu.pokemonName = "Pikachu"
        Pikachu.pokemonType = BaseType.ELECTRIC
        assert "Pikachu" == Pikachu.pokemonName
        assert BaseType.ELECTRIC == Pikachu.pokemonType
