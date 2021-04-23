import networkx as nx 
import matplotlib.pyplot as plt 
#red de mundo pequeño
G4= nx.watts_strogatz_graph(n=20,k=2,p=0.5)
print("Dibujando la red...")
nx.draw(G4,with_labels=True,node_color="yellow")
print("guardando imagen de la red de mundo pequeño")
plt.savefig("red_mundo_pequeño.png")