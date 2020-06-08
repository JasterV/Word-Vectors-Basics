import math
from functools import reduce
import operator

class Vector:
    @staticmethod
    def distance(v1, v2):
        return math.sqrt(sum((i - j)**2 for i, j in zip(v1, v2)))

    @staticmethod
    def add(*vecs):
        return [sum(t) for t in zip(*vecs)]

    @staticmethod
    def subtract(*vecs):
        return [reduce(operator.__sub__, t) for t in zip(*vecs)]

    @staticmethod
    def mean(*vectors):
        return [float(coord) / len(vectors) for coord in reduce(Vector.add, vectors)]



