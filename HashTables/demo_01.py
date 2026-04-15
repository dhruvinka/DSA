class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)

        while self.table[index] is not None:
            index = (index + 1) % self.size

        self.table[index] = key

    def search(self, key):
        index = self.hash_function(key)

        start = index

        while self.table[index] is not None:
            if self.table[index] == key:
                return True

            index = (index + 1) % self.size

            if index == start:
                return False

        return False
    
    def delete(self, key):
        index = self.hash_function(key)

        start = index

        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = None
                return True

            index = (index + 1) % self.size

            if index == start:
                return False

        return False
    
    def display(self):
        for i, val in enumerate(self.table):
            print(f"Index {i}: {val}")

if __name__ == "__main__":
    ht = HashTable(10)

    print("Inserting values...")
    ht.insert(15)
    ht.insert(25)
    ht.insert(35)

    print("\nHash Table after insertions:")
    ht.display()

    print("\nSearching for values...")
    print("Search 25:", ht.search(25))
    print("Search 30:", ht.search(30))

    print("\nDeleting a value...")
    print("Delete 25:", ht.delete(25))
    print("Delete 30:", ht.delete(30))

    print("\nHash Table after deletions:")
    ht.display()

    # ht = HashTable(10)

    # ht.insert(23)
    # ht.insert(33)
    # ht.insert(43)

    # ht.display()

    # print("Search 33:", ht.search(33))

    # ht.delete(33)
    # ht.display()