import networkx as nx 
import matplotlib.pyplot as plt 
#red donde la mitad de nodos tienen grado g
#y la otra mitad tiene grado g/2
#miembros del grupo:
#yedgar,ydani,xluis,xemilio,xdiego,ycarlos,caleb,xheli,xdiego,minion,cris
lista_enlaces_grupoC=[
	("Edgar","Luis"),
	("Edgar","Isur"),
	("Edgar","Heli"),
	("Edgar","Daniel"),
	("Luis","Minion"),
	("Heli","Diego"),
	("Isur","Carlos"),
	("Emilio","Carlos"),
	("Emilio","Diego"),
	("Daniel","Caleb"),
	("Daniel","Minion"),
	("Daniel","Carlos"),
	("Carlos","Caleb"),
	("Caleb","Minion"),
	("Caleb","Cris"),
	("Minion","Cris")]
G6=nx.Graph(lista_enlaces_grupoC)
print("Dibujando red...")
nx.draw(G6,with_labels=True,node_color="purple")
print("guardando imagen de la red 6 en formato png")
plt.savefig("red_complicada.png")
