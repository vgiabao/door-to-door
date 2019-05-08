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


class Two_opt(Graph):
    def __init__(self):
        Graph.__init__(self)

    def two_opt(self):
        best = self.nodes[:]
        min = 0
        improve = True
        def re_calculate(item):
            lene = 0
            for index in range(-1, len(item) - 1):
                lene += item[index].get_distance(item[index + 1])
            return lene

        while improve:
            improve = False
            for i in range(1, len(self.nodes) - 2):
                for j in range(i + 2, len(self.nodes)):
                    reflect = self.nodes[:]
                    old_len = re_calculate(best)
                    reflect[i:j] = self.nodes[j-1:i-1:-1]
                    new_len = re_calculate(reflect)
                    if new_len < old_len:
                        best = reflect
                        min = new_len
                        improve = True
                self.nodes = best
        return '\n'.join([str(item) for item in best]), min

