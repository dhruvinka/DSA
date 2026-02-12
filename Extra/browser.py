from S import Stack

s1=Stack(200)
s1.display()
s2=Stack(200)
s2.display()


while(True):
    print("1. visit new side")
    print("2. visit past side")
    print("3. visit next side")
    print("4. exit")
    print("Enter your Choice")
    choice=input()
    if choice == '1':
        print("Enter side need to visit")
        current=input()
        if s1.isFull():
            print('Stack is Full')
        else:
            s1.push(current)
        # s1.display()
    if choice == '2':
        # print("Top is .....",s1.top)
        if s1.isEmpty() or s1.top == 0:
            print("Stack is Empty or no Prev side")
        else:
            x=s1.pop()
            s2.push(x)
            print(" You are Right now in .....",s1.peek())
    if choice == '3':
        if s2.isEmpty():
            print("no Next side")
        else:
            x=s2.pop()
            s1.push(x)
            print(" You are Right now in .....",s1.peek())

    if choice == '4':
        break



# from S import Stack

# s1 = Stack(200)   # Back stack
# s2 = Stack(200)   # Forward stack

# while True:
#     print("\n1. Visit new site")
#     print("2. Visit past site (Back)")
#     print("3. Visit next site (Forward)")
#     print("4. Exit")
#     print("Enter your choice")

#     choice = input()

#     # 1️⃣ VISIT NEW SITE
#     if choice == '1':
#         print("Enter site to visit:")
#         current = input()
#         s1.push(current)

#         # clear forward history
#         while not s2.isEmpty():
#             s2.pop()

#         print("You are now on:", current)

#     # 2️⃣ GO BACK
#     elif choice == '2':
#         if len(s1.s) == 1:
#             print("No previous site available")
#         else:
#             x = s1.pop()
#             s2.push(x)
#             print("You are now on:", s1.peek())

#     elif choice == '3':
#         if s2.isEmpty():
#             print("No next site available")
#         else:
#             x = s2.pop()
#             s1.push(x)
#             print("You are now on:", s1.peek())

#     # 4️⃣ EXIT
#     elif choice == '4':
#         break

#     else:
#         print("Invalid choice")

# print("\nBrowsing History:")
# s1.display()
