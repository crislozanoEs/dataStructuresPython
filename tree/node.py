class Node:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children
        self.parent = None
        self.weight = None
        self.set_children(children)

    def set_children(self, children):
        self.children = children
        if self.children is not None:
            for h in self.children:
                h.parent = self

    def set_parent(self, parent):
        self.parent = parent

    def set_data(self, data):
        self.data = data

    def set_weight(self, weight):
        self.weight = weight

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def get_weight(self):
        return self.weight

    def get_data(self):
        return self.data

    def same(self, node):
        if self.get_data() == node.get_data():
            return True
        else:
            return False

    def in_list(self, node_list):
        in_the_list = False
        for node in node_list:
            in_the_list = self.same(node)
        return in_the_list

    def __str__(self):
        return str(self.get_data())


