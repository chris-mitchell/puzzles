'''
Created on Apr 21, 2012

@author: christom
'''

from array import *

class primeSeive(object):
    '''
    classdocs
    '''

    def __init__(self, maxPrimes):
        '''
        Constructor
        '''
        self.maxPrimes = maxPrimes
        self.primes = array('B',[True]*maxPrimes)
        self.primes[0] = False
        self.__calcPrimes()
    
    def __calcPrimes(self):
        i = 2
        while (i*i <= self.maxPrimes):
            if(self.primes[i-1]):
                j = i
                while(i*j <= self.maxPrimes):
                    self.primes[(i*j)-1] = False
                    j += 1
            i += 1
    
    def getPrime(self, index):
        return self.primes[index-1]
    
    def findNthPrime(self, N):
        foundPrimes = 0
        for index, prime in enumerate(self.primes):
            if (prime):
                foundPrimes += 1
                if (foundPrimes == N):
                    return index+1
    