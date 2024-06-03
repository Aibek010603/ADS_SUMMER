class Stack:
    def _init_(self):
        self.items = []  # Инициализация пустого списка для хранения элементов стека

    def push(self, item):
        self.items.append(item)  # Добавление элемента в конец списка

    def pop(self):
        if not self.is_empty():  # Проверка, что стек не пуст
            return self.items.pop()  # Удаление и возврат последнего элемента списка (вершина стека)
        else:
            return None  # Возвращение None, если стек пуст

    def peek(self):
        if not self.is_empty():  # Проверка, что стек не пуст
            return self.items[-1]  # Возвращение последнего элемента списка (вершина стека)
        else:
            return None  # Возвращение None, если стек пуст

    def is_empty(self):
        return len(self.items) == 0  # Проверка, пуст ли список

    def size(self):
        return len(self.items)  # Возвращение количества элементов в списке (размер стека)


# Тестирование реализации стека
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Стек:", stack.items)
print("Извлеченный элемент из стека:", stack.pop())
print("Последний элемент в стеке:", stack.peek())