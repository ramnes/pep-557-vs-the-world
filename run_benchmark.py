from importlib import import_module
from line_profiler import LineProfiler

names = ("attr", "box", "dict", "dataclass", "namedtuple", "simplenamespace",
         "thingy", "typednamedtuple")

for name in names:
    module = import_module(f"with_{name}")
    print(f"Using {name}:")
    total_cost, dict_repr, instance_repr = module.benchmark()
    print(f"- total cost: {total_cost}")
    print(f"- dict representation: {dict_repr}")
    print(f"- instance representation: {instance_repr}")
    print()

for name in names:
    lp = LineProfiler()
    module = import_module(f"with_{name}")
    for i in range(1000):
        lp(module.benchmark)()
    lp.print_stats()
