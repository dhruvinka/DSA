class Stack:

    def __init__(self,size):
        self.size=size
        self.stack=[None]*size
        self.top=-1

    def is_empty(self):
        return self.top==-1
    
    def is_full(self):
        return self.top==self.size-1
    
    def push(self,data):
        if self.is_full():
            print("Stack is full")
        else:
            if self.top==-1:
                self.top+=1
            else:
                self.top+=1
            self.stack[self.top]=data

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            data=self.stack[self.top]
            self.stack[self.top]=None
            self.top-=1
            return data
        
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack[self.top]


if __name__ == "__main__":
    s=Stack(5) 
    s.push(10)
    s.push(20) 
    s.push(30) 
    s.push(40) 
    s.push(50)
    print(s.peek())
    print(s.pop())
    print(s.peek())
    print(s.stack) 
        