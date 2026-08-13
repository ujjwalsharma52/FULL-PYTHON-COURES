l = []

while True:
    c = int(input('''
    1. Push Elements
    2. Pop Elements
    3. Front Element
    4. Last Element
    5. Display Queue
    6. Exit
    Enter your choice: '''))
    
    if c == 1:
        n = input("Enter the value: ")
        l.append(n)
        print("Queue:", l)

    elif c == 2:
        if len(l) == 0:
            print("Empty Queue")
        else:
            del l[0]
            print("Queue:", l)

    elif c == 3:
        if len(l) == 0:
            print("Empty Queue")
        else:
            print("First Queue Value:", l[0])

    elif c == 4:
        if len(l) == 0:
            print("Empty Queue")
        else:
            print("Last Queue Value:", l[-1])

    elif c == 5:
        if len(l) == 0:
            print("Empty Queue")
        else:
            print("Queue:", l)

    elif c == 6:
        print("Program Exit")
        break

    else:
        print("Invalid Operation")