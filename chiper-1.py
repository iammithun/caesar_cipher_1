# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 17:16:37 2024

@author: iamrs
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shif_amount):
    cipher_text=""
    for letter in plain_text:
      position=alphabet.index(letter)
      new_position=position+shift_amount
      new_alphabet=alphabet[nw_position]
      cipher_text+=new_letter
    print(f"the encoded text is {cipher_text}")
    
encrypt(plain_text=text, shift_amount=shift)
    
      
      
      
      
        