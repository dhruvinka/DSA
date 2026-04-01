import heapq

class adjacency_list:
    def __init__(self,num_vertices):
        self.vertices=num_vertices
        # self.list=[[] for i in range(num_vertices)]
        # or
        self.list={i:[] for i in range(num_vertices)}

    def display(self):
        for i in range(self.vertices):
            print(i,"",self.list[i])

    def add_edge(self,u,v,wight):
           if self.is_present(u,v):
                self.list[u].append((v,wight))
                self.list[v].append((u,wight))
           else:
               print("ege is already exit")

    def remove_edge(self, u, v):
        if not self.is_present(u, v):
                print(self.list[u])
                # remove v in the u lists
                self.list[u].remove((v,1))
                # remove v in the u lists  1 is value  values is either 0 or 1 if it presetn then 1 is there
                self.list[v].remove((u,1))
        else:
            print("Edge does not exist between u to u")
         

    def is_present(self, u, v):
        # check if v is already in u 
        # extract vertice bcz we store vertice and 1 both so node is vertice and val is  1
        for node, val in self.list[u]:
            if node == v:
                return False   
        return True
    
    def count_edge(self):
        count=0
        # print(self.list)
        for i in range(len(self.list)):
            count+=len(self.list[0])
        print(count)

    def count_edge_of_each_vertex(self):
        count=0
        # print(self.list)
        d={}
        for i in range(len(self.list)):
            count=len(self.list[0])
            d[i]=count

        print(d)
            


    def bfs(self,start_ver):
         #use q
        
         if start_ver >= self.vertices or start_ver <0:
              return
         
         visited=[False] * self.vertices
         queue=[start_ver]
         visited[start_ver]=True
         result=[]

         while queue:
              vertex=queue.pop(0)
              result.append(vertex)

              for nei,val in self.list[vertex]:
                   if not visited[nei]:
                        visited[nei]=True
                        queue.append(nei)
         return result
    

    def dfs_recursive(self, start_ver):
        if start_ver >= self.vertices or start_ver < 0:
            return 
        
        visited = [False] * self.vertices
        result = []
        self.dfs_helperfun(start_ver, visited, result)
        return result
    

    def dfs_helperfun(self, vertex, visited, result):
        visited[vertex] = True
        result.append(vertex)
        
        for nei, val in self.list[vertex]:
            if not visited[nei]:
                self.dfs_helperfun(nei, visited, result)

                

    #step -1  false to all visited node
    #step -2   create result [] for store res
    #step-3  enter staring node in result list
    #step-4  while stack is not empty run loop 
    #         pop the last element  store in to var
    #         if it is not visited then True and add in to result
    #         and check ther neighbors and push it in to stack if it is not visitad
    #         if we want to output like recursion then used reversd else not
    #         for nei, val in reversed(self.list[vertex]):  


    def dfs_using_stack(self, start_ver):
        if start_ver >= self.vertices or start_ver < 0:
            return []

        visited = [False] * self.vertices
        result = []
        stack = [start_ver]

        while stack:
            vertex = stack.pop()

            if not visited[vertex]:
                visited[vertex] = True
                result.append(vertex)
                
                for nei, val in self.list[vertex]:
                    if not visited[nei]:
                        stack.append(nei)

        return result




# use heap q  it will give thhe always get the smallest element .
    def prime_algo(self,start_ver):
        if start_ver >= self.vertices or start_ver < 0:
            return []
        
        visited = [False] * self.vertices
        # root node have always 0 weight so first do also give starting node for perform 
        min_wight=[(0,start_ver)]
        result = []
        totalcost=0
        
        while min_wight:
            # it will give the min wight node 
            wight,node=heapq.heappop(min_wight) 

            if not visited[node]:
                visited[node]=True
                totalcost+=wight

             #now come neighbor for node 
                for neighbor,wight in self.list[node]:
                # neighbor is not visited then add in to heapq
                 if not visited[neighbor]: 
                    heapq.heappush(min_wight,(wight,neighbor))
        return totalcost  






        



                 
        
al=adjacency_list(5)
print(al.list)
al.add_edge(2,3,10)
# al.add_edge(3,2,20)
al.add_edge(1,2,20)
# al.add_edge(2,1,22)
al.add_edge(0,2,30)
al.add_edge(0,1,40)
al.add_edge(1,3,5)
# al.add_edge(2,3)
# al.display()
# al.remove_edge(3,2)
# al.display()
# print(al.list[3])
print("BFS",al.bfs(0))
print("DFS using resersion",al.dfs_recursive(0))
print("DFS using Stack",al.dfs_using_stack(0))
al.count_edge()
al.count_edge_of_each_vertex()
# al.is_present(2,3)
al.display()
print(al.prime_algo(0))
