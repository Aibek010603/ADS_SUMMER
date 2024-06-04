class Stack:
    def __init__(self):
        self.items = []  # здесь будет храниться элементы стека

    def push(self, item):
        self.items.append(item)  # добавляет элемент в конец списка

    def pop(self):
        if not self.is_empty():  # Проверка, что стек не пуст
            return self.items.pop()  
        else:
            return None  

    def peek(self):
        if not self.is_empty():  
            return self.items[-1]  
        else:
            return None  

    def is_empty(self):
        return len(self.items) == 0  

    def size(self):
        return len(self.items)  # Возвращение количества элементов в списке (размер стека)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Стек:", stack.items)
print("Извлеченный элемент из стека:", stack.pop())
print("Последний элемент в стеке:", stack.peek())