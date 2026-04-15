class hashing_QuadraticProbing:
        def __init__(self):
            self.size = 7
            self.table = [None] * self.size

        def hash_function(self, data):
                return data % self.size
        
        def insert(self,data):
               index=self.hash_function(data)
               i=1
               while self.table[index] is not None:
                      index=(index+i**2) % self.size
                      i+=1
               self.table[index]=data

        def search(self,data):
                index=self.hash_function(data)
                i=1
                while self.table[index] is not None:
                        if self.table[index]==data:
                                return index
                        index=(index+i**2) % self.size
                        i+=1
                return False
        
        def delete(self,data):
                index=self.hash_function(data)
                i=1
                while self.table[index] is not None:
                        if self.table[index]==data:
                                self.table[index]=None
                                return True
                        index=(index+i**2) % self.size
                        i+=1
                return False


if __name__ == "__main__":
    hash_table = hashing_QuadraticProbing()
    hash_table.insert(10)
    hash_table.insert(20)
    hash_table.insert(30)
    hash_table.insert(40)
    hash_table.insert(50)
    hash_table.insert(60)
    hash_table.insert(70)
    print(hash_table.table)
    print(hash_table.search(20))  
    print(hash_table.search(40)) 
