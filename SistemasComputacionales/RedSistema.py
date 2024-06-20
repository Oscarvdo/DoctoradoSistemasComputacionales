import networkx as nx
import matplotlib.pyplot as plt

# Crear un gráfico dirigido
G = nx.DiGraph()

# Añadir nodos
nodos = ['A', 'B', 'C', 'D']
G.add_nodes_from(nodos)

# Añadir aristas con pesos (representando relaciones e interacciones)
aristas = [('A', 'B', 5), ('A', 'C', 3), ('B', 'D', 2), ('C', 'D', 4)]
G.add_weighted_edges_from(aristas)

# Dibujar el gráfico
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=15)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title('Ejemplo de Red de Sistema')
plt.show()
