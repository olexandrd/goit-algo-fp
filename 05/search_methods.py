def bfs_transversal(root):
    queue = [root]
    order = []
    while queue:
        node = queue.pop(0)
        order.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def dfs_transversal(root):
    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


if __name__ == "__main__":
    print("Do not run this file")
