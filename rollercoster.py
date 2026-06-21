print("Welcome to WonderLa Rollercoaster Ride!")

# Take inputs
name=input("Enter your name")
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))
photo = input("Do you want a ride photo? (y/n): ").lower()

bill = 0

# Height check
if height < 120:
    print("Sorry, you can't ride. You are not tall enough.")
else:
    # Age-based pricing
    if age < 12:
        bill += 150
    elif age <= 18:
        bill += 250
    elif age >= 45 and age <=50:
        bill += 0
        print("have a free ride")
        
    else:
        bill += 500
        

    # Optional photo
    if photo == "y":
        bill += 50

    # Final bill
    print(f"Dear {name} Your final bill is ₹{bill}")
