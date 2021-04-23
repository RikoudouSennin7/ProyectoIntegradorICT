import networkx as nx 
import matplotlib.pyplot as plt 
#red aleatoria
#n: numero de nodos
#p: probabilidad de creacion de enlaces
G5= nx.fast_gnp_random_graph(n=10,p=1.2,seed=None)
print("Dibujando la red...")
nx.draw(G5,with_labels=True,node_color="orange")
print("guardando imagen de la red aleatoria")
plt.savefig("red_aleatoria.png")
