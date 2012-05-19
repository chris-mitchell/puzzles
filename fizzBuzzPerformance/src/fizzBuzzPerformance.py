'''
Created on May 19, 2012

@author: christom
'''

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
    pass

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
    
    
    modulo = timeit.Timer("fizzBuzzModulo()", "from __main__ import fizzBuzzModulo")
    print "Results of modulo calculations..."
    print modulo.repeat(5, 50000)
    
    decrement = timeit.Timer("fizzBuzzDecrement()", "from __main__ import fizzBuzzDecrement")
    print "Results of decrement calculations..."
    print decrement.repeat(5, 50000)
    
    bitwise = timeit.Timer("fizzBuzzBitwise()", "from __main__ import fizzBuzzBitwise")
    print "Results of bitwise calculations..."
    print bitwise.repeat(5, 50000)
