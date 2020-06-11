import geopandas as gpd
import os

partidos = os.listdir('carto')
partidos

edges = gpd.GeoDataFrame()
nodes = gpd.GeoDataFrame()

for partido in partidos:
    ruta = 'carto/' + partido + '/'
    node = gpd.read_file(ruta + 'nodes.shp')
    edge = gpd.read_file(ruta + 'edges.shp')
    nodes = nodes.append(node)
    edges = edges.append(edge)


edges.to_file('carto/region_edges.geojson', driver='GeoJSON')
nodes.to_file('carto/region_nodes.geojson', driver='GeoJSON')
