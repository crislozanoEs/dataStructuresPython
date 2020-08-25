class CQueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def set_data(self, data):
        self.data = data

    def set_next(self, node):
        self.next = node

    def set_previous(self, node):
        self.previous = node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous