class Node:
    """ Класс узла связанного списка Node """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return f"Элементы узла: данные - '{self.data}'"


class LinkedList:
    """ Класс одно связанного списка """

    def __init__(self, node: Node = None):
        if node is None:
            self.head = None
        else:
            self.head = node

    def __str__(self):
        elements = []
        cursor = self.head
        while cursor:
            elements.append(str(cursor.data))
            cursor = cursor.next
        return " -> ".join(elements)

    def __len__(self):
        cursor = self.head
        count = 0
        while cursor:
            count += 1
            cursor = cursor.next
        return count

    def __getitem__(self, item):
        """ Получение элемента по индексу """
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом")
        if self.is_empty():
            raise ValueError("Ошибка. Список пустой")
        self.verify_index(item)

        cursor = self.head
        index = 0
        while cursor and index < item:
            cursor = cursor.next
            index += 1
        return cursor

    def __add__(self, other):
        """ Сложение списков """
        if not isinstance(other, LinkedList):
            raise TypeError("Операнд должен быть типом LinkedList")
        if other.is_empty():
            return self.head
        if self.is_empty():
            return other
        else:
            cursor = other.head
            while cursor:
                self.append(cursor.data)
                cursor = cursor.next
            return self

    def verify_index(self, index: int):
        if index < 0 or index >= len(self):
            raise IndexError("Ошибка. Неверный индекс или меньше 0")

    def is_empty(self):
        return self.head is None

    def append(self, data):
        """ Добавление элемента в конец списка """
        new_node = Node(data, None)
        if self.is_empty():
            self.head = new_node
        else:
            cursor = self.head
            while cursor.next:
                cursor = cursor.next
            cursor.next = new_node

    def append_node(self, node: Node):
        """ Добавление элемента в конец списка, уже созданного элемента """
        if self.is_empty():
            self.head = node
        else:
            cursor = self.head
            while cursor.next:
                cursor = cursor.next
            cursor.next = node

    def insert_by_index(self, data, index: int):
        """
        Добавление элемента по индексу списка
        :param data : данные нового узла списка
        :param index: индекс списка
       """
        self.verify_index(index)

        new_node = Node(data, None)
        if index == 0:
            new_node.next = self.head.next
            self.head.next = new_node
        else:
            cursor = self.__getitem__(index - 1)
            new_node.next = cursor.next
            cursor.next = new_node

    def insert_node(self, new_node: Node, index: int):
        """
        Добавление элемента по индексу списка
        :param new_node : новый узел списка
        :param index: индекс списка
        """
        self.verify_index(index)

        if index == 0:
            new_node.next = self.head.next
            self.head.next = new_node
        else:
            cursor = self.__getitem__(index - 1)
            new_node.next = cursor.next
            cursor.next = new_node

    def remove_by_index(self, index: int):
        """
        Удаление элемента по индексу списка
        :param index: индекс списка
       """
        self.verify_index(index)

        if index == 0:
            cursor = self.head
            self.head = self.head.next
            cursor.next = None
        else:
            cursor = self.__getitem__(index - 1)
            delete_node = cursor.next
            cursor.next = delete_node.next
            delete_node.next = None

    def delete_element(self, data):
        """
        Удаление элемента по значению данных в элементе
        :param data: значение
       """
        if self.is_empty():
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        cursor = self.head
        while cursor.next:
            if cursor.next.data == data:
                delete_node = cursor.next
                cursor.next = delete_node.next
                delete_node.next = None
                return
            cursor = cursor.next

    def is_present_element(self, data):
        """
        Проверка наличия элемента, по значению данных в элементе
        :param data: значение
       """
        if self.is_empty():
            return False
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


if __name__ == "__main__":
    my_list = LinkedList()
    # search_node = my_list[5]  # Проверка ошибки IndexError

    my_list.append(1)
    my_list.append(2)
    my_list.append(3)

    search_node = my_list[2]
    print("Поиск по индексу. ", search_node)

    print(f'Количество элементов в списке - {len(my_list)}')
    print(my_list)  # Вывод: 1 -> 2 -> 3
    my_list.delete_element(2)
    print(f'Количество элементов в списке - {len(my_list)}')
    print(my_list)  # Вывод: 1 -> 3
    print(my_list.is_present_element(3))  # Вывод: True
    print(my_list.is_present_element(2))  # Вывод: False

    my_list.insert_by_index(888, 1)
    print(my_list)  # Вывод: 1 -> 888 -> 3
    my_list.insert_node(Node(999), 2)
    print(my_list)  # Вывод: 1 -> 888 -> 999 -> 3

    print("Удаление узлов")
    # my_list.remove_by_index(4)  # Проверка ошибки IndexError
    my_list.remove_by_index(0)
    print(my_list)  # Вывод: 888 -> 999 -> 3
    my_list.remove_by_index(1)
    print(my_list)  # Вывод: 888 -> 3
    my_list.remove_by_index(1)
    print(my_list)  # Вывод: 888

    print("Добавление узлов Node")
    my_node = Node(777)
    new_list = LinkedList(my_node)
    print(my_list)  # Вывод: 777
    new_list.append_node(Node(7777))
    print(f'Количество элементов в списке - {len(new_list)}')
    print(new_list)  # Вывод: 777 -> 7777
    new_list.insert_node(Node(999), 1)
    print(new_list)  # Вывод: 777 -> 999 -> 7777
    print(f'Количество элементов в списке - {len(new_list)}')

    print("Сложение списков")
    my_list = my_list + new_list
    print(my_list)  # Вывод: 888 -> 777 -> 999 -> 7777
    print(new_list)  # Вывод: 777 -> 999 -> 7777
    print(new_list + my_list)  # Вывод: 777 -> 999 -> 7777 -> 888 -> 777 -> 999 -> 7777
