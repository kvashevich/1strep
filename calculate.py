answer = True
while answer:
    while True:
        try:
            first_number = float(input("Enter first number --> "))
            break
        except ValueError:
            print("Wrong data!")
            continue

    while True:
        operation_list = ["+", "-", "/", "*"]
        operation = input("Choose the operation(+, -, /, *) --> ")
        if operation not in operation_list:
            print("Wrong operation!")
            continue
        break

    while True:
        try:
            second_number = float(input("Enter second number --> "))
            break
        except ValueError:
            print("Wrong data!")
            continue

    operation_dict = {
        "+": first_number + second_number,
        "-": first_number - second_number,
        "/": first_number / second_number,
        "*": first_number * second_number,
    }

    print(f"\n{first_number} {operation} {second_number} = {operation_dict[operation]}")

    while True:
        continue_ = input("\nWould you like repeat operation?(y/n): ")
        if continue_ == "y" or continue_ == "n":
            if continue_ == "y":
                break
            else:
                print("\nGood bye!")
                answer = False
                break
        else:
            print("Wrong answer!")