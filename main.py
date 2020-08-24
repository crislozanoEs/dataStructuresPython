from arrays.ArrayUtilities import ArrayUtilities
from stack.Stack import Stack
from tree.node import Node
from tree.NTree import NTree
from queues.NormalQueue import NormalQueue


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
            print("Node to return " + str(node))
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
    tree = NTree(node1)
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
    result_BFS = tree.traversal_preorder()
    print("Preorder traveler")
    for r in result_BFS:
        print(str(r.get_data()))

    print("Inorder traveler")
    result_inorder = tree.init_traversal_inorder()
    for r in result_inorder:
        print(str(r.get_data()))

    print("Postorder traveler")
    result_KDF = tree.init_traversal_post_order()
    for r in result_KDF:
        print(str(r.get_data()))

    print("-----Arrays-----")
    array = [2, 1, -7, 4, 5]
    arrayUtility = ArrayUtilities(array, 5)

    arrayUtility.rotate_array(10, False)
    print("Rotated")
    for element in arrayUtility.array:
        print(str(element))

    arrayUtility.init_quick_sort(False)
    print("Sorted")
    for element in arrayUtility.array:
        print(str(element))

    result = arrayUtility.search_max()
    print("The max element is " + str(result))

    result = arrayUtility.search_min()
    print("The min element is " + str(result))

    looking_for_element = 80
    position_result = arrayUtility.init_binary_search(looking_for_element)
    print("Find the " + str(looking_for_element) + " in the position " + str(position_result))

    print("-----Stack-----")
    stack = Stack()
    stack.push("2")
    stack.push("3")
    stack.push("1")
    print("TOP STACK " + str(stack.peak()))

    stack.reverse()
    print("TOP STACK " + str(stack.peak()))

    print("-----Normal Queue-----")
    queue = NormalQueue()
    queue.push("1")
    print("FRONT LINE" +str(queue.peak_first()))
    print("BACK LINE" +str(queue.peak_back()))
    queue.push("2")
    print("FRONT LINE" + str(queue.peak_first()))
    print("BACK LINE" + str(queue.peak_back()))
    queue.push("3")
    print("FRONT LINE" + str(queue.peak_first()))
    print("BACK LINE" + str(queue.peak_back()))

    print("SIZE "+str(queue.size()))

