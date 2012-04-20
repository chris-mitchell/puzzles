'''
Created on Apr 19, 2012

@author: christom
'''

class primes(object):
    '''
    classdocs
    '''

    def __init__(self, fileName="primes.txt"):
        '''
        Constructor
        '''
        self.currentIndex = 0
        self.listPrimes = self.loadFile(fileName)
        
    def loadFile(self, fileName):
        '''
        Load a list of primes from a CSV file
        '''
        f = open(fileName, 'r')
        primes = str(f.read()).split(',')
        f.close()
        
        return primes
    
    def getPrime(self):
        return self.listPrimes[self.currentIndex]
    
    def moveNext(self):
        
        if (self.currentIndex > len(self.listPrimes)):
            '''
            No more primes in our list
            '''
            return -1
        
        self.currentIndex += 1
        return 0
        
        
            