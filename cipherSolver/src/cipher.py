'''
Created on Apr 26, 2012

@author: christom
'''

from string import ascii_uppercase, ascii_lowercase

class cipher(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.ignoreList = [' ', ',', '\'', '.', '$', '-', '"']
    
    def __rotN(self, plaintext, rotation):
        '''
        Accepts a string of plaintext, and will rotate N units
        ie: a rotation of 1 will change A to B, B to C, and so forth
        '''                
        cipher = []
        for char in plaintext:
            if (self.ignoreList.count(char) != 0):
                cipher.append(char)
            elif char in ascii_uppercase:
                index = (ascii_uppercase.find(char) + rotation) % 26
                cipher.append(ascii_uppercase[index])
            elif char in ascii_lowercase:
                index = (ascii_lowercase.find(char) + rotation) % 26
                cipher.append(ascii_lowercase[index])
            
        return "".join(cipher)
    
    def encode(self, plaintext, rotation):
        if 0 <= rotation >= 27:
            return "Invalid rotation units"
        return self.__rotN(plaintext, rotation)

    def decode(self, plaintext, rotation):
        if 0 < rotation > 27:
            return "Invalid rotation units"
        
        return self.__rotN(plaintext, -1*rotation)
