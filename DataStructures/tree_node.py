class TreeNode:
    """
    Класс представляет узел дерева с методами для добавления, удаления потомков и обхода дерева
    """

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        if child_node in self.children:
            self.children.remove(child_node)
        else:
            raise ValueError("Дочерний узел не найден")

    def find_child(self, data):
        if self.value == data:
            return self

        for child in self.children:
            node = child.find_child(data)
            if node:
                return node
        return None

    def traverse(self):
        """ Прямой обход дерева, с выводом на печать значений"""
        print(self.value)
        for child in self.children:
            child.traverse()

    def count_nodes(self):
        """ Подсчёт количества узлов в дереве """
        count = 1
        for child in self.children:
            count += child.count_nodes()
        return count


if __name__ == "__main__":
    tree = TreeNode("root")

    child_1 = TreeNode([11111, 4444])
    tree.add_child(child_1)
    child_2 = TreeNode(222222)
    child_1.add_child(child_2)
    child_1.add_child(TreeNode([333333, "My Project"]))
    tree.traverse()

    found_node = tree.find_child(222222)
    print(f"Found node data: {found_node.value}")

    child_1.remove_child(child_2)
    tree.traverse()
    found_node = tree.find_child(222222)
    print(f"Found node: {found_node}")

