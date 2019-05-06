from copy import deepcopy

class Graph:
    def __init__(self):
        self.nodes = []

    def __str__(self):
        return '\n'.join([str(node) for node in self.nodes])

    def add_node(self, node):
        self.nodes.append(node)

    def k_nearest_neighbor(self):
        original = deepcopy(self)
        solution = Graph()
        solution.add_node(original.nodes.pop(0))
        total_len = 0
        while original.nodes:
            distance = [solution.nodes[-1].get_distance(node) for node in
                        original.nodes]
            total_len += min(distance)
            solution.add_node(original.nodes.pop(distance.index(
                min(distance))))
            if len(original.nodes) == 1:
                total_len += solution.nodes[0].get_distance(original.nodes[0])
                solution.add_node(original.nodes[0])
                return solution, total_len

    def two_opt(self):
        lene = 0
        for i in range(1, len(self.nodes) - 2):
            for j in range(i + 2 , len(self.nodes)):
                old_distance = self.nodes[i].get_distance(self.nodes[i + 1])
                new_distance = self.nodes[i].get_distance(self.nodes[j])
                if old_distance > new_distance:
                    self.nodes[i+1], self.nodes[j] = self.nodes[j], \
                                                     self.nodes[i + 1]
        for index in range(-1, len(self.nodes) - 1):
            lene += self.nodes[index].get_distance(self.nodes[index + 1])
        return '\n'.join([str(node) for node in self.nodes]), lene



