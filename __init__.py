__author__ = 'Soroush'

import networkx as nx

g = nx.Graph()
g.add_edge('A', 'B', weight=4)
g.add_edge('B', 'D', weight=2)
g.add_edge('A', 'C', weight=3)
g.add_edge('C', 'D', weight=4)
print(nx.shortest_path(g, 'A', 'D', weight='weight'))

print('soroush kazemi')