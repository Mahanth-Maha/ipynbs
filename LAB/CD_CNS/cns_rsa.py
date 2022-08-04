import math
import string

main=string.ascii_lowercase

'''
function gcd(a, b)
    if b = 0
        return a
    else
        return gcd(b, a mod b)
'''

def multiplicative_inverse(a, m):
    a=a%m; 
    for x in range(1,m) : 
        if((a*x)%m==1) : 
            return x 
    return 1

'''
def get_mod_expo(base,exponent,modulus):
    result=1
    while exponent:
        d=exponent%2
        exponent=exponent//2
        if d:
            result=result*base%modulus
        base=base*base%modulus
    return result
'''

def generate_keypair(p, q):
    n=p*q
    print("Value of n: ",n)


    phi = (p-1)*(q-1)
    print("Value of phi(n): ", phi)



    print("Enter e such that is co-prime to ", phi,": ")
    e=int(input())



    g=math.gcd(e,phi)
    while(g!=1):
        print("The number you entered is not co-prime")
        e=int(input())
        g=math.gcd(e,phi)
        
    print("Value of exponent(e) entered is: ", e)


    d = multiplicative_inverse(e, phi)


    

    return (e,n),(d,n)

def encrypt(public_key, to_encrypt):
    key, n = public_key


    cipher=pow(to_encrypt,key)%n
    return cipher


def decrypt(private_key, to_decrypt):
    key, n = private_key


    decrypted=pow(to_decrypt,key)%n
    return decrypted

p=int(input("Enter prime p: "))
q=int(input("Enter prime q (!=p): "))

while(p==q):
    p=int(input("Enter prime p: "))
    q=int(input("Enter prime q (!=p): "))
    
print("Prime number p: ",p)
print("Prime number q: ",q)

print("Generating Public/Private key-pairs!")
public, private = generate_keypair(p, q)
print("Your public key is (e,n) ", public)
print("Your private key is (d,n) ", private)

message = input("Enter the message: ")

message=message.replace(" ","")
message=message.lower()
arr=[]
cipher_text=[]
for i in message:
    if i in main:
        arr.append(main.index(i))
for i in arr:
    cipher_text.append(encrypt(public,i))

print("Encrypted message (Cipher Text): ",cipher_text)

plain=[]
for i in cipher_text:
    plain.append(decrypt(private,i))
plain_text=''
for i in plain:
    plain_text=plain_text+main[i]
print("Plain text array: ",plain)
print("Decrypted message (Plain Text): ", plain_text)


'''
----------OUTPUT----------
Enter prime p: 157
Enter prime q (!=p): 149
Prime number p:  157
Prime number q:  149
Generating Public/Private key-pairs!
Value of n:  23393
Value of phi(n):  23088
Enter e such that is co-prime to  23088 : 
23
Value of exponent(e) entered is:  23
Your public key is (e,n)  (23, 23393)
Your private key is (d,n)  (6023, 23393)
Enter the message: world winner
Encrypted message (Cipher Text):  [22344, 18436, 8290, 15143, 15339, 22344, 8926, 8780, 8780, 22321, 8290]
Plain text array:  [22, 14, 17, 11, 3, 22, 8, 13, 13, 4, 17]
Decrypted message (Plain Text):  worldwinner
>>> 
'''
