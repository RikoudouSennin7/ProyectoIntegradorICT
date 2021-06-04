#Para crear y análizar redes
import networkx as nx
G = nx.erdos_renyi_graph(10,0.1)
cercania=nx.closeness_centrality(G)
cercania_mayor=max(cercania.values())
print(cercania_mayor)
for key in cercania:
    if cercania_mayor==cercania[key]:
        print("Nodo #"+str(key)+" Mayor cercania")
