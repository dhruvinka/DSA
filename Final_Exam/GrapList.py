class GraphList:
    def __init__(self, size):
        self.vertext = size
        self.list = {i: [] for i in range(size)}

    def display(self):
        for i in range(self.vertext):
            print(i, "->", self.list[i])

    def add_edge(self, u, v):
        if self.is_present(u, v):
            self.list[u].append(v)
            self.list[v].append(u)
        else:
            print("Edge already present")

    def is_present(self, u, v):
        return v not in self.list[u]

    #DFS
    def dfs(self, start):
        visited = [False] * self.vertext
        res = []
        stack = [start]

        while stack:
            vertex = stack.pop()

            if not visited[vertex]:
                visited[vertex] = True
                res.append(vertex)

                for i in reversed(self.list[vertex]):
                    if not visited[i]:
                        stack.append(i)

        return res

    #  DFS recursive
    def dfs_res(self, start):
        visited = [False] * self.vertext
        res = []

        def helper(v):
            visited[v] = True
            res.append(v)

            for i in self.list[v]:
                if not visited[i]:
                    helper(i)

        helper(start)
        return res

    #  BFS
    def bfs(self, start):
        visited = [False] * self.vertext
        res = []
        q = [start]

        visited[start] = True

        while q:
            vert = q.pop(0)
            res.append(vert)

            for i in self.list[vert]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)

        return res


# TEST
if __name__ == "__main__":
    al = GraphList(5)

    al.add_edge(2,3)
    al.add_edge(1,2)
    al.add_edge(0,2)
    al.add_edge(0,1)
    al.add_edge(1,3)
    al.add_edge(1,3)

    al.display()

    print("DFS Recursive:", al.dfs_res(0))
    print("DFS Iterative:", al.dfs(0))
    print("BFS:", al.bfs(0))