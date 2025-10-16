class Node:
    """Узел односвязного списка"""
    def __init__(self, data):
        self.data = data
        self.next = None

class SListIterator:
    """Итератор для односвязного списка"""
    def __init__(self, slist):
        self.slist = slist
        self.next_node = slist.head  # Следующий узел для возврата
        self.current = None          # Текущий узел (последний возвращенный)

    def has_next(self):
        """Проверяет, есть ли следующий узел"""
        return self.next_node is not None

    def next(self):
        """Возвращает следующий элемент и перемещает итератор"""
        if not self.has_next():
            raise StopIteration("No more elements")
        
        self.current = self.next_node
        self.next_node = self.next_node.next
        return self.current.data

    def add(self, element):
        """Добавляет элемент перед next_node"""
        new_node = Node(element)
        new_node.next = self.next_node

        # Если next_node - голова списка
        if self.next_node == self.slist.head:
            self.slist.head = new_node
        else:
            # Ищем узел, который ссылается на next_node
            node = self.slist.head
            while node.next != self.next_node:
                node = node.next
            node.next = new_node

    def remove(self):
        """Удаляет текущий узел (последний возвращенный next)"""
        if self.current is None:
            raise Exception("No element to remove")

        # Если удаляем голову списка
        if self.slist.head == self.current:
            self.slist.head = self.current.next
        else:
            # Ищем узел, который ссылается на current
            node = self.slist.head
            while node.next != self.current:
                node = node.next
            node.next = self.current.next

        self.current = None

class SList:
    """Односвязный список"""
    def __init__(self):
        self.head = None

    def __str__(self):
        """Строковое представление списка"""
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return '[' + ', '.join(elements) + ']'

    def iterator(self):
        """Создает и возвращает итератор для списка"""
        return SListIterator(self)

# Демонстрация работы
if __name__ == "__main__":
    # Создаем список
    slist = SList()
    
    # Получаем итератор
    it = slist.iterator()
    
    # Добавляем элементы через итератор
    it.add(1)
    it.add(2)
    it.add(3)
    
    print("Список после добавления элементов:", slist)  # [3, 2, 1]
    
    # Создаем новый итератор для обхода
    it2 = slist.iterator()
    
    print("Обход списка:")
    while it2.has_next():
        print(it2.next(), end=" ")  # 3 2 1
    print()
    
    # Создаем итератор для демонстрации удаления
    it3 = slist.iterator()
    it3.next()  # Переходим к первому элементу (3)
    it3.next()  # Переходим ко второму элементу (2)
    
    it3.remove()  # Удаляем второй элемент (2)
    print("После удаления второго элемента:", slist)  # [3, 1]
    
    # Демонстрация добавления в середину
    it4 = slist.iterator()
    it4.next()  # Переходим к первому элементу (3)
    it4.add(2.5)  # Добавляем после первого элемента
    
    print("После добавления 2.5:", slist)  # [3, 2.5, 1]