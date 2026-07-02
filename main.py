def add(a,b):
    return a+b
def subtracr(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        raise ValueError("Cannot divide by zero")
    else:
        return a/b
OPERATIONS = {
    '+': add,
    '-': subtracr,
    '*': multiply,
    '/': divide,
}
def calculator():
    print("simple calculator")
    print(f"Operations: {', '.join(OPERATIONS.keys())}")
    print("Type 'quit' to exit\n")
   
    while True:
        try:
            num1_input = input("Enter first number (or 'quit'): ")
            if num1_input.lower() == 'quit':
                break
            num1 = float(num1_input)
            
            op = input(f"Enter operation ({', '.join(OPERATIONS.keys())}): ").strip()
            if op not in OPERATIONS:
                print("Error: Invalid operation!\n")
                continue

            num2 = float(input("Enter second number: "))

            result = OPERATIONS[op](num1, num2)
            print(f"Result: {num1} {op} {num2} = {result}\n")

        except ZeroDivisionError as e:
            print(f"Error: {e}\n")
        except ValueError:
            print("Error: Please enter valid numbers!\n")


if __name__ == "__main__":
    calculator()
            

