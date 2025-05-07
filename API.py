import requests
from tkinter import *
import GUI
from shapely.geometry import Polygon
from pyproj import Transformer
from AreaBTS import a

Pais = "es"

class API:

    OVERPASS_URL = 'https://overpass-api.de/api/interpreter'

    def __init__(self):

        self.coordinates = {}
        self.ciudad = ""
        self.polygons1 = {}
        self.polygons2 = {}
        self.indice = 0

    def get_city_boundary(self, city_name):
        overpass_query = f'''
        [out:json][timeout:600];
        area[name="{city_name}"]; 
        ( 
        relation[type="boundary"]["boundary"="administrative"](area); 
        ); 
        out center; 
        '''
        response = requests.get(self.OVERPASS_URL, params={'data': overpass_query})

        data = response.json()

        # Obtener el admin_level
        if response.status_code == 200:
            try:

                admin_level = data['elements'][0]['tags']['admin_level']
                city_name_sin_espacios = city_name.replace(" - ", "-")


                overpass_query = f'''
                [out:json][timeout:600];
                area[name="{city_name}"]["wikipedia"="{Pais}:{city_name_sin_espacios}"]; 
                ( 
                relation[type="boundary"]["boundary"="administrative"]["admin_level"="{admin_level}"](area); 
                ); 
                out geom; 
                '''
                response = requests.get(self.OVERPASS_URL, params={'data': overpass_query})
                if response.status_code == 200:
                    data = response.json()
                    #print(data)

                    data_filtered  = [element for element in data['elements'] if element.get('tags', {}).get('name') == city_name]
                    #print(data_filtered)
                    
                    self.coordinates[city_name] = []

                    # Iterar sobre los elementos
                    for element in data_filtered:
                        # Iterar sobre los miembros de cada elemento
                        for member in element.get('members', []):
                            # Verificar si el miembro es un 'way' con rol 'outer'
                            if member['type'] == 'way':
                                # Obtener las coordenadas
                                for geometry in member.get("geometry", []):
                                    self.coordinates[city_name].append((geometry["lat"], geometry["lon"]))
                                    break

            
            except ValueError as e:
                print(f'Error: {e}')
            

    def buscar_ciudad(self):

        self.indice = GUI.notebook3.index(GUI.notebook3.select())

        if(self.indice==0):
            ciudad = GUI.Entry_city.get()
        else:
            ciudad = GUI.Entry_city2.get()

        self.get_city_boundary(ciudad)  # Llamar a la función de api.py

        if self.coordinates:
            # Mostrar el polígono en el mapa
            if(self.indice==0):
                x = GUI.map_widget.set_polygon(self.coordinates[ciudad], fill_color=None, outline_color="Black", border_width=4)
                if ciudad not in self.polygons1:
                    self.polygons1[ciudad] = []
                self.polygons1[ciudad].append(x)
                valores_actuales = list(GUI.desplegable_poligono1['values'])
                valores_actuales.append(ciudad)
                GUI.desplegable_poligono1['values'] = valores_actuales   
            else:
                y = GUI.map_widget2.set_polygon(self.coordinates[ciudad], fill_color=None, outline_color="Black", border_width=4)
                if ciudad not in self.polygons2:
                    self.polygons2[ciudad] = []
                self.polygons2[ciudad].append(y)
                valores_actuales = list(GUI.desplegable_poligono2['values'])
                valores_actuales.append(ciudad)
                GUI.desplegable_poligono2['values'] = valores_actuales   
                
            if(self.indice==1):
                #Transformador de coordenadas geográficas a UTM
                transformer = Transformer.from_crs("EPSG:4326", "EPSG:32630", always_xy=True)  

                # Convertimos las coordenadas a metros usando UTM
                utm_coords = [transformer.transform(lon, lat) for lat, lon in self.coordinates[ciudad]]

                # Creamos el polígono con coordenadas en metros
                poligono = Polygon(utm_coords)

                # Calculamos el área en metros cuadrados
                area_m2 = poligono.area

                area_km2 = (area_m2)/1000000
                
                a.Area[ciudad] = []

                a.Area[ciudad] = area_km2
            
                GUI.label_area_set.config(text=round(area_km2,2))

                a.AreaTotal = 0

                for i in a.Area.values():
                    a.AreaTotal += i

                GUI.label_total_area_set.config(text=round(a.AreaTotal,2))

                for i in GUI.history_table_ubicacion.get_children():
                    GUI.history_table_ubicacion.delete(i)

                for ciudad, km in a.Area.items():
                    GUI.history_table_ubicacion.insert("", "end", values=(ciudad, km))            


            print(f"Límite de la ciudad '{ciudad}' mostrado en el mapa.")
        else:
            print(f"No se encontraron coordenadas para la ciudad '{ciudad}'.")

    def borrar_boundary(self):

        self.indice = GUI.notebook3.index(GUI.notebook3.select())

        if(self.indice == 0):
            opc = GUI.desplegable_poligono1.get()
            borrador = self.polygons1[opc]
            if borrador:
                borrador[0].delete()
                self.polygons1.pop(opc)
                valores_actuales = list(GUI.desplegable_poligono1['values'])
                valores_actuales.remove(opc)
                GUI.desplegable_poligono1['values'] = valores_actuales
                GUI.desplegable_poligono1.set('')  # Limpiar el ComboBox

            else:
                print("The object doesn't exist.")
        else:
            opc = GUI.desplegable_poligono2.get()
            
            borrador = self.polygons2[opc]
            if borrador:
                borrador[0].delete()
                self.polygons2.pop(opc) 
                valores_actuales = list(GUI.desplegable_poligono2['values'])
                valores_actuales.remove(opc)
                GUI.desplegable_poligono2['values'] = valores_actuales
                GUI.desplegable_poligono2.set('')  # Limpiar el ComboBox

                a.Area.pop(opc)
                #print(a.Area)
                a.AreaTotal = 0
                for i in a.Area.values():
                    a.AreaTotal += i

                GUI.label_total_area_set.config(text=round(a.AreaTotal,2))

                for i in GUI.history_table_ubicacion.get_children():
                    GUI.history_table_ubicacion.delete(i)

                for ciudad, km in a.Area.items():
                    GUI.history_table_ubicacion.insert("", "end", values=(ciudad, km))                   

            else:
                print("The object doesn't exist.")



        
api = API()
