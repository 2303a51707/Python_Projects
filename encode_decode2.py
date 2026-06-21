alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
 'u', 'v', 'w', 'x', 'y', 'z']

direction=input("type encode to encrypt and decode to decrypt:\n").lower()
text=input("type your message\n").lower()
shift=int(input("type the shift number:\n"))

def encrypt(original_text,shift_amount):
    cipher_text=" "
    for letter in original_text:
        shifted_position=alphabet.index(letter)+shift_amount
        shifted_position %= len(alphabet)
        cipher_text +=alphabet[shifted_position]
    print(f"here is the encoded result: {cipher_text}")
    
encrypt(original_text=text,shift_amount=shift)

def decrypt(original_text,shift_amount):
    cipher_text=" "
    for letter in original_text:
        shifted_position=alphabet.index(letter)-shift_amount
        shifted_position %= len(alphabet)
        cipher_text +=alphabet[shifted_position]
    print(f"here is the decoded result: {cipher_text}")
    
decrypt(original_text=text,shift_amount=shift)

