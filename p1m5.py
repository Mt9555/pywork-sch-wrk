# [ ] create, call and test the adding_report() function
def add_report(report):
    total = 0
    items = ""
    print("Input an integer to add to the total or \"Q\" to quit")
    while True:
        if report.upper() == "T":
            user_1 = input('Enter an integer or "Q":')
            if user_1.isdigit():
                total = int(user_1) + total
            elif user_1.upper() == "Q":
                print("\ntotal\n", total)
                break
            else:
                print(" is Invalid input")
        elif report.upper() == "A":
            user_1 = input('Enter an integer or "Q":')
            if user_1.isdigit():
                items = items + user_1 + "\n"
                total = int(user_1) + total
            elif user_1.upper() == "Q":
                print("\nitems")
                print(items)
                print("Total")
                print(total)
                break
            else:
                print("Invalid input")

add_report("A")