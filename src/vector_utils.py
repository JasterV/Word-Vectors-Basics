import math
from functools import reduce

class Vector:
    @staticmethod
    def distance(v1, v2):
        return math.sqrt(sum((i - j)**2 for i, j in zip(v1, v2)))

    @staticmethod
    def add(*vecs):
        return [i + j for i, j in zip(*vecs)]

    @staticmethod
    def subs(*vecs):
        return [i - j for i, j in zip(*vecs)]

    @staticmethod
    def mean(*vecs):
        return [float(coord) / len(vecs) for coord in reduce(Vector.add, vecs)]
