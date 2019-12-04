#Code by - Neetish borkar
#Roll No - PB12
def PrimeTest(p):
    for i in range(2,p):
            if p%i==0:
                print (p , 'Is not a prime number')
                return(False)
                break
            else:
                return(True)
p = int(input('Enter 1st prime number:'))
q = int(input('Enter 2nd prime number:'))
text = int(input('Enter the number:'))

def gcd(a,b):
    if b==0:
        return(a)
    else:
        return gcd(b,a%b)

if PrimeTest(p) and PrimeTest(q)and text<(p*q) :
    n = p*q         #n is the modulus for the public key and the private keys
    print('N:',n)
    z = (p-1)*(q-1)

    for e in range (2,z-1):           #Public Key
        if gcd(e,z)==1:
            break

    for j in range(1,z-1):
        k = 1 + j*z
        if k % e == 0:
            d = int(k/e)        #private key
            break

    print ('Public Key e:',e,'\nPrivate Key d:',d)
    encrypt = pow(text,e)%n
    print ('Encrypted text:',encrypt)

    decrypt = pow(encrypt,d)%n
    print ('Decrypted text:',decrypt)

elif text >= (p*q):
    print ('Input Text is larger than expected')
