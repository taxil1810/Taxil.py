while True:

    print("Welcome to the bill splitter app!")
    print()

    bill = float(input("Enter the total bill amount:₹ "))
    people = int(input("Enter Number of people: "))
    tip_percentage = int(input("Enter tip percentag (0/5/10/15/20): "))

    if bill < 0 or people <= 0 or tip_percentage not in [0, 5 , 10 , 15 , 20]:
        print("Invalid input! please try again.")
        continue

    tip = (tip_percentage / 100) * bill
    final_bill = bill + tip
    per_person = final_bill / people    

    print(f"\nTip amount : ₹{tip:.2f}")
    print(f"Total bill (with tip): ₹{final_bill:.2f}")
    print(f"Each person should pay: ₹{per_person / people}")

    input("\nwould you like to calculate anothrr bill? (y/n): ")
    print("Thank you for using the bill splitter app!")
    print("...\n")
    break