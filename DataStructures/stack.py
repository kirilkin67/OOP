class Stack:
    """ Определяем класс Stack """

    def __init__(self):
        self.stack = list()

    def __str__(self):
        elements = ', '.join(map(str, self.stack))
        return f"Элементы стека: {elements}"

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пустой")
        else:
            return self.stack.pop()

    def clear(self):
        return self.stack.clear()

    def is_empty(self):
        return len(self.stack) == 0


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(5)
    my_stack.push(12)
    my_stack.push(14)
    print(my_stack)
    print("Стек пустой: ", my_stack.is_empty())
    print(my_stack.pop())
    print(my_stack)
    print(my_stack.pop())
    print(my_stack)
    print(my_stack.pop())
    print(my_stack)
    print("Стек пустой: ", my_stack.is_empty())
    my_stack.push(5)
    my_stack.push(14)
    print(my_stack)
    my_stack.clear()
    print("Стек пустой: ", my_stack.is_empty())
