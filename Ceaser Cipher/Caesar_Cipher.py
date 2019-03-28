#Caesar Cipher

import pyperclip

# message to encrypt or decrypt
message = 'L9wx8Lx8Lrpt8p7Lrx5wt7Lt3r7.59x43'

#key for encryption/decryption
key = 15

# Mode - e/d
mode = 'decrypt'

#Symbols
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#String to store
translated = ''

# To find the Index value
for symbol in message:
    if symbol in SYMBOLS:
        symbolINdex = SYMBOLS.find(symbol)
        
        #encrypt or decrypt
        if mode == 'encrypt':
            translateIndex = symbolINdex + key
        elif mode == 'decrypt':
            translateIndex = symbolINdex - key
            
        # Handle wraparound if needed
        if translateIndex >= len(SYMBOLS):
            translateIndex = translateIndex - len(SYMBOLS)
        elif translateIndex < 0:
            translateIndex = translateIndex + len(SYMBOLS)
            
        translated = translated + SYMBOLS[translateIndex]
    else:
        #append without encrypting
        translated = translated + symbol
#output
print(translated)
pyperclip.copy(translated)
            
            
        
    