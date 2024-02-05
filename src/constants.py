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

    @classmethod
    def get_enum(cls, value):
        if value == "new":
            return cls.NEW
        if value == "analysis":
            return cls.ANALYSIS
        if value == "solved":
            return cls.SOLVED
        if value == "in_delivery":
            return cls.IN_DELIVERY
        if value == "closed":
            return cls.CLOSED
        return None


class Responsible(Enum):
    L1 = "L1"
    L2 = "L2"
    L3 = "L3"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    @classmethod
    def get_enum(cls, value):
        if value == "L1":
            return cls.L1
        if value == "L2":
            return cls.L2
        if value == "L3":
            return cls.L3
        return None


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
