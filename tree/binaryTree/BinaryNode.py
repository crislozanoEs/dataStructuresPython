class BinaryNode:
    def __init__(self, data, children=None):
        if children is None:
            children = [2]
        self.data = data
        if len(children) > 2:
            self.children = children(0,1)
        self.parent = None
        self.weight = None
        self.set_children(children)

    def set_children(self, children=None):
        if children is None:
            children = [2]
        self.children = children

    def add_children(self, child, position=True, replace=False):
        pos = 1
        if position:
            pos = 0
        inserted = replace
        if replace:
            self.children[pos] = child
        else:
            if self.children[pos] is None:
                self.children[pos] = child
                inserted = True
        return inserted


