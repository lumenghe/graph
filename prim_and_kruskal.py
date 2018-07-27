
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
