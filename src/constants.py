from enum import Enum


class State(Enum):
    NEW = "new"
    ANALYSIS = "analysis"
    SOLVED = "solved"
    IN_DELIVERY = "in_delivery"
    CLOSED = "closed"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class Responsible(Enum):
    L1 = "L1"
    L2 = "L2"
    L3 = "L3"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class Type(Enum):
    PR = "PR"
    IR = "IR"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    @classmethod
    def get_enum(cls, value):
        if value == "PR":
            return cls.PR
        if value == "IR":
            return cls.IR
        return None
