from enum import Enum

# BaseType Class define the type for skills and pokemons
class BaseType(Enum):
	UNDEFINED = 0
	FIRE = 1
	WATER = 2
	GRASS = 3
	ELECTRIC = 4
	NORMAL = 5
	ICE = 6
	POSION = 7
	FIGHTING = 8
	FLYTING = 9
	GROUND = 10
	PSYCHIC = 11
	ROCK = 12
	BUG = 13
	DROGAN = 14
	GHOST = 15
	DARK = 16
	STEEL = 17
	FAIRY = 18

class BaseAttribute(Enum):
	ATTACK = 0
	DEFENSE = 1
	SPECIAL_ATTACK = 2
	SPECIAL_DEFENSE = 3
	SPEED = 4
	HEALTH = 5

