import numpy as np

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)

X = X/np.amax(X, axis=0)
y = y/100


class NeuralNetwork(object):
    def __init__(self):
        self.inp = 2
        self.hid = 3
        self.out = 1
        self.W1 = np.random.randn(self.inp, self.hid)
        self.W2 = np.random.randn(self.hid, self.out)
        # print(f'initial Guess (RANDOMIZED) : \n{self.W1=}\n{self.W2=}')

    def feedForward(self, X):
        self.z = np.dot(X, self.W1)
        self.z2 = self.sigmoid(self.z)
        self.z3 = np.dot(self.z2, self.W2)
        output = self.sigmoid(self.z3)
        return output

    def sigmoid(self, s, d=False):
        if d:
            return s * (1 - s)
        return 1/(1 + np.exp(-s))

    def backward(self, X, y, output):
        self.output_error = y - output
        self.output_delta = self.output_error * self.sigmoid(output, True)
        self.z2_error = self.output_delta.dot(self.W2.T)
        self.z2_delta = self.z2_error * self.sigmoid(self.z2, True)
        self.W1 += X.T.dot(self.z2_delta)
        self.W2 += self.z2.T.dot(self.output_delta)

    def train(self, X, y):
        output = self.feedForward(X)
        self.backward(X, y, output)


NN = NeuralNetwork()
for i in range(50000):
    if (i % 10000 == 0):
        print("Loss: " + str(np.mean(np.square(y - NN.feedForward(X)))))
    NN.train(X, y)

print("\nInput: " + str(X))
print("Actual Output: " + str(y))
print("Loss: " + str(np.mean(np.square(y - NN.feedForward(X)))))
print('-'*25)
print("Predicted Output: " + str(NN.feedForward(X)))
