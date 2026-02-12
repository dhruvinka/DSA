size=None
f=None
r=None
queue=None

def init(s):
    global f,r,queue,size
    size=s
    f=-1
    r=-1
    queue=[None]*size

def is_empty():
    global f,r
    if f==-1 and r==-1:
        return True
    return False

def is_full():
    global r,size
    if r==size-1:
        return True
    return False

def push(val):
    global f,r,queue
    if is_full():
        print("Queue is full")
        return
    if f==-1:
        f=0
    r+=1
    queue[r]=val

def pop():
    global f,r,queue
    if is_empty():
        print("Queue is empty")
        return
    val=queue[f]
    queue[f]=None
    if f==r:
        f=-1
        r=-1
    else:
        f+=1
    return val

def display():
    global f,r,queue
    print(queue)
    print(f)
    print(r)

def peek():
    global f,queue
    return queue[f]

def destroy():
    global f,r,queue
    f=None
    r=None
    queue=None

if __name__=="__main__":
    init(10)
    display()
    push(30)
    display()
    print(peek())