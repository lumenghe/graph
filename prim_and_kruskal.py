
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
