import itertools


def split(liste, mot, exclu=True):
    if exclu:
        return list(filter(
            lambda n: not isinstance(n[0], str) or (n[0].strip() != "" and n[0] != mot),
            map
                (
                lambda n: list(n[1]),
                itertools.groupby(liste, lambda word: isinstance(word, str) and word == mot)
            )
        ))
    else:
        return list(filter(
            lambda n: not isinstance(n[0], str) or (n[0].strip() != ""),
            map
                (
                lambda n: list(n[1]),
                itertools.groupby(liste, lambda word: isinstance(word, str) and word == mot)
            )
        ))