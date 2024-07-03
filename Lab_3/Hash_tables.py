class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    del self.table[index][i]
                    return True
        return False

if __name__ == "__main__":
    ht = HashTable()
    ht.insert("apple", "fruit")
    ht.insert("carrot", "vegetable")
    ht.insert("python", "programming language")
    print("apple:", ht.get("apple"))  # Output: fruit
    print("carrot:", ht.get("carrot"))  # Output: vegetable
    print("python:", ht.get("python"))  # Output: programming language
    ht.delete("carrot")
    print("carrot after deletion:", ht.get("carrot"))  # Output: None
