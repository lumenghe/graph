import tempfile, shlex, subprocess

class Node:
    def __init__(self, value, pointers):
        self.value = value
        self.pointers = pointers
