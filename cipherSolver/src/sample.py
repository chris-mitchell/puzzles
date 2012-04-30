'''
Created on Apr 26, 2012

@author: christom
'''

from solveCipher import solveCipher
from cipher import cipher

if __name__ == '__main__':
    
    sampleString = "Washington had a vision of a great and powerful nation that would be built on republican lines using federal power. He sought to use the national government to preserve liberty, improve infrastructure, open the western lands, promote commerce, found a permanent capital, reduce regional tensions and promote a spirit of American nationalism. At his death, Washington was hailed as \"first in war, first in peace, and first in the hearts of his countrymen\". The Federalists made him the symbol of their party but for many years, the Jeffersonians continued to distrust his influence and delayed building the Washington Monument. As the leader of the first successful revolution against a colonial empire in world history, Washington became an international icon for liberation and nationalism, especially in France and Latin America. He is consistently ranked among the top three presidents of the United States, according to polls of both scholars and the general public"
    
    print "Sample String: " + sampleString
    
    cipher = cipher()
    sampleCipher = cipher.encode(sampleString, 13)
    
    print "Sample Cipher: " + sampleCipher
    
    myCipherSolver = solveCipher(sampleCipher)
    rotation = myCipherSolver.findRotationByChar("E")
    print "Guessed rotation of: " + str(rotation)
    
    print "Original String: " +  str(cipher.decode(sampleCipher, rotation))
    
    