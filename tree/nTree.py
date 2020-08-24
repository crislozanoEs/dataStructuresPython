from tree.node import Node


class NTree:

    def __init__(self, root_node=Node):
        self.root_node = root_node

    def setRoot_node(self, root_node):
        self.root_node = root_node
        self.root_node.set_parent(None)

    def traversal_preorder(self):
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

    def traversal_inorder(self, node=Node, visited_nodes=[]):
        if node is None:
            return
        if node.get_children() is not None:
            tam = len(node.get_children())
            if tam == 1:
                self.traversal_inorder(node.get_children()[0], visited_nodes)
            for pos in range(0, tam - 1):
                self.traversal_inorder(node.get_children()[pos], visited_nodes)
            visited_nodes.append(node)
            if tam > 1:
                self.traversal_inorder(node.get_children()[tam - 1], visited_nodes)
        else:
            visited_nodes.append(node)

    def init_traversal_inorder(self):
        result = []
        self.traversal_inorder(self.root_node, result)
        return result

    def traversal_postorder(self, node=Node, visited_nodes=[]):
        if node is None:
            return
        if node.get_children() is not None:
            tam = len(node.get_children())
            for pos in range(0, tam):
                self.traversal_postorder(node.get_children()[pos],visited_nodes)
            visited_nodes.append(node)
        else:
            visited_nodes.append(node)

    def init_traversal_post_order(self):
        result = []
        self.traversal_postorder(self.root_node, result)
        return result



