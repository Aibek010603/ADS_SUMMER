class Queue:
    def __init__(self):
        self.items = []  # Хранение элементов в кью

    def enqueue(self, item):
        self.items.append(item)  # Добавление элемента в конец списка

    def dequeue(self):
        if not self.is_empty():  
            return self.items.pop(0) 
        else:
            return None  # Возвращение None, если очередь пуста

    def is_empty(self):
        return len(self.items) == 0 

    def size(self):
        return len(self.items)  # Возвращение количества элементов в списке (размер очереди)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Очередь:", queue.items)
print("Извлеченный элемент из очереди:", queue.dequeue())