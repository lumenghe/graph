import tempfile, shlex, subprocess
import numpy as np


class MatrixGraph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.reset_color_and_distance()

    def reset_color_and_distance(self):
        self.color = ["white" for node in range(len(self.matrix))]
        self.distance = [None for node in range(len(self.matrix))]

    def display(self, filename):
        with tempfile.NamedTemporaryFile(delete=False) as tmpf:
            tmpf.write("graph BFS {\nnode [fontname=\"Arial\"];\n")
            for node in range(len(self.matrix)):
                label = str(self.distance[node]) if self.distance[node] else "*"
                tmpf.write("node%d [label=\"%s\" style=filled fillcolor=%s];\n" % (node, label, self.color[node]))
            for (x, y), value in np.ndenumerate(self.matrix):
                if value and x>=y:
                    tmpf.write("node%d -- node%d;\n" % (x,y))
            tmpf.write("}")
        cmd =  "dot -Tpng -o %s %s" % (filename, tmpf.name)
        args = shlex.split(cmd)
        subprocess.Popen(args)
        return
