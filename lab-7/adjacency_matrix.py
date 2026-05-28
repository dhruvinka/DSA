class adjacency_matrix:
    def __init__(self,num_vertices):
        self.vertices=num_vertices
        self.matrix=[[0 for i in range(num_vertices)]for i in range(num_vertices)]
        # self.matrix=[]
        # or

        # for i in range(num_vertices):
        #     e=[]
        #     for j in range(num_vertices):
        #         e.append(0)
        #     self.matrix.
        # 
        # append(e)

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

    def count_degree(self):
         d={}
         for i in range(len(self.matrix)):
             count=0
             for j in range(len(self.matrix)):
                  if self.matrix[i][j] == 1:
                       count+=1
             d[i]=count
         print(d)

    def count_edge_list(self):
         d=[]
         for i in range(len(self.matrix)):
             for j in range(len(self.matrix)):
                  if self.matrix[i][j] == 1:
                       d.append((i,j))
         print(d)


    def bfs(self,start_ver):
         if start_ver >= self.vertices or start_ver <0:
              return
         
         visited=[False]*self.vertices
         queue=[start_ver]
         visited[start_ver]=True
         result=[]

         while queue:
              vertex=queue.pop(0)
              result.append(vertex)

              for i in range(len(self.matrix)):
                   if self.matrix[vertex][i] == 1 and not visited[i]:
                        visited[i]=True
                        queue.append(i)
         return result
    
    def dfs(self, start_ver):
        if start_ver >= self.vertices or start_ver < 0:
            return []

        visited = [False] * self.vertices
        result = []

        def dfs_util(v):
            visited[v] = True
            result.append(v)

            for i in range(self.vertices):
                if self.matrix[v][i] == 1 and not visited[i]:
                    dfs_util(i)

        dfs_util(start_ver)
        return result
    
    
    def dfs_stack(self, start_ver):
        if start_ver >= self.vertices or start_ver < 0:
            return []

        visited = [False] * self.vertices
        stack = [start_ver]
        result = []

        while stack:
            vertex = stack.pop()

            if not visited[vertex]:
                visited[vertex] = True
                result.append(vertex)

                # push in reverse order to match recursive DFS order else normal loop
                for i in range(self.vertices - 1, -1, -1):
                    if self.matrix[vertex][i] == 1 and not visited[i]:
                        stack.append(i)

        return result
                    


al=adjacency_matrix(5)
al.add_edge(2,3)
al.add_edge(1,3)
al.add_edge(1,0)
al.add_edge(2,0)
al.display()
# al.remove_edge(2,3)
# al.display()
al.count_degree()
al.count_edge_list()
# print(al.bfs(0))
# print(al.dfs(0))
print(al.dfs_stack(0))


