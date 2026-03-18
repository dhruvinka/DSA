class adjacency_matrix:
    def __init__(self,num_vertices):
        self.vertices=num_vertices
        # self.matrix=[[0 for i in range(num_vertices)]for i in range(num_vertices)]
        self.matrix=[]
        # or

        for i in range(num_vertices):
            e=[]
            for j in range(num_vertices):
                e.append(0)
            self.matrix.append(e)

    def display(self):
        for i in range(len(self.matrix)):
            print(i, end="   ")
            for j in range(len(self.matrix)):
                print(self.matrix[i][j],end=" ")
            print()
        print()

    def add_edge(self,u,v):
            #check that v is present or not 
            if 0 <= u < self.vertices and 0 <= v < self.vertices:
                        self.matrix[u][v]=1
                        self.matrix[v][u]=1
            else:
                 print("Invalid vertices")
    

    def remove_edge(self,u,v):
       if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.matrix[u][v]=0
            self.matrix[v][u]=0
       else:
                 print("Invalid vertices")

    def countedge(self):
         d={}
         for i in range(len(self.matrix)):
             count=0
             for j in range(len(self.matrix)):
                  if self.matrix[i][j] == 1:
                       count+=1
             d[i]=count
         print(d)
                       
                       




al=adjacency_matrix(5)
al.add_edge(2,3)
al.display()
# al.remove_edge(2,3)
al.display()
al.countedge()