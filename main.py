from tree.node import Node
from tree.nTree import nTree


def search_BFS(initial_state, solution):
    solved = False
    visited_nodes = []
    edge_nodes = []
    initial_node = Node(initial_state)
    edge_nodes.append(initial_node)
    while (not solved) and len(edge_nodes) != 0:
        node = edge_nodes.pop(0)
        visited_nodes.append(node)
        if node.get_data() == solution:
            solved = True
            print("Node to return "+str(node))
            return node
        else:
            data_node = node.get_data()
            # L
            son = [data_node[1], data_node[0], data_node[2], data_node[3]]
            left_son = Node(son)
            if not left_son.in_list(visited_nodes) and not left_son.in_list(edge_nodes):
                edge_nodes.append(left_son)
            # C
            son = [data_node[0], data_node[2], data_node[1], data_node[3]]
            central_son = Node(son)
            if not central_son.in_list(visited_nodes) and not central_son.in_list(edge_nodes):
                edge_nodes.append(central_son)
            # R
            son = [data_node[0], data_node[1], data_node[3], data_node[2]]
            right_son = Node(son)
            if not right_son.in_list(visited_nodes) and not right_son.in_list(edge_nodes):
                edge_nodes.append(right_son)

            node.set_children([left_son, central_son, right_son])


# Init tree
#          1
#  21          22
# 2131    2231 2232 2233
def initTree():
    node2231 = Node(2231)
    node2232 = Node(2232)
    node2233 = Node(2233)
    node2131 = Node(2131)
    node21 = Node(21)
    node22 = Node(22)
    node21.set_children([node2131])
    node22.set_children([node2231, node2232, node2233])
    node1 = Node(1)
    node1.set_children([node21, node22])
    tree = nTree(node1)
    tree.setRoot_node(node1)
    return tree

def callingBFS_search():
    print("Init program")
    initial_state = [4, 3, 2, 1]
    solution = [1, 2, 3, 4]
    print("Init searching")
    solution_node = search_BFS(initial_state, solution)
    result = []
    node = solution_node
    while node.get_parent() is not None:
        result.append(node.get_data())
        node = node.get_parent()
    result.append(initial_state)
    result.reverse()
    print(result)

if __name__ == '__main__':
    tree = initTree()
    result_BFS = tree.travel_BFS()
    print("BFS traveler")
    for r in result_BFS:
        print(str(r.get_data()))

    print("Inorder traveler")
    result_inorder = tree.init_travel_inorder()
    for r in result_inorder:
        print(str(r.get_data()))

    print("KDF traveler")
    result_KDF = tree.init_travel_KDF()
    for r in result_KDF:
        print(str(r.get_data()))