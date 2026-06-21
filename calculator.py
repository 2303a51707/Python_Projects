print('''_____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|''')

      
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

calculation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    num1 = float(input("What is the first number?: "))

    should_accumulate = True
    while should_accumulate:
        # Show all available symbols
        for symbol in calculation:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        calc_function = calculation[operation_symbol]
        answer = calc_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start fresh: ").lower()

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()  # restart fresh

calculator()
