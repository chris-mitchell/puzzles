'''
Created on Apr 21, 2012

@author: christom
'''

import primeSeive

if __name__ == '__main__':
    
    '''
    Assume the Nth prime will be less than the sieve we create
    '''
    primes = primeSeive.primeSeive(105000)
    
    '''
    Go find the Nth prime
    '''
    print "The " + str(10001) + " prime is: " + str(primes.findNthPrime(10001))
    