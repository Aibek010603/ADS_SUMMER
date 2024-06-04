class Deque:
    def _init_(self):
        self.items = []  # Создаем пустой список для дека

    def addFront(self, item):
        self.items.append(item)  

    def addRear(self, item):
        self.items.insert(0, item)  

    def removeFront(self):
        if not self.isEmpty():  
            return self.items.pop()  # Удаление и возврат последнего элемента из списка 
        else:
            return None  

    def removeRear(self):
        if not self.isEmpty():  
            return self.items.pop(0)  
        else:
            return None  

    def isEmpty(self):
        return len(self.items) == 0  # Проверка, пуст ли список

    def size(self):
        return len(self.items)  # Возвращение количества элементов в списке (размер дека)


deque = Deque()
deque.addFront(1)
deque.addRear(2)
deque.addFront(3)
print("Дек:", deque.items)
print("Удаленный элемент спереди из дека:", deque.removeFront())
print("Удаленный элемент сзади из дека:", deque.removeRear())