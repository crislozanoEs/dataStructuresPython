from queues.NQueueNode import NQueueNode


class NormalQueue:
    def __init__(self, top=NQueueNode):
        self.front = None
        self.back = None

    def peak_first(self):
        if self.front is None:
            return None
        return self.front.get_data()

    def peak_back(self):
        if self.back is None:
            return None
        return self.back.get_data()

    def push(self, data):
        new_node = NQueueNode(data)
        new_node.set_next(None)
        if self.front is None:
            self.front = new_node
            self.back = new_node
        else:
            self.back.set_next(new_node)
            self.back = new_node

    def size(self):
        count = 1
        if self.front is None:
            return 0
        node_to_count = self.front
        while node_to_count != self.back:
            count = count + 1
            node_to_count = node_to_count.get_next()
        return count

    def pop(self):
        if self.front is None:
            return None
        to_return = self.front
        self.front = to_return.get_next()
        if self.front is None:
            self.back = None
        return to_return
