class Stack:
    def __init__(self,size):
        self.size=size
        self.top=None
        self.stack=None

    def dis(self):
        print("Size",self.size,"top",self.top,"stack",self.stack)
    
    def init(self):
        self.stack=[]
        self.top=-1
