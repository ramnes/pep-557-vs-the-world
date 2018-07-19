def benchmark():
    import attr

    @attr.s
    class InventoryItem:
        name: str = attr.ib()
        unit_price: float = attr.ib()
        quantity: int = attr.ib(default=0)

        @property
        def total_cost(self) -> float:
            return self.unit_price * self.quantity

    item = InventoryItem("hammer", 10.49, 12)
    total_cost = item.total_cost
    item_dict = attr.asdict(item)

    for i in range(50):
        item = InventoryItem(**item_dict)
        item.total_cost

    return total_cost, item_dict, item


if __name__ == "__main__":
    benchmark()
