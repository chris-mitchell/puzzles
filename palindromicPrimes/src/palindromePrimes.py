'''
Created on Apr 13, 2012

@author: christom
'''
import math

def isPalindrome(data):
    return (str(data) == str(data)[::-1])


def isPrime(data):
    data = int(data)
    #If divisible by 2, no good
    if (data%2==0): 
        return False
    
    #Use square root of data, count two to skip evens
    for i in range(3, int(data**0.5)+1, 2):
        if (data % i==0):            
            return False
        
    return True

def findFirstInPi(valid):
    
    bestMatch = 0
    bestMatchLocation = 0
    
    for data in valid:
        firstOccurence = pi.find(str(data))
        if ((bestMatchLocation == 0 or bestMatchLocation > firstOccurence) 
                and firstOccurence != -1):
            bestMatch = data
            bestMatchLocation = firstOccurence
    
    return bestMatch

def readAccuratePi():
    f = open('pi.txt', 'r')
    data = str(f.read())
    f.close()
    return data   
    
if __name__ == '__main__':
    
    valid = []
    sortedResults = []
    
    isPrime(9)
    
    pi = readAccuratePi()
    
    for i in range(1000000, 9999999):
        if (isPalindrome(i)):
            if (isPrime(i)):
                valid.append(i)
                
    print "Got " + str(len(valid)) + " palindromes that are prime"
    
    print str(findFirstInPi(valid)) + " is our answer..."
                
    
            