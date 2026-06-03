expenses = []
try:
    with open("expense.txt", "r")as f:
        for line in f.read().splitlines():
            parts = line.split(",")
            expenses.append({"name": parts[0], "amount": float(parts[1])})

except FileNotFoundError:
    pass

while True:
    print("1. Add expense")
    print("2. View expense")
    print("3. View total")
    print("4. Quit")

    choice = (input("pick one (1/2/3/4): "))

    if choice == "1":
        name = input("Enter expense: ")
        amount = float(input("Enter amount: "))
        expenses.append({"name": name, "amount": amount})
        with open("expense.txt", "w")as f:
            for i in expenses:
                f.write(i["name"] + "," + str(i["amount"]) + "\n")
        
    elif choice == "2":
        for i in expenses:
            print(i["name"] + "-" + str(i["amount"]))

    elif choice == "3":
        total = 0
        for i in expenses:
            total = total + i["amount"]
        print(total)
        
    elif choice == "4":
        break

    


    

    


