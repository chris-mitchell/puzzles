'''
Created on Apr 16, 2012

@author: christom
'''

if __name__ == '__main__':
    
    total = 0
    
    for i in range(1,1000):
        if (i%3 == 0) or (i%5 == 0):
            total += i

    print "Total: " + str(total)
        