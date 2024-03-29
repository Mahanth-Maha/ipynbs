import string


main=string.ascii_lowercase

def generate_key(n,s):
    s=s.replace(" ","")
    s=s.lower()
    
    key_matrix=['' for i in range(n)]
    i=0;j=0
    for c in s:
        if c in main:
            key_matrix[i]+=c
            j+=1
            if(j>n-1):
                i+=1
                j=0
    print("The key matrix "+"("+str(n)+'x'+str(n)+") is:")
    print(key_matrix)
    
    key_num_matrix=[]
    for i in key_matrix:
        sub_array=[]
        for j in range(n):
            sub_array.append(ord(i[j])-ord('a'))
        key_num_matrix.append(sub_array)
        
    for i in key_num_matrix:
        print(i)
    return(key_num_matrix)
    

def message_matrix(s,n):
    s=s.replace(" ","")
    s=s.lower()
    final_matrix=[]
    if(len(s)%n!=0):

        while(len(s)%n!=0):
            s=s+'z'
    print("Converted plain_text for encryption: ",s)
    for k in range(len(s)//n):
        message_matrix=[]
        for i in range(n):
            sub=[]
            for j in range(1):
                sub.append(ord(s[i+(n*k)])-ord('a'))
            message_matrix.append(sub)
        final_matrix.append(message_matrix)
    print("The column matrices of plain text in numbers are:  ")
    for i in final_matrix:
        print(i)
    return(final_matrix)

def getCofactor(mat, temp, p, q, n): 
    i = 0
    j = 0
  
    for row in range(n):  
        for col in range(n): 
            if (row != p and col != q) : 
                temp[i][j] = mat[row][col] 
                j += 1        
                if (j == n - 1): 
                    j = 0
                    i += 1

def determinantOfMatrix(mat, n): 
  
    if (n == 1): 
        return mat[0][0] 
          
    temp = [[0 for x in range(n)]  
               for y in range(n)]  
    for f in range(n): 
        getCofactor(mat, temp, 0, f, n) 
        D += (sign * mat[0][f] *
              determinantOfMatrix(temp, n - 1))
        sign = -sign 
    return D 
  
def isInvertible(mat, n): 
    if (determinantOfMatrix(mat, n) != 0): 
        return True
    else: 
        return False


def multiply_and_convert(key,message):
    
    res_num = [[0 for x in range(len(message[0]))] for y in range(len(key))]
    
    for i in range(len(key)): 
        for j in range(len(message[0])):
            for k in range(len(message)): 
        
                res_num[i][j]+=key[i][k] * message[k][j]

    res_alpha = [['' for x in range(len(message[0]))] for y in range(len(key))]
    for i in range(len(key)):
        for j in range(len(message[0])):
    
            res_alpha[i][j]+=chr((res_num[i][j]%26)+97)
            
    return(res_alpha)
    
n=int(input("What will be the order of square matrix: "))
s=input("Enter the key: ")
key=generate_key(n,s)
if (isInvertible(key, len(key))): 
    print("Yes it is invertable and can be decrypted") 
else: 
    print("No it is not invertable and cannot be decrypted")
    
plain_text=input("Enter the message: ")
message=message_matrix(plain_text,n)
final_message=''
for i in message:
    sub=multiply_and_convert(key,i)
    for j in sub:
        for k in j:
            final_message+=k
print("plain message: ",plain_text)
print("final encrypted message: ",final_message)

'''
----------OUTPUT----------
What will be the order of square matrix: 3
Enter the key: BACK UP ABC
The key matrix (3x3) is:
['bac', 'kup', 'abc']
[1, 0, 2]
[10, 20, 15]
[0, 1, 2]
Yes it is invertable and can be decrypted
Enter the message: hi there my name is abhiram
Converted plain_text for encryption:  hitheremynameisabhiramzz
The column matrices of plain text in numbers are:  
[[7], [8], [19]]
[[7], [4], [17]]
[[4], [12], [24]]
[[13], [0], [12]]
[[4], [8], [18]]
[[0], [1], [7]]
[[8], [17], [0]]
[[12], [25], [25]]
plain message:  hi there my name is abhiram
final encrypted message:  tvuppmaqilyyocsovpierkhx
>>> 
'''
import string
import numpy as np

main=string.ascii_lowercase

def generate_key(n,s):
    s=s.replace(" ","")
    s=s.lower()
    
    key_matrix=['' for i in range(n)]
    i=0;j=0
    for c in s:
        if c in main:
            key_matrix[i]+=c
            j+=1
            if(j>n-1):
                i+=1
                j=0
    print("The key matrix "+"("+str(n)+'x'+str(n)+") is:")
    print(key_matrix)
    
    key_num_matrix=[]
    for i in key_matrix:
        sub_array=[]
        for j in range(n):
            sub_array.append(ord(i[j])-ord('a'))
        key_num_matrix.append(sub_array)

    for i in key_num_matrix:
        print(i)
    return(key_num_matrix)


def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

def method(a, m) :
    if(a>0):
        return (a%m)
    else:
        k=(abs(a)//m)+1
    return method(a+k*m,m)


def message_matrix(s,n):
    s=s.replace(" ","")
    s=s.lower()
    final_matrix=[]
    if(len(s)%n!=0):
        for i in range(abs(len(s)%n)):
            s=s+'z'
    print("Converted cipher_text for decryption: ",s)
    for k in range(len(s)//n):
        message_matrix=[]
        for i in range(n):
            sub=[]
            for j in range(1):
                sub.append(ord(s[i+(n*k)])-ord('a'))
            message_matrix.append(sub)
        final_matrix.append(message_matrix)
    print("The column matrices of plain text in numbers are:  ")
    for i in final_matrix:
        print(i)
    return(final_matrix)


def multiply_and_convert(key,message):
    
    res_num = [[0 for x in range(len(message[0]))] for y in range(len(key))]
    
    for i in range(len(key)): 
        for j in range(len(message[0])):
            for k in range(len(message)): 
                res_num[i][j]+=key[i][k] * message[k][j]

    res_alpha = [['' for x in range(len(message[0]))] for y in range(len(key))]
    for i in range(len(key)):
        for j in range(len(message[0])):
            res_alpha[i][j]+=chr((res_num[i][j]%26)+97)
            
    return(res_alpha)



n=int(input("What will be the order of square matrix: "))
s=input("Enter the key: ")
key_matrix=generate_key(n,s)
A = np.array(key_matrix)
det=np.linalg.det(A)
adjoint=det*np.linalg.inv(A)

if(det!=0):
    convert_det=modInverse(int(det),26)
    adjoint=adjoint.tolist()
    print("Adjoint Matrix before modulo26 operation: ")
    for i in adjoint:
        print(i)
    print(convert_det)

    for i in range(len(adjoint)):
        for j in range(len(adjoint[i])):
            adjoint[i][j]=round(adjoint[i][j])
            adjoint[i][j]=method(adjoint[i][j],26)
    print("Adjoint Matrix after modulo26 operation: ")
    for i in adjoint:
        print(i)

    adjoint=np.array(adjoint)
    inverse=convert_det*adjoint

    inverse=inverse.tolist()
    for i in range(len(inverse)):
        for j in range(len(inverse[i])):
            inverse[i][j]=inverse[i][j]%26

    print("Inverse matrix after applying modulo26 operation: ")
    for i in inverse:
        print(i)

    cipher_text=input("Enter the cipher text: ")
    message=message_matrix(cipher_text,n)
    plain_text=''
    for i in message:
        sub=multiply_and_convert(inverse,i)
        for j in sub:
            for k in j:
                plain_text+=k
                
    print("plain message: ",plain_text)
else:
    print("Matrix cannot be inverted")

'''
----------OUTPUT----------
What will be the order of square matrix: 3
Enter the key: BACK UP ABC
The key matrix (3x3) is:
['bac', 'kup', 'abc']
[1, 0, 2]
[10, 20, 15]
[0, 1, 2]
Adjoint Matrix before modulo26 operation: 
[25.000000000000014, 2.000000000000001, -40.000000000000014]
[-20.000000000000004, 2.000000000000001, 5.000000000000001]
[10.000000000000002, -1.0000000000000004, 20.000000000000004]
11
Adjoint Matrix after modulo26 operation: 
[25, 2, 12]
[6, 2, 5]
[10, 25, 20]
Inverse matrix after applying modulo26 operation: 
[15, 22, 2]
[14, 22, 3]
[6, 15, 12]
Enter the cipher text: tvuppmaqilyyocsovpierkhx
Converted cipher_text for decryption:  tvuppmaqilyyocsovpierkhx
The column matrices of plain text in numbers are:  
[[19], [21], [20]]
[[15], [15], [12]]
[[0], [16], [8]]
[[11], [24], [24]]
[[14], [2], [18]]
[[14], [21], [15]]
[[8], [4], [17]]
[[10], [7], [23]]
plain message:  hitheremynameisabhiramzz
>>> 
'''
             
            