from sython3.Core.Interpreter import Interpreter

import sys


def main():
    if len(sys.argv) == 1:
        Interpreter().repl()
    else:
        if ".sy" not in sys.argv[1]:
            print("Erreur : Mauvaise extension de fichier. Faites 'python Sython3.py <file>.sy'")
        else:
            with open(sys.argv[1], "r") as f:
                text = f.read()
            Interpreter().execute(text)


if __name__ == "__main__":
    main()
