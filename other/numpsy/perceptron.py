from random import random
from other.numpsy.perceptron import generate_data
import numpy as np


class Perceptron:

    def __init__(self, dimensions):
        self.bias = 0
        self.weights = np.array([random() for _ in range(dimensions)])

    def predict(self, x):
        return 1* ((x*self.weights).sum(axis=1) + self.bias > 0)

    def train(self, X, Y, maxIter):
        for i in range(maxIter):
            for x, y in zip(X, Y):
                act = self.predict(x)
                if y*act <= 0:
                    self.weights += y*x
                    self.bias += y


def decision(sample, weights, theta):
    z = (sample * weights).sum()
    if z >= theta:
        return 1
    else:
        return -1


x, y = generate_data(10, 10, 1)
print('x\n', x, '\ny\n', y)
