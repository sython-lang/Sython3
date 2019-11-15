import os

print("BEGIN TESTS")
for i in ("comparaison.sy", "operations.sy", "print.sy"):
    print("\n"+i)
    os.system("python ../Sython.py "+i)
print("\nEND TESTS")