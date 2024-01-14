class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        self.children = [child for child in self.children if child is not node]

    def find_node(self, data):
        if self.data == data:
            return self
        for child in self.children:
            node = child.find_child(data)
            if node:
                return node
        return None


class Tree:
    def __init__(self):
        self.root = None

    def find(self, data):
        if self.root:
            return self.root.find_child(data)
        return None

    def add(self, parent_data, data):
        if not self.root:
            self.root = Node(parent_data)
            return self.root.add_child(Node(data))

        parent_node = self.find(parent_data)
        if parent_node:
            parent_node.add_child(Node(data))

    def delete(self, data):
        if not self.root:
            return

        if self.root.data == data:
            self.root = None
            return

        nodes_to_visit = [self.root]
        while nodes_to_visit:
            current_node = nodes_to_visit.pop()
            for child in current_node.children:
                if child.data == data:
                    current_node.remove_child(child)
                    return
                nodes_to_visit.append(child)

    def count_elements(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0

        count = 1
        for child in node.children:
            count += self.count_elements(child)
        return count


tree = Tree()

tree.add(None, "root")
tree.add("root", "child1")
tree.add("root", "child2")
tree.add("child1", "grandchild1")

found_node = tree.find("child2")
found_node_data = found_node.data if found_node else "Not found"
print(f"Found node data: {found_node_data}")

tree.delete("child2")
found_node = tree.find("child2")
found_node_data = found_node.data if found_node else "Not found"
print(f"Found node data (after deletion): {found_node_data}")

count = tree.count_elements()
print(f"Number of elements of the tree: {count}")
