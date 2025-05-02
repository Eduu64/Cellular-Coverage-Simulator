import requests
from tkinter import *
from shapely.geometry import Polygon
from pyproj import Transformer
import math
import GUI
from AreaBTS import a

OVERPASS_URL = 'https://overpass-api.de/api/interpreter'



def get_city_boundary(city_name):

    """
    Realiza una consulta a la API de Overpass y devuelve los datos en formato JSON.

    Obtiene el límite administrativo de una ciudad dada.
    
    :param city_name: Nombre de la ciudad.
    :return: Coordenadas del límite de la ciudad o None si hay un error.
    """

    overpass_query = f'''
    [out:json][timeout:600];
    area[name="{city_name}"]; 
    ( 
    relation[type="boundary"]["boundary"="administrative"](area); 
    ); 
    out center; 
    '''
    response = requests.get(OVERPASS_URL, params={'data': overpass_query})

    data = response.json()

    # Obtener el admin_level
    if response.status_code == 200:

        admin_level = data['elements'][0]['tags']['admin_level']
        #print(admin_level)

        overpass_query = f'''
        [out:json][timeout:600];
        area[name="{city_name}"]; 
        ( 
        relation[type="boundary"]["boundary"="administrative"]["admin_level"="{admin_level}"](area); 
        ); 
        out geom; 
        '''
        response = requests.get(OVERPASS_URL, params={'data': overpass_query})
        if response.status_code == 200:
            data = response.json()
            data_filtered  = [element for element in data['elements'] if element.get('tags', {}).get('name') == city_name]
            #print(data_filtered)
            coordinates = []

            # Iterar sobre los elementos
            for element in data_filtered:
                # Iterar sobre los miembros de cada elemento
                for member in element.get('members', []):
                    # Verificar si el miembro es un 'way' con rol 'outer'
                    if member['type'] == 'way':
                        # Obtener las coordenadas
                        for geometry in member.get("geometry", []):
                            coordinates.append((geometry["lat"], geometry["lon"]))
                            break

        return coordinates
    
    return None

def buscar_ciudad():
    """
    Busca el límite de la ciudad ingresada y lo muestra en el mapa.

    :param ciudad: Nombre de la ciudad a buscar.
    :param map_widget: Widget del mapa donde se mostrará el límite de la ciudad.
    """
    ciudad = GUI.Entry_city.get()
    coordinates = get_city_boundary(ciudad)  # Llamar a la función de api.py

    if coordinates:
        # Mostrar el polígono en el mapa
        GUI.map_widget.set_polygon(coordinates, fill_color=None, outline_color="Black", border_width=4)
        print(f"Límite de la ciudad '{ciudad}' mostrado en el mapa.")
    else:
        print(f"No se encontraron coordenadas para la ciudad '{ciudad}'.")

    #Transformador de coordenadas geográficas a UTM
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:32630", always_xy=True)  

    # Convertimos las coordenadas a metros usando UTM
    utm_coords = [transformer.transform(lon, lat) for lat, lon in coordinates]

    # Creamos el polígono con coordenadas en metros
    poligono = Polygon(utm_coords)

    # Calculamos el área en metros cuadrados
    area_m2 = poligono.area

    area_km2 = (area_m2)/1000000

    a.setArea(area_km2)

    print(f"Área del polígono: {area_km2:.2f} km²")
    print(f"Área del polígono: {a.getArea():.2f} km²")
    GUI.label_area_set.config(text=round(area_km2,2))
    GUI.label_total_area_set.config(text=round(a.getArea(),2))
    eNodes = a.getArea()/ a.getAreaCobertura()
    GUI.label_enodes_set.config(text=math.ceil(eNodes))


