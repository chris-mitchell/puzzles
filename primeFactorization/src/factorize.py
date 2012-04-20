'''
Created on Apr 19, 2012

@author: christom
'''

import primes

if __name__ == '__main__':
    
    factors = []
    
    primeManager = primes.primes()
    
    primeToFactorize = long(600851475143)
    
    while(True):
        currentPrime = long(primeManager.getPrime())
        
        while(primeToFactorize % currentPrime == 0):
            primeToFactorize /= currentPrime
            factors.append(int(currentPrime))
        
        if (primeToFactorize == 1):
            break
        
        if (primeManager.moveNext() != 0):
            print "Exceeded number of available primes..."
            break
        
    print "List of factors: " + str(factors)