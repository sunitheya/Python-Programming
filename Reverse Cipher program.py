
"""@author: nitin
"""

"""The reverse cipher encrypts a message by printing it in reverse order. So “Hello, world!” 
encrypts to “!dlrow ,olleH”. To decrypt, or get the original message, you simply reverse the 
encrypted message. The encryption and decryption steps are the same.

However, this reverse cipher is weak, making it easy to figure out the plaintext. Just by 
looking at the ciphertext, you 
can figure out the message is in reverse order."""

Message = input('Enter the sentence to Cipher')
Translated =''
i = len(Message)-1
while i>=0:
    Translated = Translated + Message[i]
    i = i-1
print('Translated Message :'+Translated) 
print('Original Message :'+ Message)