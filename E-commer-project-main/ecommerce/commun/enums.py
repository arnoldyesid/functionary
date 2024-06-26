from enum import Enum, unique


@unique
class OrderStatus(Enum):
    """Class for enums of order status"""

    DELAYED = "DELAYED"
    CREATED = "CREATED"

    @staticmethod
    def values():
        return list(map(lambda e: e.value, OrderStatus))
