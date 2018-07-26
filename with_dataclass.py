def benchmark():
    from dataclasses import dataclass, asdict

    @dataclass
    class InventoryItem:
        name: str
        unit_price: float
        quantity: int = 0

        @property
        def total_cost(self) -> float:
            return self.unit_price * self.quantity

    item = InventoryItem("hammer", 10.49, 12)
    total_cost = item.total_cost
    item_dict = asdict(item)

    for i in range(50):
        item = InventoryItem(**item_dict)
        item.total_cost

    return total_cost, item_dict, item


if __name__ == "__main__":
    print(benchmark())
