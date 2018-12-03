
from enum import Enum
from CommonInterface import BaseType


# skill type
# There  are more subtype, such as powder, weather change, not take into consideration so far
class SkillType(Enum):
	UNDEFINED = 0
	SPECIAL = 1
	PYHSICAL = 2
	STATUSMOVE = 3

# status change
class Status(Enum):
	NORMAL = 0
	BURN = 1
	POSION = 2
	CONFUSE = 3
	PARALYZE = 4
	SLEEP = 5
	FREEZE = 6
	SCARED = 7


class SkillBase():
	def __init__(self):
		self.skillName = ""
		self.skillType = BaseType.UNDEFINED
		self.hitRate = 1 # 0-100%
		self.sequence = 0

#inheretence skill base type for 3 kind of skill type