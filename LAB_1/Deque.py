class Deque:
    def _init_(self):
        self.items = []  # Инициализация пустого списка для хранения элементов дека

    def addFront(self, item):
        self.items.append(item)  # Добавление элемента в конец списка

    def addRear(self, item):
        self.items.insert(0, item)  # Добавление элемента в начало списка

    def removeFront(self):
        if not self.isEmpty():  # Проверка, что дек не пуст
            return self.items.pop()  # Удаление и возврат последнего элемента из списка (спереди)
        else:
            return None  # Возвращение None, если дек пуст

    def removeRear(self):
        if not self.isEmpty():  # Проверка, что дек не пуст
            return self.items.pop(0)  # Удаление и возврат первого элемента из списка (сзади)
        else:
            return None  # Возвращение None, если дек пуст

    def isEmpty(self):
        return len(self.items) == 0  # Проверка, пуст ли список

    def size(self):
        return len(self.items)  # Возвращение количества элементов в списке (размер дека)


# Тестирование реализации дека
deque = Deque()
deque.addFront(1)
deque.addRear(2)
deque.addFront(3)
print("Дек:", deque.items)
print("Удаленный элемент спереди из дека:", deque.removeFront())
print("Удаленный элемент сзади из дека:", deque.removeRear())