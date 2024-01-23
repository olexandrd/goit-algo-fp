import networkx as nx
import matplotlib.pyplot as plt

from graph import nodes, edges
from search_methods import bfs_recursive, dfs_recursive
from draw_methods import draw_binary_tree
from collections import deque


graph = {}

for edge in edges:
    source, target, attributes = edge
    weight = attributes["weight"]

    if source not in graph:
        graph[source] = {}
    if target not in graph:
        graph[target] = {}

    graph[source][target] = weight


def node_color(graph: nx.DiGraph, node_order: list) -> list:
    step = 1 / len(edges)
    for index, node in enumerate(node_order):
        G.nodes[node]["color"] = (0, step * index + 0.3, 0.8 * step * index + 0.3)
    return [G.nodes[node]["color"] for node in G.nodes]


def node_sequence(graph: nx.DiGraph, node_order: list) -> None:
    graph.clear_edges()
    for index, node in enumerate(node_order):
        if (index + 1) < len(node_order):
            graph.add_edge(node, node_order[index + 1])
            graph.edges[node, node_order[index + 1]]["sequence"] = index + 1


G = nx.DiGraph()
G.add_edges_from(edges)


plt.subplot(1, 2, 1)
pos = nx.circular_layout(G, scale=1)

node_sequence(G, bfs_recursive(graph, deque(["Івано-Франківськ"])))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=700,
    font_size=8,
    font_color="black",
    font_weight="bold",
    edge_color="gray",
    width=1.5,
    font_family="Arial",
    node_color=node_color(G, bfs_recursive(graph, deque(["Івано-Франківськ"]))),
)


edge_labels = nx.get_edge_attributes(G, "sequence")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")
plt.title("BFS")

plt.subplot(1, 2, 2)
pos = nx.circular_layout(G, scale=1)
node_sequence(G, dfs_recursive(graph, "Івано-Франківськ"))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=700,
    font_size=8,
    font_color="black",
    font_weight="bold",
    edge_color="gray",
    width=1.5,
    font_family="Arial",
    node_color=node_color(G, dfs_recursive(graph, "Івано-Франківськ")),
)


edge_labels = nx.get_edge_attributes(G, "sequence")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")
plt.title("DFS")

plt.show()

# draw_binary_tree(bfs_recursive(graph, deque(["Київ"])))
