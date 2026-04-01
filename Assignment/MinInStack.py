# 4. Design a MinStack that supports below operations in O(1) time. 
# ● push(x) 
# ● pop() 
# ● peek() 
# ● getMin() → return minimum element 
# Note: Try without using any auxiliary stack. 
class Stack:
    def __init__(self,size):
        self.s = []
        self.size=size
        self.top = -1
        self.minvalue=0

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.size - 1
    
    def push(self, data):
        if self.isFull():
            print("Stack full")
        else:
            if self.top == -1:
                self.minvalue = data
            x=min(data,self.minvalue)
            self.minvalue=x
            self.s.append((data,x))
            # print(x,self.minvalue)
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
        
    def minvalinstack(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            x=self.s[self.top]  
            return x[1]
        
    
        
if __name__=="__main__":
    st1 = Stack(5)
    st1.push(50)
    st1.push(5)
    st1.push(10)
    st1.display()
    st1.pop()
    print("Min :",st1.minvalinstack())
