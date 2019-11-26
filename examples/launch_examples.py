import os

print("BEGIN TESTS")
path = os.path.dirname(__file__)
for i in ("comparaison.sy", "operations.sy", "print.sy", "conditions.sy", "input.sy", "loop.sy", "complex_types.sy"):
    print("\n"+i)
    os.system("python ../sython3/Sython.py "+os.path.join(path, i))
print("\nEND TESTS")