
import string


def key_generation(key):
    main = string.ascii_lowercase.replace('j', '.')
    key = key.lower()
    key_matrix = ['' for i in range(5)]
    i = 0
    j = 0
    for c in key:
        if c in main:
            key_matrix[i] += c
            main = main.replace(c, '.')
            j += 1
            if(j > 4):
                i += 1
                j = 0
    for c in main:
        if c != '.':
            key_matrix[i] += c
            j += 1
            if j > 4:
                i += 1
                j = 0
    return(key_matrix)


def conversion(plain_text):
    plain_text_pairs = []
    cipher_text_pairs = []
    plain_text = plain_text.replace(" ", "")
    plain_text = plain_text.lower()
    i = 0
    while i < len(plain_text):
        a = plain_text[i]
        b = ''
        if((i+1) == len(plain_text)):
            b = 'x'
        else:
            b = plain_text[i+1]
        if(a != b):
            plain_text_pairs.append(a+b)
            i += 2
        else:
            plain_text_pairs.append(a+'x')
            i += 1
    print("plain text pairs: ", plain_text_pairs)

    for pair in plain_text_pairs:
        flag = False
        for row in key_matrix:
            if(pair[0] in row and pair[1] in row):
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])
                cipher_text_pair = row[(j0+1) % 5]+row[(j1+1) % 5]
                cipher_text_pairs.append(cipher_text_pair)
                flag = True
        if flag:
            continue
        for j in range(5):
            col = "".join([key_matrix[i][j] for i in range(5)])
            if(pair[0] in col and pair[1] in col):
                i0 = col.find(pair[0])
                i1 = col.find(pair[1])
                cipher_text_pair = col[(i0+1) % 5]+col[(i1+1) % 5]
                cipher_text_pairs.append(cipher_text_pair)
                flag = True
        if flag:
            continue

        i0 = 0
        i1 = 0
        j0 = 0
        j1 = 0

        for i in range(5):
            row = key_matrix[i]
            if(pair[0] in row):
                i0 = i
                j0 = row.find(pair[0])
            if(pair[1] in row):
                i1 = i
                j1 = row.find(pair[1])
        cipher_text_pair = key_matrix[i0][j1]+key_matrix[i1][j0]
        cipher_text_pairs.append(cipher_text_pair)

    print("cipher text pairs: ", cipher_text_pairs)
    print('plain text: ', plain_text)
    print('cipher text: ', "".join(cipher_text_pairs))


key = input("Enter the key: ")
key_matrix = key_generation(key)
print("Key Matrix for encryption:")
print(key_matrix)
plain_text = input("Enter the message: ")

conversion(plain_text)

'''
----------OUTPUT----------
Enter the key: Make my day beautiful
Key Matrix for encryption:
['makey', 'dbuti', 'flcgh', 'nopqr', 'svwxz']
Enter the message: hi there my name is abhiram
plain text pairs:  ['hi', 'th', 'er', 'em', 'yn', 'am', 'ei', 'sa', 'bh', 'ir', 'am']
cipher text pairs:  ['rh', 'ig', 'yq', 'ya', 'mr', 'ka', 'yt', 'vm', 'il', 'hz', 'ka']
plain text:  hitheremynameisabhiram
cipher text:  rhigyqyamrkaytvmilhzka
>>> 
'''


def conversion(cipher_text):
    plain_text_pairs = []
    cipher_text_pairs = []
    cipiher_text = cipher_text.lower()
    i = 0
    while i < len(cipher_text):
        a = cipher_text[i]
        b = cipher_text[i+1]
        cipher_text_pairs.append(a+b)
        i += 2
    print("cipher text pairs: ", cipher_text_pairs)
    for pair in cipher_text_pairs:
        flag = False
        for row in key_matrix:
            if(pair[0] in row and pair[1] in row):
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])
                plain_text_pair = row[(j0+4) % 5]+row[(j1+4) % 5]
                plain_text_pairs.append(plain_text_pair)
                flag = True
        if flag:
            continue
        for j in range(5):
            col = "".join([key_matrix[i][j] for i in range(5)])
            if(pair[0] in col and pair[1] in col):
                i0 = col.find(pair[0])
                i1 = col.find(pair[1])
                plain_text_pair = col[(i0+4) % 5]+col[(i1+4) % 5]
                plain_text_pairs.append(plain_text_pair)
                flag = True
        if flag:
            continue
        i0 = 0
        i1 = 0
        j0 = 0
        j1 = 0
        for i in range(5):
            row = key_matrix[i]
            if(pair[0] in row):
                i0 = i
                j0 = row.find(pair[0])
            if(pair[1] in row):
                i1 = i
                j1 = row.find(pair[1])
        plain_text_pair = key_matrix[i0][j1]+key_matrix[i1][j0]
        plain_text_pairs.append(plain_text_pair)

    print("plain text pairs: ", plain_text_pairs)
    print('cipher text: ', "".join(cipher_text_pairs))
    print('plain text (message): ', "".join(plain_text_pairs))


key = input("Enter the key: ")

key_matrix = key_generation(key)
print("Key Matrix for encryption:")
print(key_matrix)
cipher_text = input("Enter the encrypted message: ")

conversion(cipher_text)

'''
----------OUTPUT----------
Enter the key: Make my day beautiful
Key Matrix for encryption:
['makey', 'dbuti', 'flcgh', 'nopqr', 'svwxz']
Enter the encrypted message: rhigyqyamrkaytvmilhzka
cipher text pairs:  ['rh', 'ig', 'yq', 'ya', 'mr', 'ka', 'yt', 'vm', 'il', 'hz', 'ka']
plain text pairs:  ['hi', 'th', 'er', 'em', 'yn', 'am', 'ei', 'sa', 'bh', 'ir', 'am']
cipher text:  rhigyqyamrkaytvmilhzka
plain text (message):  hitheremynameisabhiram
>>> 
'''

