import uuid
from copy import copy

import networkx as nx
import matplotlib.pyplot as plt

from constants import data32 as data

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


def generate_colormap(data: list) -> dict:
    step = 0.8 / len(data)
    colormap = {element: (0.8, step * index, step * index) for index, element in enumerate(data)}
    return colormap


def insert_to_tree(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert_to_tree(root.left, key)
        else:
            root.right = insert_to_tree(root.right, key)
    return root


def build_binary_tree(node_list: list):
    root = None
    for node in node_list:
        root = insert_to_tree(root, node)
    return root

def change_node_color(node, colormap):
    if node is not None:
        node.color = colormap[node.val]
        change_node_color(node.left, colormap)
        change_node_color(node.right, colormap)

def drawing(nodes):
    root = build_binary_tree(nodes)
    draw_tree(root)


if __name__ == "__main__":
    drawing(data)