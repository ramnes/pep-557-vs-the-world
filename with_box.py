def benchmark():
    from box import Box

    class InventoryItem(Box):
        @property
        def total_cost(self) -> float:
            return self.unit_price * self.quantity

    item = InventoryItem(name="hammer", unit_price=10.49, quantity=12)
    total_cost = item.total_cost
    item_dict = item.to_dict()

    for i in range(50):
        item = InventoryItem(item_dict)
        item.total_cost

    return total_cost, item_dict, item


if __name__ == "__main__":
    benchmark()
