class Node:

    def __init__(self, key, value, size, color):
        self.key = key
        self.value = value
        self.size = size
        # boolean true for red; None or false for black
        self.color = color

    def is_red(self):
        return bool(self.color)