from trees.utilities import get_mock_tree

if __name__ == '__main__':
    root = get_mock_tree(height=4)

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

    print(pre_order)

