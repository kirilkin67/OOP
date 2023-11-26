class Stack:
    """ Определяем класс Stack """

    def __init__(self):
        self.queue = list()

    def __str__(self):
        elements = ', '.join(map(str, self.queue))
        return f"Элементы очереди: {elements}"

    def put(self, element):
        self.queue.append(element)

    def get(self):
        if self.is_empty():
            raise IndexError("Очередь пустая")
        else:
            return self.queue.pop(0)

    def clear(self):
        return self.queue.clear()

    def is_empty(self):
        return len(self.queue) == 0


if __name__ == "__main__":
    my_queue = Stack()
    my_queue.put("Я первый")
    my_queue.put("Я второй")
    my_queue.put("Я третий")
    print(my_queue)
    print("Очередь пустая: ", my_queue.is_empty())
    print(my_queue.get())
    print(my_queue)
    print(my_queue.get())
    print(my_queue)
    print(my_queue.get())
    print(my_queue)
    print("Очередь пустая: ", my_queue.is_empty())
    my_queue.put(5)
    my_queue.put(14)
    print(my_queue)
    my_queue.clear()
    print("Очередь пустая: ", my_queue.is_empty())
