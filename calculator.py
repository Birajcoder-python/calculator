while True:
   print("welcome to Biraj calculator")
   print("\nChoose an operation:")
   print("1. Add")
   print("2. Subtract")
   print("3. Multiply")
   print("4. Divide")

   choice = input("Enter your choice (1-4): ")

   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))

   if choice == "1":
    print("Ans:", num1 + num2)
   elif choice == "2":
    print("Ans:", num1 - num2)
   elif choice == "3":
    print("Ans:", num1 * num2)
   elif choice == "4":
    if num2 != 0:
        print("Ans:", num1 / num2)
    else:
        print("Cannot divide by zero!")
   else:
    print("Invalid choice")

   again = input("Do you want to try again? (yes/no): ")
   if again.lower() != "yes":
    print("Thank you for using Biraj calculator!")
    break