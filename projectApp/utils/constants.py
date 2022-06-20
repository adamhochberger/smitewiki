import enum


class ItemTypes(enum.Enum):
    PHYSICAL = "physical"
    MAGICAL = "magical"
    NEUTRAL = "neutral"


class ClassTypes(enum.Enum):
    ASSASSIN = "assassin"
    GUARDIAN = "guardian"
    HUNTER = "hunter"
    MAGE = "mage"
    WARRIOR = "warrior"
