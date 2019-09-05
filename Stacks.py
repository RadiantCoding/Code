stack=[]
def view():
    for x in range(len(stack)):
        print(stack[x])
def push():
    item = input ("Please enter the item you wish to add to the Stack: ")
    stack.append(item)
def pop():
    item = stack.pop(-1)
    print("You just poped out: ",item)
def peek():
    item = stack[-1]
    print("You just peeked",item)

while True:
    print("")
    print("=======================")
    print("1.View the Stack")
    print("2.Push the Stack")
    print("3.Pop the Stack")
    print("4.Peek the Stack")
    print("=======================")
    print("")
    choice = int(input("Please enter a menu choice: "))

    if choice == 1:
        view()
    elif choice == 2:
        push()
    elif choice == 3:
        pop()
    elif choice==4:
        peek()
    else:
        print("Input Incorrect")
