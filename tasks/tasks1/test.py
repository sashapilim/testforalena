from collections import defaultdict
from typing import Tuple, List

technic = [("Ноутбук", 1500, "Татьяна", "89002001020"),
           ("Ноутбук", 4500, "Татьяна", "89002001020"),
           ("Смартфон", 500, "Анна", "89002001022"),
           ("Планшет", 1200, "Анна", "89002001022"),
           ("Принтер", 750, "Игорь", "89303303236"),
           ("Планшет", 2300, "Игорь", "89303303236")]


def service_center(technic: List[Tuple[str, int, str, str]]) -> None:
    customers = defaultdict(list)
    for tech, price, name, phone in technic:
        customers[(name, phone)].append((tech, price))

    for (name, phone), techs in customers.items():
        techs_str = "; ".join(f"{tech}-{price}" for tech, price in techs)
        print(f"{name} {phone}:{techs_str}")
