class hashing_DoubleHashing:
    def __init__( self):
        self.size = 15
        self.table = [None] * self.size

    def hash_function(self,data):
        return data % self.size
     
    def hash_function2(self,data):
        return 7 - (data % 7)
    
    def insert(self,data):
        index = self.hash_function(data)
        
        i = 1
        while self.table[index] is not None:
                index = (index + i * self.hash_function2(data)) % self.size
                i += 1
        self.table[index] = data
        
        
    def search(self,data):
        index=self.hash_function(data)
        
        if self.table[index] is None:
            return False
        else:
            i = 1
            while self.table[index] is not None:
                if self.table[index] == data:
                    return index
                index = (index + i * self.hash_function2(data)) % self.size
                i += 1

                if i == self.size:  
                    return False
                    
            return False


if __name__ == "__main__":
    hash_table = hashing_DoubleHashing()
    hash_table.insert(1)
    hash_table.insert(2)
    hash_table.insert(3)
    hash_table.insert(4)
    # hash_table.insert(4)
    hash_table.insert(5)
    hash_table.insert(6)
    hash_table.insert(7)
    # hash_table.insert(7)
    print(hash_table.table)
    print(hash_table.search(2))  
    print(hash_table.search(4))
    