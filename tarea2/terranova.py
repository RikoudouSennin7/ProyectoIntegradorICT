import networkx as nx 
import matplotlib.pyplot as plt 
#red completa de n nodos
#terranova otra prepa donde fuí
lista_enlaces_terranova=[
	("Daniela","Isur"),
	("Daniela","Ernesto"),
	("Daniela","Edgar"),
	("Isur","Daniel"),
	("Isur","Edgar"),
	("Ernesto","Sebastian"),
	("Sebastian","Daniela"),
	("Jazmin","Sebastian")
]
G2=nx.Graph(lista_enlaces_terranova)
print("Dibujando red...")
nx.draw(G2,with_labels=True,node_color="purple")
print("guardando imagen de la red 2 en formato png")
plt.savefig("red_terranova.png")