from enum import Enum

class FeedingSideEnum(Enum):
    LEFT = "left_feeding"
    RIGHT = "right_feeding"
    BOTH = "both_feeding"

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]

class PumpingSideEnum(Enum):
    LEFT = "left_pump"
    RIGHT = "right_pump"
    BOTH = "both_pump"

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]
