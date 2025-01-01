def arithmetic_operations():
    print("Basic Arithmetic Program")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

    choice = input("Choose an operation (1/2/3/4): ")
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1 * num2}")
        elif choice == '4':
            print(f"Result: {num1 / num2}" if num2 != 0 else "Error: Division by zero.")
    else:
        print("Invalid choice.")

arithmetic_operations()