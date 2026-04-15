class SimpleIntHashTable:
	def __init__(self, capacity=10):
		self.capacity = capacity
		self.buckets = [[] for _ in range(capacity)]
		self.count = 0

	def _hash(self, value):
		return value % self.capacity

	def insert(self, value):
		if not isinstance(value, int):
			raise TypeError("Value must be an integer.")

		index = self._hash(value)
		bucket = self.buckets[index]

		if value not in bucket:
			bucket.append(value)
			self.count += 1

	def search(self, value):
		if not isinstance(value, int):
			raise TypeError("Value must be an integer.")

		index = self._hash(value)
		return value in self.buckets[index]

	def delete(self, value):
		if not isinstance(value, int):
			raise TypeError("Value must be an integer.")

		index = self._hash(value)
		bucket = self.buckets[index]

		if value in bucket:
			bucket.remove(value)
			self.count -= 1
			return True
		return False

	def values_at_index(self, index):
		if not isinstance(index, int):
			raise TypeError("Index must be an integer.")
		if index < 0 or index >= self.capacity:
			raise IndexError("Index out of range.")
		return self.buckets[index]

	def load_factor(self):
		return self.count / self.capacity

	def display(self):
		print("\nHash Table State (index acts as key):")
		for i, bucket in enumerate(self.buckets):
			print(f"Index {i}: {bucket}")


if __name__ == "__main__":
	ht = SimpleIntHashTable(capacity=7)

	print("Inserting integer values only...")
	ht.insert(10)
	ht.insert(17)
	ht.insert(24)
	ht.insert(3)
	ht.insert(31)

	ht.display()
	print(f"\nLoad Factor: {ht.load_factor():.2f}")

	print("\nSearching values:")
	print("10 present? ->", ht.search(10))
	print("24 present? ->", ht.search(24))
	print("99 present? ->", ht.search(99))

	print("\nValues at index 3 ->", ht.values_at_index(3))

	print("\nDeleting value 3...")
	ht.delete(3)

	ht.display()
	print(f"\nLoad Factor after delete: {ht.load_factor():.2f}")
