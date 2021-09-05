while True:
    digit_or_not = input("Check to input is digit --> ")
    if digit_or_not.isdigit():
        print("\n---Input is digit---\n")
    elif digit_or_not == "stop":
        break
    else:
        print("\n---Input is not digit---\n")

list_of_string = ["12", "python", "book", "7", "999", "0", "digit"]
for i in range(0, len(list_of_string)):
    if list_of_string[i].isdigit():
        list_of_string[i] = f"{list_of_string[i]} - digit"
    else:
        list_of_string[i] = f"{list_of_string[i]} - not digit"
print(list_of_string)

