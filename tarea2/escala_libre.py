import networkx as nx 
import matplotlib.pyplot as plt 
#red de escala libre
#algoritmo obtenido de geekforgeeks
def barabasi_albert_graph(n,m,seed=None):
	#n: numero de nodos
	#m: numero de enlaces para unirse desde un nuevo nodo a los nodos
	#	existentes
	#seed: semilla opcional para generador de numeros aleatorios
	if m<1 or m>=n:
		raise nx.NetworkXError("Condiciones erroneas")
	if seed is not None:
		random.seed(seed)
	G3=empty_graph(m)
	objetivos=list(range(m))
	repeated_nodes=[]
	source=m
	while source<n:
		G3.add_edges_from(zip(*m,objetivos))
		repeated_nodes.extend(objetivos)
		repeated_nodes.extend(*m)
		objetivos= _random_subset(repeated_nodes,m)
		source +=1
	return G3
G3=nx.barabasi_albert_graph(20,15)
print("Dibujando red...")
nx.draw(G3,with_labels=True,node_color="green")
print("guardando imagen de la red escala libre")
plt.savefig("red_escala_libre.png")
