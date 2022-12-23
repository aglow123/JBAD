import numpy as np
from perceptron.generator import generate_data


def true_values(correct, test):
    return np.count_nonzero((correct == test) == 'True')


def tp(correct, test):
    return np.count_nonzero(correct * test == 1)


def tn(correct, test):
    return true_values(correct, test) - tp(correct, test)


def fp(correct, test):
    return np.count_nonzero(test == 1) - tp(correct, test)


def fn(correct, test):
    return np.count_nonzero(test == 1) - tn(correct, test)


def accuracy(correct, test):
    return (tp(correct, test) + tn(correct, test))/(tp(correct, test) + tn(correct, test) + fp(correct, test) + fn(correct, test))


def precision(correct, test):
    return tp(correct, test)/(tp(correct, test) + fp(correct, test))


def recall(correct, test):
    return tp(correct, test)/(tp(correct, test) + fn(correct, test))


def decision(sample, weights, theta):
    z = (sample * weights).sum()
    if z >= theta:
        return 1
    else:
        return -1


x, y = generate_data(10, 10, 1)
print('x\n', x, '\ny\n', y)
