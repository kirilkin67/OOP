class Tree:
    """
    Класс Tree представляет собой бинарное дерево,
    где каждый узел содержит значение и ссылки на левое и правое поддеревья.
    Метод insert() добавляет новый узел в дерево.
    Методы inorder(), preorder() и postorder() выполняют обход дерева в порядке возрастания,
    в порядке убывания и в обратном порядке соответственно.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.insert(value)

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.value)
        if self.right is not None:
            self.right.inorder()

    def preorder(self):
        print(self.value)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.value)


if __name__ == "__main__":
    root = Tree(10)
    root.insert(5)
    root.insert(3)
    root.insert(7)
    root.insert(2)
    root.insert(4)

    root.inorder()
    # Вывод: 4 2 5 3 7 10

    root.preorder()
    # Вывод: 10 5 3 2 4 7

    root.postorder()
    # Вывод: 4 2 3 5 7 10
