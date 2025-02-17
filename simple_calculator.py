# Simple Python App
def main():
    print("Welcome to the simple calculator!")
    
    # Ask for two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Calculate the sum
        result = num1 + num2
        
        # Show the result
        print(f"The result of adding {num1} and {num2} is: {result}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
