'''
Created on Apr 14, 2012

@author: christom
'''
import palindrome
import unittest


class Test(unittest.TestCase):


    def testPalindrome(self):
        self.assertTrue(palindrome.isPalindrome(1111))
        self.assertTrue(palindrome.isPalindrome(313))
        self.assertTrue(palindrome.isPalindrome(12344321))
        self.assertTrue(palindrome.isPalindrome(1))
        
        self.assertFalse(palindrome.isPalindrome(1121))
        self.assertFalse(palindrome.isPalindrome(233))
        self.assertFalse(palindrome.isPalindrome(5678))
        self.assertFalse(palindrome.isPalindrome(1234))

    def testPrime(self):
        self.assertTrue(palindrome.isPrime(1))
        self.assertTrue(palindrome.isPrime(7))
        self.assertTrue(palindrome.isPrime(2207))

        self.assertFalse(palindrome.isPrime(2))
        self.assertFalse(palindrome.isPrime(8))
        self.assertFalse(palindrome.isPrime(9))
        self.assertFalse(palindrome.isPrime(10))
        self.assertFalse(palindrome.isPrime(2208))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()