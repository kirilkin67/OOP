from collections import deque


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
        else:
            print("Вершина уже существует в графе")

    def add_edge(self, start, end):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].append(end)
            self.vertices[end].append(start)
        else:
            print("Одна или обе вершины отсутствуют в графе")

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            del self.vertices[vertex]
            for connections in self.vertices.values():
                if vertex in connections:
                    connections.remove(vertex)
        else:
            print("Вершина отсутствует в графе")

    def remove_edge(self, start, end):
        if start in self.vertices and end in self.vertices:
            if end in self.vertices[start]:
                self.vertices[start].remove(end)
                self.vertices[end].remove(start)
            else:
                print("Ребро не существует")
        else:
            print("Одна или обе вершины отсутствуют в графе")

    def shortest_path(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            print("Одна или обе вершины отсутствуют в графе")
            return

        queue = deque([(start, [start])])
        visited = set()

        while queue:
            current, path = queue.popleft()
            visited.add(current)

            if current == end:
                return path

            for neighbor in self.vertices[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        print("Кратчайший путь не найден")
        return
