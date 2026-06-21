import coffee_art

print(coffee_art.data)

# Menu dictionary
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 50
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 120
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 150
    }
}

# Machine resources
resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 200,
    "money": 0
}

is_on = True

while is_on:
    user = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user == "off":
        print("Machine shutting down...")
        is_on = False

    elif user == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ₹{resources['money']}")

    elif user in menu:
        drink = menu[user]
        ingredients = drink["ingredients"]
        cost = drink["cost"]

        # Check resources
        can_make = True
        for item in ingredients:
            if ingredients[item] > resources.get(item, 0):
                print(f"Sorry, not enough {item}.")
                can_make = False
                break

        if can_make:
            print(f"{user.title()} costs ₹{cost}. Please insert coins.")
            rupees = int(input("Enter amount: ₹"))

            if rupees < cost:
                print("Sorry, not enough money. Money refunded.")
            else:
                # Deduct resources
                for item in ingredients:
                    resources[item] -= ingredients[item]
                resources["money"] += cost

                change = rupees - cost
                if change > 0:
                    print(f"Here is ₹{change} in change.")
                print(f"Here is your {user}. Enjoy! ☕")

    else:
        print("Invalid choice. Please select espresso/latte/cappuccino/off/report.")
