
    # Import only what is needed 
from operations import add, modulus, subtract, multiply, divide, power, square_root,  natural_log,log_base_10, sin, cos, tan, tangent, factorial
from input_handler import get_operation, get_numbers

def calculate(choice, numbers):
    if choice == "1":
        return add(*numbers)
    elif choice == "2":
        return subtract(*numbers)
    elif choice == "3":
        return multiply(*numbers)
    elif choice == "4":
        return divide(*numbers)
    elif choice == "6":
        return modulus(*numbers)
    elif choice == "6":
        return power(*numbers)
    elif choice == "7":
        return square_root(*numbers)
    elif choice == "8":
        return log_base_10(*numbers)
    elif choice == "9":
        return natural_log(*numbers)
    elif choice == "10":
        return sin(*numbers)
    elif choice == "11":
        return cos(*numbers)
    elif choice == "12":
        return tan(*numbers)
    elif choice == "13":
        return tangent(*numbers)
    elif choice == "14":
        return factorial(*numbers)

def print_result(result):
    print("Result:", result)

# Main Loop
def main():
    while True:
        choice = get_operation()
        if choice.lower() == "exit":
            print("Exiting Calculator...")
            break

        numbers = get_numbers(choice)
        try:
            result = calculate(choice, numbers)
            print_result(result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
