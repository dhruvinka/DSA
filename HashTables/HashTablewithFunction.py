
class SimpleHashTable:
	def __init__(self, capacity=8):
		self.capacity = capacity
		self.buckets = [[] for _ in range(capacity)]
		self.count = 0  # Number of stored key-value pairs.

	def _hash(self, key):
		key_str = str(key)
		hash_value = 0
		for i, ch in enumerate(key_str):
			hash_value += (i + 1) * ord(ch)
		return hash_value % self.capacity

	def insert(self, key, value):
		index = self._hash(key)
		bucket = self.buckets[index]

		for pair in bucket:
			if pair[0] == key:
				pair[1] = value
				return

		bucket.append([key, value])
		self.count += 1

	def get(self, key):
		index = self._hash(key)
		bucket = self.buckets[index]

		for pair in bucket:
			if pair[0] == key:
				return pair[1]
		return None

	def delete(self, key):
		index = self._hash(key)
		bucket = self.buckets[index]

		for i, pair in enumerate(bucket):
			if pair[0] == key:
				del bucket[i]
				self.count -= 1
				return True
		return False

	def load_factor(self):
		return self.count / self.capacity

	def display(self):
		print("\nHash Table State:")
		for i, bucket in enumerate(self.buckets):
			print(f"Bucket {i}: {bucket}")


if __name__ == "__main__":
	ht = SimpleHashTable(capacity=7)

	print("Inserting key-value pairs...")
	ht.insert("name", "Himanshu")
	ht.insert("city", "Nadiad")
	ht.insert("course", "Data Structures")
	ht.insert("age", 19)

	ht.display()
	print(f"\nLoad Factor: {ht.load_factor():.2f}")

	print("\nRetrieving keys:")
	print("name ->", ht.get("name"))
	print("city ->", ht.get("city"))
	print("unknown ->", ht.get("unknown"))

	print("\nUpdating 'city' and deleting 'age'...")
	ht.insert("city", "Ahmedabad")
	ht.delete("age")

	ht.display()
	print(f"\nLoad Factor after update/delete: {ht.load_factor():.2f}")
