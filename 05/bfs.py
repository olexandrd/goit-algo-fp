from search_methods import bfs_transversal
from draw_methods import (
    build_binary_tree,
    change_node_color,
    generate_colormap,
    draw_tree,
)
from constants import data32 as data

nodes = build_binary_tree(data)


dfs = bfs_transversal(nodes)
node_colormap = generate_colormap(dfs)
change_node_color(nodes, node_colormap)


draw_tree(nodes)