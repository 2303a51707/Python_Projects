alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type encode to encrypt and decode to decrypt:\n").lower()
text = input("type your message\n").lower()
shift = int(input("type the shift number:\n"))


def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    # flip shift for decode
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    
    print(f"Here is the {encode_or_decode}d result: {output_text}")
    
    

ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)


