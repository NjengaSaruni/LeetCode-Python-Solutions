from trees.utilities import get_mock_tree


def pre_order_traversal(root):
    stack = []
    pre_order = []
    stack.append(root)
    while len(stack):
        node = stack.pop(0)
        pre_order.append(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return pre_order

def post_order_traversal(root):

    stack = []
    post_order = []

    if root.left:
        stack.append(root.left)
    if root.right:
        stack.append(root.right)
    stack.append(root)


    while len(stack):
        node = stack.pop(0)
        post_order.append(node.value)




if __name__ == '__main__':
    root = get_mock_tree(height=4)

    print(pre_order_traversal(root))
    print(post_order_traversal(root))

