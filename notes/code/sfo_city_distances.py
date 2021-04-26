import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("distances.csv")
G = nx.Graph()

print(G)
for row in df.iterrows():
    to, d = row[1]
    G.add_node('San Francisco')
    G.add_node(to)
    G.add_edge('San Francisco',to,distance=d)

# This just draws the graph with distances as edge labels
# Pick one of the next layouts
layout = 'circular'
layout = 'spiral'
layout = 'fruchterman_reingold'
nodes = list(G.nodes)
edges = list(G.edges)
if layout=='circular':
    positions = nx.circular_layout(G)
elif layout=='spiral':
    positions = nx.spiral_layout(G)
else:
    positions = nx.fruchterman_reingold_layout(G)

plt.figure(figsize=(15,15))
nx.draw_networkx_edges(G, positions, width=.3)
nx.draw_networkx_nodes(G, positions, node_size=5)
nx.draw_networkx_labels(G, positions, font_size=7)
edge_labels = nx.get_edge_attributes(G, 'distance')
nx.draw_networkx_edge_labels(G, positions,
                             edge_labels=edge_labels,
                             font_size=5)
plt.ylim(-1,1)
plt.xlim(-1,1)
plt.axis("off")
plt.savefig(f"/Users/parrt/Desktop/distances-{layout}.pdf", bbox_inches="tight", pad_inches=0)
plt.show()