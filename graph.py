from collections import defaultdict


class Graph:
    def __init__(self, is_directed):
        self.graph = defaultdict(list)
        self.is_directed = is_directed

    def add_vertex(self, vertex):
        try:
            if vertex not in list(self.graph.keys()):
                self.graph[vertex] = []
            else:
                raise ValueError
        except ValueError:
            print("vertex " + str(vertex) + " already exist")

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in list(self.graph.keys()):
            self.add_vertex(vertex1)
        if vertex2 not in list(self.graph.keys()):
            self.add_vertex(vertex2)
        try:
            if vertex2 not in self.graph[vertex1]:
                self.graph[vertex1].append(vertex2)
                if not self.is_directed:
                    self.graph[vertex2].append(vertex1)
            else:
                raise ValueError
        except ValueError:
            print("edge (" + str(vertex1) + "," + str(vertex2) + ") already exist")

    def del_vertex(self, vertex):
        try:
            if vertex in list(self.graph.keys()):
                del self.graph[vertex]                  # wychodzące krawędzie
                for edge in list(self.graph.keys()):    # wchodzące krawędzie
                    if vertex in self.graph[edge]:
                        self.graph[edge].remove(vertex)
            else:
                raise ValueError
        except ValueError:
            print("cannot delete, vertex " + str(vertex) + " does not exist")

    def del_edge(self, vertex1, vertex2):
        try:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
                if not self.is_directed:
                    self.graph[vertex2].remove(vertex1)
            else:
                raise ValueError
        except ValueError:
            print("cannot delete, edge (" + str(vertex1) + "," + str(vertex2) + ") does not exist")

    def neighbours(self, vertex):
        try:
            if vertex not in list(self.graph.keys()):
                raise ValueError
            else:
                return self.graph[vertex]
        except ValueError:
            print("cannot get neighbourhood, vertex " + str(vertex) + " does not exist")

    def bfs(self, vertex):
        return BfsIterator(self, vertex)

    def dfs(self, vertex):
        return DfsIterator(self, vertex)

    def show_all(self):
        print(self.graph)


class BfsIterator:
    def __init__(self, graph, vertex):
        self.graph = graph
        self.vertex = vertex
        self.visited = defaultdict(None)
        self.queue = [vertex]
        self.visited[vertex] = True

    def __iter__(self):
        return self

    def __next__(self):
        try:
            vertex = self.queue.pop(0)
            for neighbour in self.graph.graph[vertex]:
                if neighbour not in self.visited:
                    self.queue.append(neighbour)
                    self.visited[neighbour] = True
            return vertex
        except IndexError:
            raise StopIteration


class DfsIterator:
    def __init__(self, graph, vertex):
        self.graph = graph
        self.vertex = vertex
        self.visited = defaultdict(None)
        self.queue = [vertex]
        self.visited[vertex] = True
        self._next()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            vertex = self.queue.pop(0)
            return vertex
        except IndexError:
            raise StopIteration

    def _next(self):
        for neighbour in self.graph.graph[self.vertex]:
            if neighbour not in self.visited:
                self.queue.append(neighbour)
                self.visited[neighbour] = True
                self.vertex = neighbour
                self._next()


mygraph = Graph(0)
mygraph.add_vertex(8)
mygraph.add_edge(1, 2)
mygraph.add_edge(1, 2)
mygraph.add_edge(1, 3)


mygraph.show_all()
mygraph.add_edge(2, 4)
mygraph.add_edge(2, 5)
mygraph.add_edge(3, 6)
mygraph.show_all()

mygraph.add_edge(1, 7)
mygraph.add_edge(4, 8)
mygraph.add_edge(8, 1)
mygraph.add_edge(3, 2)

mygraph.show_all()

mygraph.del_vertex(2)
mygraph.show_all()

mygraph.del_edge(3, 6)
mygraph.show_all()
print(mygraph.neighbours(1))
print(mygraph.neighbours(2))
for v in mygraph.bfs(8):
    print(v)
