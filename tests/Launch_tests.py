import os

files = [i for i in os.listdir(".") if i not in ["launch_tests.py"] and i.endswith(".py")]
os.system("python -m unittest -v "+" ".join(files))
