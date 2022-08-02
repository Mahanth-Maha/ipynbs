import numpy as np

data = [['outlook', 'temp', 'humidity', 'windy', 'play'],
        ['sunny', 'hot', 'high', 'Weak', 'no'],
        ['sunny', 'hot', 'high', 'Strong', 'no'],
        ['overcast', 'hot', 'high', 'Weak', 'yes'],
        ['rainy', 'mild', 'high', 'Weak', 'yes'],
        ['rainy', 'cool', 'normal', 'Weak', 'yes'],
        ['rainy', 'cool', 'normal', 'Strong', 'no'],
        ['overcast', 'cool', 'normal', 'Strong', 'yes'],
        ['sunny', 'mild', 'high', 'Weak', 'no'],
        ['sunny', 'cool', 'normal', 'Weak', 'yes'],
        ['rainy', 'mild', 'normal', 'Weak', 'yes'],
        ['sunny', 'mild', 'normal', 'Strong', 'yes'],
        ['overcast', 'mild', 'high', 'Strong', 'yes'],
        ['overcast', 'hot', 'normal', 'Weak', 'yes'],
        ['rainy', 'mild', 'high', 'Strong', 'no']]

splitRatio = 0.75
trainSize = int(len(data[1:]) * splitRatio)
trainset = []
testset = list(data[1:])
i = 0
while len(trainset) < trainSize:
    trainset.append(testset.pop(i))
train = np.array(trainset)
test = np.array(testset)

print(f'Spliting @{splitRatio} results\n{train.shape=}\n{test.shape=}')

train_rows = train.shape[0]
test_rows = test.shape[0]
cols = train.shape[1]

countYes = 0
countNo = 0
probYes = 0
probNo = 0

for x in range(train_rows):
    if train[x, cols-1] == 'yes':
        countYes += 1
    if train[x, cols-1] == 'no':
        countNo += 1

probYes = countYes/train_rows
probNo = countNo/train_rows

print(f'\nProbabilites of train dataset\n{probYes=}\n{probNo=}')

acc = 0
print(f'\nSEQ\t\t  RESULT\t  PREDICTED')
for i in range(test_rows):
    p0 = np.zeros(cols-1)
    p1 = np.zeros(cols-1)
    for j in range(cols - 1):
        c0 = 0
        c1 = 0
        for k in range(train_rows):
            if test[i, j] == train[k, j] and train[k, -1] == 'yes':
                c1 += 1
            elif test[i, j] == train[k, j] and train[k, -1] == 'no':
                c0 += 1
        p0[j] = c0/probNo
        p1[j] = c1/probYes
    p02 = probNo
    p12 = probYes
    for q in range(cols-1):
        p02 *= p0[q]
        p12 *= p1[q]
    if p12 > p02:
        res = 'yes'
    else:
        res = 'no'
    print(f'{i+1}\t\t  {test[i,cols-1]}\t\t  {res}')
    if test[i, cols-1] == res:
        acc += 1

print('\nACCURACY : ', 100 * acc/test_rows, '%')
