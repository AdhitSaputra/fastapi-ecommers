from enum import Enum

class IGenderEnum(str, Enum):
    female = "female"
    male = "male"
    other = "other"