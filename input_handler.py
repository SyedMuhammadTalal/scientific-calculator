
def get_operation():
    print("Select operation you want to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Natural Log")
    print("9. Log Base 10")
    print("10. Sin")
    print("11. Cos")
    print("12. Tan")
    print("13. Tangent")
    print("14. Factorial")
    print("Type 'exit' to quit")

    return input("Enter your choice (1-14): ").strip()
def get_numbers(operation): 
    # Operations that require two numbers
    if operation in['1','2','3','4','5','6']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a,b
    # Operations that require one number
    elif operation in ['7', '8', '9', '10', '11', '12', '13']:
        a = float(input("Enter number: "))
        return a,
    else:
        return()
       