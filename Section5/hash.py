# This program implements a hash table data structure.

class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size
		self.items = 0

	def put(self, key, value):
		position = self.hashFunction(key)

		if self.slots[position] == None:
			self.slots[position] = key
			self.data[position] = value
			self.items += 1
		else:
			count = 1
			while count < self.size:
				position = self.hashFunction(key) + count
				if position > self.size - 1:
					position = count - 1
				if count > self.size:
					break
				elif self.slots[position] == None:
					self.slots[position] = key
					self.data[position] = value
					self.items += 1
					return
					break
				else:
					count += 1

	def get(self, key):
		position = self.hashFunction(key)

		if self.slots[position] == None:
			return None
		elif self.slots[position] == key:
			return self.data[position]
		else:
			count = 1
			while True:
				position = self.hashFunction(key) + count
				if position > self.size - 1:
					position = count - 1
				if count > self.size:
					return None
					break
				elif self.slots[position] == key:
					return self.data[position]
				else:
					count += 1

	def set(self, key, value):
		position = self.hashFunction(key)

		if self.slots[position] == None:
			self.slots[position] = key
			self.data[position] = value
		elif self.slots[position] == key:
			self.data[position] = value
		else:
			count = 1
			while True:
				position = self.hashFunction(key) + count
				if position > self.size - 1:
					position = count - 1
				if count > self.size:
					break
				elif self.slots[position] == key:
					self.data[position] = value
					break
				elif self.slots[position] == None:
					self.slots[position] = key
					self.data[position] = value
					return
					break
				else:
					count += 1

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, value):
		self.set(key, value)

	def __len__(self):
		return self.items

	def __contains__(self, key):
		if self.get(key) == None:
			return False
		return True

	def __delitem__(self, key):
		position = self.hashFunction(key)
		if self.slots[position] == key:
			self.slots[position] = None
			self.data[position] = None
		else:
			count = 1
			while True:
				position = self.hashFunction(key) + count
				if position > self.size - 1:
					position = count - 1
				if count > self.size:
					break
				elif self.slots[position] == key:
					self.slots[position] = None
					self.data[position] = None
				else:
					count += 1

	def hashFunction(self, key):
		hashValue = key % self.size
		return hashValue


def main():
	h = HashTable()
	h[54] = "cat"
	h[26] = "dog"
	h[93] = "lion"
	h[17] = "tiger"
	h[77] = "bird"
	h[31] = "cow"
	h[44] = "goat"
	h[55] = "pig"
	h[20] = "chicken"
	print(h.slots)
	print(h.data)
	h[20] = "duck"
	print(h[20])
	print(h.data)
	print(h.slots)

if __name__ == "__main__":
	main()
