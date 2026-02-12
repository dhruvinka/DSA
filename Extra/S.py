class Stack:
    def __init__(self,size):
        self.s = []
        self.size=size
        self.top = -1

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.size - 1
    
    def push(self, data):
        if self.isFull():
            print("Stack full")
        else:
            self.s.append(data)
            self.top += 1

    def display(self):
        print("Stack",self.s)
        print("Size",self.size)
        print("Top",self.top)
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.top-=1
            return self.s.pop()
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.s[self.top]   
        
if __name__=="__main__":
    st1 = Stack(5)
    st2 = Stack(5)
    st1.push(10)
    st1.push(20)
    st1.push(30)
    st1.display()
    st1.pop()
    print("Top element is:",st1.peek())
#     st2.push(100)
#     st2.push(200)   
#     st2.display()
#     print("Top element is:",st2.peek())
#     st2.pop()
#     st2.pop()
#     st2.display()
#     print(st2.top)
    



    



    
    
