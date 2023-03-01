from typing import Union


class Technik:
    __slots__ = ("name", "price", "available")

    def __init__(self, name: str, price: Union[int, float], available: bool):
        self.name = name
        self.price = price
        self.available = available

    def __str__(self) -> str:
        return f"{self.name} ({'available' if self.available else 'unavailable'}), price: {self.price}"

    @property
    def category(self) -> str:
        return 'budget' if self.price < 1000 else 'expensive'

    def __lt__(self, other) -> bool:
        return len(self.name) < len(other.name)

    def __eq__(self, other) -> bool:
        return len(self.name) == len(other.name)


t1 = Technik("Laptop", 1500, True)
t2 = Technik("Smartphone", 800, False)

print(t1)  # Laptop (available), price: 1500
print(t1.category)  # expensive
print(t2.category)  # budget
print(t2)  # Smartphone (available), price: 800
print(t2.category)

print(t1 < t2)  # True
print(t1 == t2)  # False
