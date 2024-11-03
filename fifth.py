import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color 
        self.id = str(uuid.uuid4()) 
        self.traversal_index = None 


def add_edges_iterative(graph, root):
    """
    Додає вузли та ребра до графа, використовуючи ітеративний підхід замість рекурсії.
    """
    pos = {}
    stack = [(root, 0, 0, 1)] 
    while stack:
        node, x, y, layer = stack.pop()
        if node:
            graph.add_node(node.id, color=node.color, label=node.val, node_obj=node)
            pos[node.id] = (x, y)
            if node.left:
                graph.add_edge(node.id, node.left.id)
                l = x - 1 / 2 ** layer
                stack.append((node.left, l, y - 1, layer + 1))
            if node.right:
                graph.add_edge(node.id, node.right.id)
                r = x + 1 / 2 ** layer
                stack.append((node.right, r, y - 1, layer + 1))
    return pos


def draw_tree(tree_root, title=''):
    tree = nx.DiGraph()
    pos = add_edges_iterative(tree, tree_root)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {}
    for node_id, data in tree.nodes(data=True):
        label = str(data['label'])
        node_obj = data['node_obj']
        if node_obj.traversal_index is not None:
            label += f"\n({node_obj.traversal_index})"
        labels[node_id] = label

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def dfs_traversal_with_colors(root):
    stack = []
    traversal_order = []
    visited = set()
    stack.append(root)
    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            traversal_order.append(node)
            visited.add(node.id)
            stack.append(node.right)
            stack.append(node.left)
    assign_colors_and_indices(traversal_order)


def bfs_traversal_with_colors(root):
    queue = deque()
    traversal_order = []
    visited = set()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if node and node.id not in visited:
            traversal_order.append(node)
            visited.add(node.id)
            queue.append(node.left)
            queue.append(node.right)
    assign_colors_and_indices(traversal_order)


def assign_colors_and_indices(traversal_order):
    N = len(traversal_order)
    colormap = cm.get_cmap('Blues', N)
    for idx, node in enumerate(traversal_order):
        color = mcolors.rgb2hex(colormap(idx / (N - 1))) if N > 1 else mcolors.rgb2hex(colormap(0))
        node.color = color
        node.traversal_index = idx + 1 


def reset_tree_iterative(root):
    """
    Скидає кольори та індекси вузлів, використовуючи ітеративний підхід.
    """
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.color = "skyblue"
            node.traversal_index = None
            stack.append(node.right)
            stack.append(node.left)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    dfs_traversal_with_colors(root)
    draw_tree(root, title='Обхід у глибину (DFS)')

    reset_tree_iterative(root)

    bfs_traversal_with_colors(root)
    draw_tree(root, title='Обхід у ширину (BFS)')


if __name__ == "__main__":
    main()
