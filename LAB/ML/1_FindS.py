data = [['outlook', 'temp', 'humidity', 'wind', 'Water', 'Forecast', 'play'],
        ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
        ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
        ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
        ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']]

att = (len(data[0]))

h = data[1][:-1]
for i in data[1:]:
    if i[-1] == 'Yes':
        for j in range(len(i[:-1])):
            if h[j] != i[j]:
                h[j] = '?'
print('Most Specific Hypothesis : ', h)
