'''
Created on May 19, 2012

@author: christom
'''
import profile
import pstats
import timeit

def fizzBuzzModulo():
    '''
    Implement fizz buzz by computing the modulo of each value in the range
    '''
    fizzBuzz = {}
    
    for i in xrange(1, 101):
        if ((i % 5 == 0) and (i % 3 == 0)):
            fizzBuzz[i] =  "FizzBuzz"
        elif (i % 3 == 0):
            fizzBuzz[i] = "Fizz"
        elif (i % 5 == 0):
            fizzBuzz[i] = "Buzz"
        else:
            fizzBuzz[i] = str(i)
    
    return fizzBuzz

def fizzBuzzBitwise():
    fizzBuzz = {}
    '''
    Fizz Buzz map using two bits for each number, so 1 is 00, 2 is 00, 3 is 01, etc...
    01 is multiples of 3
    10 is multiples of 5
    11 is multiples of both 3 and 5
    '''
    fizzBuzzMap = 0b110000010010010000011000010000
    fBTranslate = ("Fizz", "Buzz", "FizzBuzz")
    for i in xrange(1,101):
        # Bitmask all but the current value
        current = fizzBuzzMap & 0b11 
        #Assign our result
        fizzBuzz[i] =  fBTranslate[int(current)-1] if (current > 0b0) else str(i)
        # Make a circular loop by shifting the map, and appending current to the beginning
        fizzBuzzMap = fizzBuzzMap >> 2 | current << 28 
    
    return fizzBuzz

def fizzBuzzDecrement():
    '''
    Implements fizz buzz by keeping track of how many steps we've taken 
    since the last results
    '''
    fizzBuzz = {}
    
    fizz = 3
    buzz = 5
    
    for i in xrange(1, 101):
        fizz -= 1
        buzz -= 1
        
        if (fizz == 0 and buzz == 0):
            fizzBuzz[i] =  "FizzBuzz"
            fizz = 3
            buzz = 5
        elif (fizz == 0):
            fizzBuzz[i] = "Fizz"
            fizz = 3
        elif (buzz == 0):
            fizzBuzz[i] = "Buzz"
            buzz = 5
        else:
            fizzBuzz[i] = str(i)

    return fizzBuzz

if __name__ == '__main__':
    
    moduloNames = []
    
    modulo = timeit.Timer("fizzBuzzModulo()", "from __main__ import fizzBuzzModulo")
    print "Results of modulo calculations..."
    print modulo.repeat(5, 50000)
    print profile.run('fizzBuzzModulo();')
    
    decrement = timeit.Timer("fizzBuzzDecrement()", "from __main__ import fizzBuzzDecrement")
    print "Results of decrement calculations..."
    print decrement.repeat(5, 50000)
    print profile.run('fizzBuzzDecrement();')
    
    bitwise = timeit.Timer("fizzBuzzBitwise()", "from __main__ import fizzBuzzBitwise")
    print "Results of bitwise calculations..."
    print bitwise.repeat(5, 50000)
    print profile.run('fizzBuzzBitwise();')
    
    