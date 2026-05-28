class GraphUsingMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def add_edge(self, u, v):
        if u >= self.V or v >= self.V:
            print("Invalid vertices")
            return
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def Dfs_Traversal(self,start):
        if start >= self.V:
            print("Invalid start vertex")
            return
        
        visited = [False] * self.V
        res=[]
        stack = [start]

        while stack:
            vertex=stack.pop()

            if not visited[vertex] :
                visited[vertex]=True
                res.append(vertex)
                
                for i in range(self.V -1,-1,-1):
                    if self.graph[vertex][i] == 1 and not visited[i]:
                        stack.append(i)
                        
        return res
    
    def Dfs_using_Recrsion(self,start):
        if start >= self.V:
            print("Invalid start vertex")
            return
        
        visited = [False] * self.V
        res=[]
       

        def helper(start_ver):
            visited[start_ver]=True
            res.append(start_ver)

            for i in range(self.V):
                if self.graph[start_ver][i] == 1 and not visited[i]:
                    helper(i)
        helper(start)
        return res

    
    def Bfs_Traversal(self,start):
        if start >= self.V:
            print("Invalid start vertex")
            return
        
        visited = [False] * self.V
        res=[]
        visited[start]=True
        q = [start]

        while q:
            vertex=q.pop(0)
            res.append(vertex)

            for i in range(self.V):
                if self.graph[vertex][i] == 1 and not visited[i]:
                    visited[i]=True
                    q.append(i)
        return res



    def print_graph(self):
        for row in self.graph:
            print(row)

if __name__ == "__main__":
    g=GraphUsingMatrix(5)
    g.add_edge(0,1)
    # g.add_edge(0,3)
    g.add_edge(0,2)
    g.add_edge(1,3)
    g.add_edge(1,0)
    g.add_edge(1,4)
    g.print_graph()
    print("Dfs Traversal:", g.Dfs_Traversal(0))
    print("Dfs Traversal usinf Recursion:", g.Dfs_using_Recrsion(0))
    print("Bfs Traversal:", g.Bfs_Traversal(0))
