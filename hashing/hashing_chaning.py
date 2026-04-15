
class hash_chaining:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size
    
    def insert(self,data):
        index=self.hash_function(data)
        self.table[index].append(data)

    def search(self,data):
        index=self.hash_function(data)
        if data in self.table[index]:
            return self.table[index].index(data)
        else:
            return False
    
    def delete(self,data):
        index=self.hash_function(data)
        if data in self.table[index]:
            self.table[index].remove(data)
            return True
        else:
            return False
        
    

if __name__ == "__main__":
    hash_table = hash_chaining()
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
    print(hash_table.delete(40)) 