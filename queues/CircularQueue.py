from queues.CQueueNode import CQueueNode


class CircularQueue:
    def __init__(self):
        self.front = None
        self.back = None

    def peak_first(self):
        if self.front is None:
            return None
        return self.front.get_data()

    def peak_last(self):
        if self.back is None:
            return None
        return self.back.get_data()

    def push(self, data):
        new_node = CQueueNode(data)
        new_node.set_next(None)
        new_node.set_previous(None)
        if self.front is None:
            self.front = new_node
            self.back = new_node
            self.front.set_previous(self.back)
            self.front.set_next(self.back)
            self.back.set_next(self.front)
            self.back.set_previous(self.front)
        else:
            self.back.set_next(new_node)
            new_node.set_previous(self.back)
            new_node.set_next(self.front)
            self.back = new_node

    def pop(self):
        if self.front is None:
            return None
        to_return = self.front
        self.front = to_return.get_next()
        if self.front is None:
            self.back = None
        else:
            self.front.set_previous(self.back)
            self.back.set_next(self.front)
        return to_return

    def size(self):
        count = 1
        if self.front is None:
            return 0
        node_to_count = self.front
        while node_to_count != self.back:
            count = count + 1
            node_to_count = node_to_count.get_next()
        return count

    def is_empty(self):
        if self.front is None:
            return True
        return False

    def _print_forward_one(self):
        node_to_count = self.front
        print("------")
        print(str(self.front.get_data()))
        while node_to_count != self.back:
            node_to_count = node_to_count.get_next()
            print(str(node_to_count.get_data()))
        print("------")

    def print_forward(self, times):
        print("---Start---")
        for i in range(0, times):
            self._print_forward_one()
        print("--Finish---")

    def _print_backward_one(self):
        node_to_count = self.back
        print("------")
        print(str(self.back.get_data()))
        while node_to_count != self.front:
            node_to_count = node_to_count.get_previous()
            print(str(node_to_count.get_data()))
        print("------")

    def print_backward(self, times):
        print("---Start---")
        for i in range(0, times):
            self._print_backward_one()
        print("--Finish---")
