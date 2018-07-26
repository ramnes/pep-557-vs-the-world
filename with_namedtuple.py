def benchmark():
    from collections import namedtuple

    InventoryItem = namedtuple("InventoryItem", ["name", "unit_price", "quantity"])
    # note: you can't have defaults, nor properties

    item = InventoryItem("hammer", 10.49, 12)
    total_cost = item.unit_price * item.quantity
    item_dict = item._asdict()

    for i in range(50):
        item = InventoryItem(**item_dict)
        item.unit_price * item.quantity

    return total_cost, item_dict, item


if __name__ == "__main__":
    print(benchmark())
