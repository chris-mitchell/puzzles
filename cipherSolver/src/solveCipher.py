'''
Created on Apr 26, 2012

@author: christom
'''
from cipher import cipher
from string import ascii_uppercase, upper
from decimal import *

class solveCipher(object):

    def __init__(self, cipher):
        '''
        Constructor
        '''
        self.ignoreList = [' ', ',', '\'', '.', '$', '-', '"']
        self.cipher = self.__parseCipher(cipher)
        self.cipherLength = len(self.cipher)
        self.cipherFrequency = self.__getCipherFrequency()
        self.letterFreq = self.__getLetterFreq()
        
    def __parseCipher(self, cipher):
        parsedCipher = []
        for char in cipher:
            if (self.ignoreList.count(char) == 0):
                parsedCipher.append(char)
                
        return "".join(parsedCipher)
        
    def __getLetterFreq(self):
        '''
        Returns a dictionary of letters A through Z and their frequency as a percentage
        '''
        return {
                'A': 8.167,
                'B': 1.492,
                'C': 2.782,
                'D': 4.253,
                'E': 12.702,
                'F': 2.228,
                'G': 2.015,
                'H': 6.094,
                'I': 6.966,
                'J': 0.153,
                'K': 0.772,
                'L': 4.025,
                'M': 2.406,
                'N': 6.749,
                'O': 7.507,
                'P': 1.929,
                'Q': 0.095,
                'R': 5.987,
                'S': 6.327,
                'T': 9.056,
                'U': 2.758,
                'V': 0.978,
                'W': 2.360,
                'X': 0.150,
                'Y': 1.974,
                'Z': 0.074
                }
    
    def __getCipherFrequency(self):
        '''
        Returns a dictionary of letters and their frequency within the cipher
        '''
        alphabet = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                    'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 
                    'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
        frequency = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                    'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 
                    'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
        
        for char in self.cipher:
            '''
            Count the number of times each char is used.
            '''
            char = upper(char)
            alphabet[char] += 1
        
        for char in alphabet.keys():
            '''
            Store the percentage of characters from the cipher 
            '''
            frequency[char] = (float(alphabet[char])/float(self.cipherLength) * 100)
            
        return frequency
    
    def findRotationByChar(self, characterToMatch):
        '''
        Finds the closest match for the character given. E is the recommended choice.
        '''
        charFreq = self.letterFreq[characterToMatch]
        
        bestMatch = sorted([(abs(k - charFreq),v) for (v,k) in self.cipherFrequency.items()])[0][1]
        
        bestMatchIndex = ascii_uppercase.find(bestMatch)
        charToMatchIndex = ascii_uppercase.find(characterToMatch)
        
        if (bestMatchIndex >= charToMatchIndex):
            return bestMatchIndex-charToMatchIndex
        else:
            return (bestMatchIndex + 26) - charToMatchIndex        
