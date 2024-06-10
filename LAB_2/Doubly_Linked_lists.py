class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, node):
        if not self.head:
            return

        if node == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def traverse_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

# Пример использования двусвязного списка
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)

print("Обход вперед:")
dll.traverse_forward()  # Вывод: 0 1 2 3

print("Обход назад:")
dll.traverse_backward()  # Вывод: 3 2 1 0

# Удаление узла
dll.delete(dll.head.next)  # Удаление узла со значением 1
print("После удаления узла со значением 1:")
dll.traverse_forward()  # Вывод: 0 2 3
