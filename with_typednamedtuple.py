def benchmark():
    from typing import NamedTuple

    class InventoryItem(NamedTuple):
        name: str
        unit_price: float
        quantity: int = 0
        # note: that wouldn't be a good idea with mutable types

        @property
        def total_cost(self) -> float:
            return self.unit_price * self.quantity

    item = InventoryItem("hammer", 10.49, 12)
    total_cost = item.total_cost
    item_dict = item._asdict()

    for i in range(50):
        item = InventoryItem(**item_dict)
        item.total_cost

    return total_cost, item_dict, item


if __name__ == "__main__":
    print(benchmark())
