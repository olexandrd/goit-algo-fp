import uuid
from copy import copy

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def insert_to_tree(root, key, color):
    if root is None:
        return Node(key, color=color)
    else:
        if key < root.val:
            root.left = insert_to_tree(root.left, key, color=color)
        else:
            root.right = insert_to_tree(root.right, key, color=color)
    return root


def generate_colormap(data: list) -> list:
    step = 0.9 / len(data)
    colormap = [(0.8, (step * x), (step * x)) for x in (range(1, len(data) + 1))]
    return colormap


def build_binary_tree(node_list: list):
    colormap = generate_colormap(node_list)
    node_dict = zip(node_list, colormap)
    root = None
    for node, color in node_dict:
        root = insert_to_tree(root, node, color)
    return root


def drawing(nodes):
    root = build_binary_tree(nodes)
    draw_tree(root)


if __name__ == "__main__":
    data = [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17 ,19, 21, 23, 25, 27, 29, 31]
    drawing(data)