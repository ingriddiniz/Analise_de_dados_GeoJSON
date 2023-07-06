# -*- coding: utf-8 -*-
"""AnalisedeDadosGeoJSON

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XhpTTypjxtacH1RxtCP0xovDVe5rxbPe
"""

import pandas as pd
import geojson
from PIL import ImageColor

# Lendo os arquivos em DataFrames separados
routes_df = pd.read_csv('/metro/routes.txt')
shapes_df = pd.read_csv('metro/shapes.txt')
stops_df = pd.read_csv('metro/stops.txt')

# Renomear a coluna "shape_id" para "route_id" em shapes
shapes_df.rename(columns={'shape_id': 'route_id'}, inplace=True)

# Realizar a junção dos DataFrames utilizando a coluna "route_id" como chave
merged_data = pd.merge(shapes_df, routes_df, on='route_id')
merged_data = pd.merge(merged_data, stops_df, left_on=['shape_pt_lat', 'shape_pt_lon'], right_on=['stop_lat', 'stop_lon'])

merged_data

def desenhaMetro():
    features = []
    for _, group in merged_data.groupby('route_short_name'): #merged_data agrupadas por linha de metrô
        group = group.sort_values('shape_pt_sequence')# Ordenar as estações pelo sequenciamento

        coordinates = []

        for _, row in group.iterrows():
            lon = row['stop_lon']
            lat = row['stop_lat']

            point = geojson.Point((lon, lat)) # Criar um objeto Point para a estação

            # Metainformação: nome da estação
            properties = {
                'stop_name': row['stop_name']
            }

            # Criar uma feature com o objeto Point e as propriedades
            feature = geojson.Feature(geometry=point, properties=properties)
            features.append(feature)
            coordinates.append((lon, lat))

        color ='#'+group['route_color'].values[0]

        linestring = geojson.LineString(coordinates) # Criar um objeto LineString para cada linha

        # Metainformação: nome da linha e cor
        properties = {
            'route_short_name': group['route_short_name'].values[0],
            "stroke": color
        }

        # Criar uma feature com o objeto LineString e as propriedades
        feature = geojson.Feature(geometry=linestring, properties=properties, stroke=color)
        features.append(feature)

    # Criar o objeto FeatureCollection com a lista de features
    feature_collection = geojson.FeatureCollection(features)

    # Escrever o objeto FeatureCollection no arquivo "metro.geojson"
    with open('metro.geojson', 'w') as f:
        geojson.dump(feature_collection, f)

desenhaMetro()