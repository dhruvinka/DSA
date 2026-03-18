class adjacency_list:
    def __init__(self,num_vertices):
        self.vertices=num_vertices
        # self.list=[[] for i in range(num_vertices)]
        # or
        self.list={i:[] for i in range(num_vertices)}

    def display(self):
        for i in range(self.vertices):
            print(i,"",self.list[i])

    def add_edge(self,u,v):
           if self.is_present(u,v):
                self.list[u].append((v,1))
                self.list[v].append((u,1))
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




al=adjacency_list(5)
print(al.list)
al.add_edge(2,3)
# al.add_edge(2,3)
al.display()
al.remove_edge(3,2)
al.display()
# print(al.list[3])

# al.is_present(2,3)
# al.display()
