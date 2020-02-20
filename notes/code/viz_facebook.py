import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from random import sample

# Download from https://snap.stanford.edu/data/facebook_combined.txt.gz

# Read with networkx:
G = nx.read_edgelist('/Users/parrt/data/facebook_combined.txt')
# Or with pandas and then subsample to get smaller (88k records)
# BUT, it samples edges not nodes
# df = pd.read_csv('/Users/parrt/data/facebook_combined.csv')
# df = df.sample(frac=.03) # subsample
# G = nx.from_pandas_edgelist(df, source='user1', target='user2')

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

# subsample_nodes_idx = sample(nodes, 1000)
# G = G.subgraph(subsample_nodes_idx)
subsample_edges_idx = sample(edges, 2300)
G = G.edge_subgraph(subsample_edges_idx)

nx.draw_networkx_edges(G, positions, width=.05)
nx.draw_networkx_nodes(G, positions, node_size=.1)
plt.ylim(-1,1)
plt.xlim(-1,1)
plt.axis("off")
plt.savefig(f"/Users/parrt/Desktop/fb-{layout}.pdf", bbox_inches="tight", pad_inches=0)
plt.show()