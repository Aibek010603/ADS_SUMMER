class Queue:
    def _init_(self):
        self.items = []  # Инициализация пустого списка для хранения элементов очереди

    def enqueue(self, item):
        self.items.append(item)  # Добавление элемента в конец списка

    def dequeue(self):
        if not self.is_empty():  # Проверка, что очередь не пуста
            return self.items.pop(0)  # Удаление и возврат первого элемента из списка (передняя часть очереди)
        else:
            return None  # Возвращение None, если очередь пуста

    def is_empty(self):
        return len(self.items) == 0  # Проверка, пуст ли список

    def size(self):
        return len(self.items)  # Возвращение количества элементов в списке (размер очереди)


# Тестирование реализации очереди
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Очередь:", queue.items)
print("Извлеченный элемент из очереди:", queue.dequeue())