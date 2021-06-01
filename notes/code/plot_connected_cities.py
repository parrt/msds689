import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

FILTER=False
if FILTER:
    df = pd.read_csv("flights.csv")
    G = nx.Graph()
    for row in df.sample(500).iterrows():
        src,trg = row[1]
        G.add_node(src)
        G.add_node(trg)
        G.add_edge(src,trg)

    largest_cc = max(nx.connected_components(G), key=len)
    G = G.subgraph(largest_cc).copy()
    # print('\n'.join(G.nodes))
    nx.write_edgelist(G, "flights_subset.csv", delimiter=',', data=False)
else:
    df = pd.read_csv("flights_subset.csv")
    G = nx.DiGraph()
    for row in df.iterrows():
        src,trg = row[1]
        G.add_node(src)
        G.add_node(trg)
        G.add_edge(src,trg)

print("Built")

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
plt.savefig(f"/Users/parrt/Desktop/connected-{layout}.pdf", bbox_inches="tight", pad_inches=0)
plt.show()