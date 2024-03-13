"""
This module defines the constants used in the project.

It includes the following classes:
- State: An enumeration representing the possible states of a ticket.
- Responsible: An enumeration representing the possible responsible levels for a ticket.
- Type: An enumeration representing the possible types of a ticket.
"""

from enum import Enum


class State(Enum):
    """
    An enumeration representing the possible states of a ticket.

    The states include:
    - NEW
    - ASSIGNED
    - ANALYSIS
    - SOLVED
    - IN_DELIVERY
    - CLOSED
    """

    NEW = "new"
    ASSIGNED = "assigned"
    ANALYSIS = "analysis"
    SOLVED = "solved"
    IN_DELIVERY = "in_delivery"
    CLOSED = "closed"

    @classmethod
    def has_value(cls, value):
        """
        Checks if the given value is a valid state.

        :param value: The value to check.
        :return: True if the value is a valid state, False otherwise.
        """
        return value in cls._value2member_map_

    @classmethod
    def get_enum(cls, value):
        """
        Returns the enum member corresponding to the given value.

        :param value: The value to get the enum member for.
        :return: The enum member corresponding to the given value, or None if the value is not a valid state.
        """
        if value == "new":
            return cls.NEW
        if value == "assigned":
            return cls.ASSIGNED
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
    """
    An enumeration representing the possible responsible levels for a ticket.

    The levels include:
    - L1
    - L2
    - L3
    """

    L1 = "L1"
    L2 = "L2"
    L3 = "L3"

    @classmethod
    def has_value(cls, value):
        """
        Checks if the given value is a valid responsible level.

        :param value: The value to check.
        :return: True if the value is a valid responsible level, False otherwise.
        """
        return value in cls._value2member_map_

    @classmethod
    def get_enum(cls, value):
        """
        Returns the enum member corresponding to the given value.

        :param value: The value to get the enum member for.
        :return: The enum member corresponding to the given value, or None if the value is not a valid responsible level.
        """
        if value == "L1":
            return cls.L1
        if value == "L2":
            return cls.L2
        if value == "L3":
            return cls.L3
        return None


class Type(Enum):
    """
    An enumeration representing the possible types of a ticket.

    The types include:
    - PR
    - IR
    """

    PR = "PR"
    IR = "IR"

    @classmethod
    def has_value(cls, value):
        """
        Checks if the given value is a valid ticket type.

        :param value: The value to check.
        :return: True if the value is a valid ticket type, False otherwise.
        """
        return value in cls._value2member_map_

    @classmethod
    def get_enum(cls, value):
        """
        Returns the enum member corresponding to the given value.

        :param value: The value to get the enum member for.
        :return: The enum member corresponding to the given value, or None if the value is not a valid ticket type.
        """
        if value == "PR":
            return cls.PR
        if value == "IR":
            return cls.IR
        return None
