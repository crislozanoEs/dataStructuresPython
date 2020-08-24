from stack.StackNode import StackNode


class Stack:
    def __init__(self, top=StackNode):
        self.top = None

    def peak(self):
        if self.top is None:
            return None
        return self.top.get_data()

    def push(self, data):
        new_node = StackNode(data)
        new_node.set_next(None)
        if self.top is None:
            self.top = new_node
        else:
            new_node.set_next(self.top)
            self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        to_return = self.top
        new_top = to_return.get_next()
        self.top = new_top
        to_return.set_next(None)
        return to_return

    def reverse(self):
        new_stack = Stack()
        while self.top is not None:
            to_return = self.top
            new_stack.push(to_return.get_data())
            new_top = self.top.get_next()
            self.top = new_top
        self.top = new_stack.top
        new_stack = None
