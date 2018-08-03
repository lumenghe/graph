import tempfile, shlex, subprocess
import numpy as np


class MatrixGraph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.reset_color_and_distance()

    def reset_color_and_distance(self):
        self.color = ["white" for node in range(len(self.matrix))]
        self.distance = [None for node in range(len(self.matrix))]
