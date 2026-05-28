class Stack:
    def __init__(self,size):
        self.stack=[None]*size
        self.top=-1
        self.size=size


    def is_full(self):
        return self.top==self.size-1
    
    def is_Empty(self):
        return self.top==-1

    def push(self,data):
        if self.is_full():
            print("full")
        else:
            self.top+=1
            self.stack[self.top]=data

    def pop(self):
        if self.is_Empty():
            print("empty")
        else:
            data=self.stack[self.top]
            self.stack[self.top]=None
            self.top-=1
            return data
        
    def peek(self):
        if self.is_Empty():
            print("empty")
        else:
            data=self.stack[self.top]
            return data
        

    
# if __name__ == "__main__":
#     stack=Stack(5)
#     stack.push(1)
#     stack.push(2)   
#     stack.push(3)
#     stack.push(4)
#     stack.push(5)
#     print(stack.stack)
#     print(stack.peek())
#     print(stack.pop())
#     print(stack.stack)

        

    