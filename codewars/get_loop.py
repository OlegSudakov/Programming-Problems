# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863

def loop_size(node):
    if not isinstance(node, Node):
        return None
    if (node == None):
        return 0
    if (node.next == None):
        return 1
    visited_nodes = {}
    current_node = node
    current_step = 0
    while True:
        try:
            if visited_nodes[current_node] > 0:
                loop_size = current_step - visited_nodes[current_node]
                break
        except KeyError:
            pass
        visited_nodes[current_node] = current_step
        current_node = current_node.next
        current_step += 1
    return loop_size
