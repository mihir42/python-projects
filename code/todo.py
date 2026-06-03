try:
    with open ("tasks.txt", "r") as f:
        tasks = f.read().splitlines()
except FileNotFoundError:
    tasks = []

while True:

    print("1. View")
    print("2. Add")
    print("3. Delete")
    print("4. Quit")

    inp = input("Choose one(1/2/3/4): ")

    if inp == "4":
        print("Bye")
        break

    if inp == "2":
        task = input("Enter a task: ")
        tasks.append(task)
        with open("tasks.txt", "w")as f:
             for task in tasks:
                 f.write(task + "\n")

    if inp == "1":
        if tasks == []:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, task)

    if inp == "3":
        inp3 = input("Enter task no. to delete: ")
        num = int(inp3) - 1
        tasks.pop(num)
        print("Task removed")
        with open("tasks.txt", "w")as f:
             for task in tasks:
                 f.write(task + "\n")
                
            
