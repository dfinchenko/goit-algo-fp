import matplotlib.pyplot as plt
import networkx as nx
import uuid
import time

class Node:
    def __init__(self, key, color="#FFFFFF"):  # Початковий колір - білий
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def generate_colors(n):
    colors = []
    for i in range(n):
        intensity = int(255 - (i * 255 / n))  # Від темного до світлого
        colors.append(f"#00{intensity:02x}{intensity:02x}")
    return colors

def reset_colors(node, color="#FFFFFF"):  # Білий колір за замовчуванням
    if node:
        node.color = color
        reset_colors(node.left, color)
        reset_colors(node.right, color)


def update_node_color(node, color, tree_root, pos):
    node.color = color
    draw_tree(tree_root, pos, pause_time=1)  # Динамічне оновлення з затримкою

def dfs(node, colors, pos, tree_root, index=[0]):
    if node is not None:
        update_node_color(node, colors[index[0]], tree_root, pos)
        index[0] += 1
        dfs(node.left, colors, pos, tree_root, index)
        dfs(node.right, colors, pos, tree_root, index)

def bfs(root, colors, pos):
    queue = [root]
    color_index = 0
    while queue:
        current_node = queue.pop(0)
        if current_node is not None:
            update_node_color(current_node, colors[color_index], root, pos)
            color_index += 1
            queue.append(current_node.left)
            queue.append(current_node.right)

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, pos, pause_time=0):
    tree = nx.DiGraph()
    tree = add_edges(tree, tree_root, pos)
    
    plt.close()
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_size=10)
    plt.pause(pause_time)  # Показуємо вікно з затримкою

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Підготовка до візуалізації
pos = {root.id: (0, 0)}
add_edges(nx.DiGraph(), root, pos)

# Підготовка кольорів
colors = generate_colors(6)

# Візуалізація DFS
plt.ion()
dfs(root, colors, pos, root)
plt.show(block=False)
time.sleep(2)
plt.close()  # Закриваємо вікно DFS

# Візуалізація BFS
reset_colors(root)
bfs(root, generate_colors(6), pos)
plt.show()