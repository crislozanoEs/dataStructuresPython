from tree.node import Node


class nTree:

    def __init__(self, root_node=Node):
        self.root_node = root_node

    def setRoot_node(self, root_node):
        self.root_node = root_node
        self.root_node.set_parent(None)

    def travel_BFS(self):
        visited_nodes = []
        edge_nodes = [self.root_node]
        while len(edge_nodes) != 0:
            node = edge_nodes.pop(0)
            visited_nodes.append(node)
            if node.get_children() is not None:
                for son_node in node.get_children():
                    if not son_node.in_list(visited_nodes) and not son_node.in_list(edge_nodes):
                        edge_nodes.append(son_node)
        return visited_nodes

    def travel_inorder(self, node=Node, visited_nodes=[]):
        if node is None:
            return
        if node.get_children() is not None:
            tam = len(node.get_children())
            for pos in range(0, tam - 1):
                self.travel_inorder(node.get_children()[pos],visited_nodes)
            visited_nodes.append(node)
            self.travel_inorder(node.get_children()[tam - 1],visited_nodes)
        else:
            visited_nodes.append(node)

    def init_travel_inorder(self):
        result = []
        self.travel_inorder(self.root_node, result)
        return result

    def travel_KDF(self, node=Node, visited_nodes=[]):
        if node is None:
            return
        if node.get_children() is not None:
            tam = len(node.get_children())
            for pos in range(0, tam):
                self.travel_KDF(node.get_children()[pos],visited_nodes)
            visited_nodes.append(node)
        else:
            visited_nodes.append(node)

    def init_travel_KDF(self):
        result = []
        self.travel_KDF(self.root_node, result)
        return result



