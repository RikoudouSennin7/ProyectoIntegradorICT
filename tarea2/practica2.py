import networkx as nx 
import matplotlib.pyplot as plt 
print("Este programa realizará la creación de las redes deseadas en la tarea 2")
#red donde todos los nodos tienen el mismo grado
#declaración de la lista de enlaces
#lem es una preparatoria donde fuí
lista_enlaces_lem=[
	("david","carlos"),
	("david","cholo"),
	("david","itzel"),
	("carlos","cholo"),
	("carlos","itzel"),
	("cholo","itzel")
]
G1= nx.Graph(lista_enlaces_lem)
print("Dibujando red...")
nx.draw(G1,with_labels=True,node_color="red")
print("guardando imagen de la red 1 en formato png")
plt.savefig("red_lem.png")