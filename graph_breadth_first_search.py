import tempfile, shlex, subprocess
import numpy as np


class MatrixGraph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.reset_color_and_distance()
