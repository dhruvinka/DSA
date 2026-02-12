f=None
r=None
size=None
q=None

def init(s):
    global f,r,size,q
    f=-1
    r=-1
    size=s
    q=[None]*size

def is_full():
    global f,r,size,q
    return  r+1==size

def is_empty():
    global f,r,size,q
    return  r==-1 and f==-1

def Enqueue(val):
    global f,r,size,q
    if is_full():
        print("Queue is Full")
    else:
        if f==-1:
            f+=1
        r+=1
        q[r]=val

def Dequeue():
    global f,r,size,q
    if is_empty():
        print("Queue is empty")
    else:
            if f==r:
                 q[f]=None
                 f=-1
                 r=-1
            else:
                val=q[f]
                q[f]=None
                f+=1
                return val
    
def display():
        global f,r,size,q
        print(q)
        print(f)
        print(r)


    
init(5)
Enqueue(1)
Enqueue(2)
Enqueue(3)
Enqueue(4)
Enqueue(5)
display()

Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
display()

            





