print("Welcome to PVR CINEMAS")

age = int(input("enter ur age"))
d_glass = input("do you want 3d glass y/n")
popcorn=input("do you want popcorn")
bill=0

if age<12:
    bill += 150
    
elif age<=18:
    bill += 200
    
elif age>18:
    bill += 300
    
else:
    print("invalid chars")
    
if d_glass=="y":
        bill += 50
        
if popcorn=="y":
        bill += 100
        
print(f"your final bill is {bill}")
        
    
    
        