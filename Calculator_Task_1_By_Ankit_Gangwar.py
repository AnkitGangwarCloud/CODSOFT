print("CALCULATOR")

while True:

    n1 = float(input("Enter First Number: "))

    n2 = float(input("Enter First Number: "))

    print("Options for arithmetic calculations are:")

    print("1-Addition (n1+n2)")
    print("2-Subraction (n1-n2)")
    print("3-Multiplication (n1*n2)")
    print("4-Devision (n1/n2)")

    choice = int(input("What you want to do: "))

    if choice == 1:
        print(n1 + n2)


    elif choice == 2:
        print(n1 - n2)

    elif choice == 3:
        print(n1 * n2)

    elif choice == 4:
        print(n1 / n2)

    else:
        print("Invalid Choice ! Choose something from given options")

    confirmation = input("Do you want to continue arithmetic calculations ?(y/n): ")

    if confirmation.lower() == "n":
        break