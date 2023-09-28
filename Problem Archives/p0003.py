#Importing math module for the sqrt function
import math

def isprime(x):
    """
    Returns true if the given number x is prime, else false
    """
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return False
    return True
    
def largest_prime_factor(num):
    """
    returns the largest prime factor of a given number num
    """
    maxp = -1
    for n in range(2,int(math.sqrt(num))+1):
        if(num%n==0):
            print(num//n,n)
            if(isprime(num//n)):
                return num//n
            elif(isprime(n) and n>maxp):
                maxp=n
    if(maxp!=-1):
        return maxp
    return num

if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
