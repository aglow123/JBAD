from math import sqrt
import numpy as np


class KNN:

    def __init__(self, dataset):
        self.train_dataset = []  # lista?
        self.train(dataset)

    def train(self, data_to_train):
        self.train_dataset.extend(data_to_train)
        
    def predict(self, data_to_predict, k, type_of_distance=0):
        if type_of_distance not in range(4):  # a gdyby użyć enuma? albo przekazać funkcję?
            raise ValueError('wrong type_of_distance value')

        if type_of_distance == 0:
            type_of_distance = self.euclidean_distance
        elif type_of_distance == 1:
            type_of_distance = self.taxicab_dictance
        elif type_of_distance == 2:
            type_of_distance = self.chebyshev_distance
        elif type_of_distance == 3:
            type_of_distance = self.cosine_distance
        predictions = []
        for test_row in data_to_predict:
            distances = np.array([])
            for train_row in self.train_dataset:
                distances = np.append(distances, [train_row[-1], type_of_distance(train_row, test_row)])  # append zabija sens używania numpy'a
            distances = distances.reshape(-1, 2)
            distances = distances[np.argsort(distances[:, -1])][:k, :1]
            values, counts = np.unique(distances, return_counts=True)
            predictions.append(values[np.argmax(counts)])
        return predictions

    def euclidean_distance(self, train_row, test_row):  # do przemyślenia, czy nie lepiej z tego zrobić funkcję
        distance = 0.0
        for i in range(len(train_row) - 1):  # nie dałoby się uniknąć tej pętli?
            distance += (train_row[i] - test_row[i]) ** 2
        return sqrt(distance)

    def taxicab_dictance(self, train_row, test_row):
        distance = 0.0
        for i in range(len(train_row) - 1):
            distance += abs(train_row[i] - test_row[i])
        return distance

    def chebyshev_distance(self, train_row, test_row):
        distance = 0.0
        for i in range(len(train_row) - 1):
            if distance < abs(train_row[i] - test_row[i]):  # woła o pomstę
                distance = abs(train_row[i] - test_row[i])
        return distance

    def cosine_distance(self, train_row, test_row):
        return np.dot(train_row[:-1], test_row) / (np.linalg.norm(train_row[:-1]) + np.linalg.norm(test_row))  # 1-


sample = KNN([[2.7810836, 2.550537003, 0],
              [1.465489372, 2.362125076, 0],
              [3.396561688, 4.400293529, 0],
              [1.38807019, 1.850220317, 0],
              [3.06407232, 3.005305973, 0],
              [7.627531214, 2.759262235, 1],
              [5.332441248, 2.088626775, 1],
              [6.922596716, 1.77106367, 1]])

sample.train([[8.675418651, -0.242068655, 1],
              [7.673756466, 3.508563011, 1]])

print(sample.predict([[2.5, 2.5], [5.3, 2.0]], 5, 2))
