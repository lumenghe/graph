
import numpy, random, tempfile, subprocess, shlex, heapq
from operator import itemgetter


class MatrixGraph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.tree_edges = []

    def create_priority_queue(self, root):
        self.tree = []
        priority_queue = []
        priority_queue = self.update_priority_queue(priority_queue, root, None)
        self.total_cost = 0
        return priority_queue

    def create_heapqueue(self, root):
        heapqueue = []
        self.total_cost = 0
        self.tree = [root]
        self.tree_edges = []
        for neighbor, cost in self.get_neighbors(root):
     #   cost should be the first item in heapqueue because queue is sorted by the first item
            heapq.heappush(heapqueue, (cost, root, neighbor))
        return heapqueue

    def create_edges(self):
        self.colors = {}
        edges = []
        self.tree_edges = []
        self.total_cost = 0
        for node in xrange(len(self.matrix)):
            self.colors[node] = node

        for (node_1, node_2), cost in numpy.ndenumerate(self.matrix):
            if node_1 < node_2 and cost:
                edges.append((node_1, node_2, cost))
        edges = sorted(edges, key=itemgetter(2))
        return edges

    def display(self, filename):
        with tempfile.NamedTemporaryFile(delete=False) as tmpf:
            tmpf.write("graph Prim{\n node [fontname=\"Arial\"];\n")
            for node in xrange(len(self.matrix)):
                tmpf.write("node%d [label=\"%d\" style=filled fillcolor=white];\n" % (node, node))
            for (node_1, node_2, cost) in self.tree_edges:
                tmpf.write("node%d--node%d [label=\"%d\"];\n" % (node_1, node_2, cost))
            tmpf.write("}")

        cmd = "dot -Tpng -o %s %s" % (filename, tmpf.name)
        args = shlex.split(cmd)
        subprocess.Popen(args)
        return

    def get_neighbors(self, node):
        for n in range(len(self.matrix)):
            if n < node and self.matrix[n][node]:
                yield n, self.matrix[n][node]
            elif n > node and self.matrix[node][n]:
                yield n, self.matrix[node][n]

    def update_priority_queue(self, priority_queue, new_node, new_edge):
        for neighbor, cost in self.get_neighbors(new_node):
            if neighbor in self.tree:
                priority_queue.remove((min(new_node, neighbor), max(new_node, neighbor), cost))
            else:
                priority_queue.append((min(new_node, neighbor), max(new_node, neighbor), cost))

        if new_edge:
            self.tree_edges.append(new_edge)
            self.total_cost += new_edge[2]
        self.tree.append(new_node)
        return priority_queue
