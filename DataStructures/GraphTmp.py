class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = {}

    def add_edge(self, node1, node2, weight):
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("One or both nodes not found in graph")
        self.nodes[node1][node2] = weight

    def shortest_path(self, start, end):
        if start not in self.nodes or end not in self.nodes:
            raise ValueError("Start or end node not found in graph")

        unvisited_nodes = list(self.nodes.keys())
        shortest_path = {node: float('inf') for node in self.nodes}
        shortest_path[start] = 0

        while unvisited_nodes:

            current_node = min(unvisited_nodes, key=lambda node: shortest_path[node])

            if shortest_path[current_node] == float('inf'):
                break

            for neighbour, weight in self.nodes[current_node].items():
                new_path = shortest_path[current_node] + weight
                if new_path < shortest_path[neighbour]:
                    shortest_path[neighbour] = new_path

            unvisited_nodes.remove(current_node)

        if shortest_path[end] == float('inf'):
            raise ValueError("There's no path between the specified nodes")

        return shortest_path[end]


graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_edge("A", "B", 1)
graph.add_edge("B", "C", 2)
graph.add_edge("A", "C", 4)

try:
    path_length = graph.shortest_path("A", "C")
    print(f"The shortest path from A to C is {path_length}")
except ValueError as e:
    print(e)

try:
    path_length = graph.shortest_path("A", "A")
    print(f"The shortest path from A to A is {path_length}")
except ValueError as e:
    print(e)

try:
    path_length = graph.shortest_path("B", "C")
    print(f"The shortest path from B to C is {path_length}")
except ValueError as e:
    print(e)

try:
    path_length = graph.shortest_path("C", "B")
    print(f"The shortest path from C to B is {path_length}")
except ValueError as e:
    print(e)