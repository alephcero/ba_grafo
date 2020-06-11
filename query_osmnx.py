import pandas as pd
import osmnx as ox
import networkx as nx

# leer partidos nominatim
partidos = pd.read_csv('partidos.csv', sep=';')

# consultar y bajar en shape nodos y arcos
for i, partido in partidos.iterrows():
    try:
        print('Bajando', partido.nombre_breve)
        G = ox.graph_from_place(
            partido.nominatim, network_type='drive_service')
        nx.set_node_attributes(G, partido.nombre_breve, 'partido')
        nx.set_edge_attributes(G, partido.nombre_breve, 'partido')
        ox.save_graph_shapefile(G, filepath='carto/' + partido.nombre_breve,
                                encoding='utf-8')
    except:
        print('ERROR', partido.nombre_breve)
