# 9. Implement a linked list to create and manage a set of elements. Set of elements 
# contains integer values i.e. S = {4,5,6}. No Elements are repeated in a Set. Also 
# implement a method which shows all possible subsets of the created set by user 
# i.e. {{4}, {5}, {6}, {4,5}, {4,6}, {5,6}, {4,5,6}, {Ø}}.

from Node import *

class Lklist:
    def __init__(self):
        self.head=None

    def insert(self,data):
        tmp=self.head
        while tmp:
            if tmp.data == data:
                return
            tmp=tmp.next
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new_node

    def get_element(self):
        curr=self.head
        x=[]
        while curr:
            x.append(curr.data)
            curr=curr.next
        return x
    
    def allsubsets(self):
        x=self.get_element()
        n=len(x)

        for i in range(n):
            print(x[i],end= " ")
        print()
        
        subsets=[[]]
        for i in x:
            x=[]
            for j in subsets:
                x.append(j +[i])
            subsets.extend(x)
        print(subsets)

        print("{", end="")
        for i in range(len(subsets)):
            if i == len(subsets)-1:
             print("{"+",".join(map(str,subsets[i]))+"}" ,end="")
            else:
                print("{"+",".join(map(str,subsets[i]))+"}" , "," ,end="")

        print("}", end="")



l1=Lklist();
n=int(input('enter the number of element you want to add :'))
if n > 0:
    for i in range(n):
        x=int(input("enter the element"))
        l1.insert(x)
l1.get_element()
l1.allsubsets()


