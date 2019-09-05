queue=[]
def view():
    for x in range(len(queue)):
        print(queue[x])
def push():
    item = input("Please enter the item you wish to add to the Queue: ")
    queue.append(item)
def pop():
    item = queue.pop(0)
    print("You just popped out",item)
def peek():
    item = queue[0]
    print("You peeked",queue[0])

while True:
    print("")
    print("=========================")
    print("1. View Queue")
    print("2. Push onto Queue")
    print("3. Pop out of Queue")
    print("4. Peek Queue")
    print("=========================")
    print("")
    choice=int(input("Please enter your menu choice: "))
    if choice == 1:
        view()
    elif choice ==2:
        push()
    elif choice ==3:
        pop()
    elif choice ==4:
        peek()
    else:
        print("Invalid Input")
