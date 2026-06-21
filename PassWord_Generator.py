import random

# Letters
letters = [ 'a','b','c','d','e','f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t',
            'u','v','w','x','y','z' ]

# Numbers
numbers = [ '0','1','2','3','4','5','6','7','8','9' ]

# Symbols
symbols = [ '!','@','#','$','%','^','&','*','(',')' ]

print("Welcome to the password generator")

nletters = int(input("How many letters would you like in your password?\n"))
nnumbers = int(input("How many numbers would you like in your password?\n"))
nsymbols = int(input("How many symbols would you like in your password?\n"))

#password = ""

#for char in range(nletters):
#    password += random.choice(letters)

#for char in range(nnumbers):
#    password += random.choice(numbers)

# for char in range(nsymbols):
  #  password += random.choice(symbols)

#print("Your password is:", password)

password_list = []
for char in range(0,nletters):
    password_list.append(random.choice(letters))
    
for char in range(0,nsymbols):
    password_list.append(random.choice(symbols))
    
for char in range(0,nnumbers):
    password_list.append(random.choice(numbers))
    
print(password_list)
random.shuffle(password_list)
print(password_list)

password= " "
for char in password_list:
    password += char
    
print(f"your password is: {password}")

    