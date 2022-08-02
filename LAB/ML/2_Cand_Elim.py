data = [['outlook', 'temp', 'humidity', 'wind', 'Water', 'Forecast', 'play'],
        ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
        ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
        ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
        ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']]

att = (len(data[0]))

S = ['#'] * (att-1)
G = []

# init S
for i in data[1:]:
    if i[-1] == 'Yes':
        S = i[:-1]
        break
for i in data[1:]:
    # +ve
    if i[-1] == 'Yes':
        for j in range(att-1):
            if S[j] != i[j]:
                S[j] = '?'
        if len(G) != 0:
            rem = []
            for k in G:
                for j in range(att-1):
                    if k[j] != S[j] and k[j] != '?':
                        rem.append(k)
                        break
            for j in rem:
                G.remove(j)
    # -ve
    else:
        for j in range(att-1):
            if S[j] != i[j] and S[j] != '?':
                g = ['?'] * (att-1)
                g[j] = S[j]
                if g not in G:
                    G.append(g)

print('Specific Hypothesis : ', S)
print('General Hypothesis : ', G)
