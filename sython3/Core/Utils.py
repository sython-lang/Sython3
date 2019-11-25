import itertools

from collections import deque, MutableSet


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


class Flattener(object):
    DEFAULT_FLATTEN_TYPES = (
        list,
        tuple,
        set,
        (x for x in ()).__class__,
        range,
        deque,
        MutableSet,
    )

    def __init__(self, flatten_types=None, iterable_getters={}):
        self.flatten_types = flatten_types or self.DEFAULT_FLATTEN_TYPES
        self.iterable_getters = iterable_getters

    def should_flatten(self, obj):
        return isinstance(obj, self.flatten_types)

    def transform_iterable(self, obj):
        if obj.__class__ in self.iterable_getters:
            return self.iterable_getters[obj.__class__](obj)
        return obj

    def __call__(self, iterable):
        for e in iterable:
            if self.should_flatten(e):
                for f in self(self.transform_iterable(e)):
                    yield f
            else:
                yield e


flattener = Flattener()
