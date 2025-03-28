# gui.py
from tkinter import *
from tkinter import ttk
import tkintermapview
import customtkinter
import requests
from shapely.geometry import Polygon
from pyproj import Proj, Transformer

class Area:
    Area = 0

    def getArea(self):
        return self.Area
    
    def setArea(self,Area):
        self.Area +=  Area


a = Area()

def create_gui(calcular_callback):
    # Botón para buscar la ciudad
    
    def buscar_ciudad():
        overpass_url = 'https://overpass-api.de/api/interpreter'
        ciudad = Entry_city.get()


        overpass_query = f'''
        [out:json][timeout:600];
        area[name="{ciudad}"]; 
        ( 
        relation[type="boundary"]["boundary"="administrative"](area); 
        ); 
        out center; 
        '''
        response = requests.get(overpass_url, params={'data': overpass_query})

        data = response.json()

        # Obtener el admin_level
        if response.status_code == 200:

            admin_level = data['elements'][0]['tags']['admin_level']
            print(admin_level)

            overpass_query = f'''
            [out:json][timeout:600];
            area[name="{ciudad}"]; 
            ( 
            relation[type="boundary"]["boundary"="administrative"]["admin_level"="{admin_level}"](area); 
            ); 
            out geom; 
            '''
            response = requests.get(overpass_url, params={'data': overpass_query})
            if response.status_code == 200:
                data = response.json()
                data_filtered  = [element for element in data['elements'] if element.get('tags', {}).get('name') == ciudad]
                print(data_filtered )
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
                
                map_widget.set_polygon(coordinates,fill_color=None, outline_color="Black", border_width=4)

                # Transformador de coordenadas geográficas a UTM
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
                LabelAreaset.config(text=round(area_km2,2))
                LabelTotalAreaset.config(text=round(a.getArea(),2))


            else:
                print(f"Error: {response.status_code}")
        else:
                print(f"Error: {response.status_code}")





    window = Tk()

    window.title("Cellular Coverage Simulator")

    window.geometry("1000x900")

    # Bloquear el redimensionamiento de la ventana
    window.resizable(False, False)  # (ancho, alto)

    window.configure(bg="#FFFFFF")

    # Entradas para la interfaz gráfica
    Label_id4 = Label(window, text="Coordenadas BTS", font=("Arial", 14), bg="#FFFFFF")
    Label_id4.place(x=30, y=10)

    Label_id5 = Label(window, text="Latitud", font=("Arial", 14), bg="#FFFFFF")
    Label_id5.place(x=10, y=50)
    Entry_id1 = customtkinter.CTkEntry(master=window, placeholder_text="Latitud")
    Entry_id1.place(x=150, y=50)  

    Label_id6 = Label(window, text="Longitud", font=("Arial", 14), bg="#FFFFFF")
    Label_id6.place(x=10, y=90)
    Entry_id2 = customtkinter.CTkEntry(master=window, placeholder_text="Longitud")
    Entry_id2.place(x=150, y=90)  

    Label_id4 = Label(window, text="Parametros", font=("Arial", 14), bg="#FFFFFF")
    Label_id4.place(x=30, y=130)

    Label_id8 = Label(window, text="Ptx", font=("Arial", 14), bg="#FFFFFF")
    Label_id8.place(x=10, y=170)
    Entry_id3 = customtkinter.CTkEntry(master=window, placeholder_text="Ptx")
    Entry_id3.place(x=150, y=170)  

    Label_id12 = Label(window, text="Gtx", font=("Arial", 14), bg="#FFFFFF")
    Label_id12.place(x=10, y=210)
    Entry_id13 = customtkinter.CTkEntry(master=window, placeholder_text="Gtx")
    Entry_id13.place(x=150, y=210)  

    Label_id14 = Label(window, text="Ltx", font=("Arial", 14), bg="#FFFFFF")
    Label_id14.place(x=10, y=250)
    Entry_id15 = customtkinter.CTkEntry(master=window, placeholder_text="Ltx")
    Entry_id15.place(x=150, y=250)  

    Label_id18 = Label(window, text="Grx", font=("Arial", 14), bg="#FFFFFF")
    Label_id18.place(x=10, y=290)
    Entry_id16 = customtkinter.CTkEntry(master=window, placeholder_text="Grx")
    Entry_id16.place(x=150, y=290)  

    Label_id19 = Label(window, text="Lrx", font=("Arial", 14), bg="#FFFFFF")
    Label_id19.place(x=10, y=330)
    Entry_id17 = customtkinter.CTkEntry(master=window, placeholder_text="Lrx")
    Entry_id17.place(x=150, y=330)  

    Label_id20 = Label(window, text="Frecuencia", font=("Arial", 14), bg="#FFFFFF")
    Label_id20.place(x=10, y=370)
    Entry_id21 = customtkinter.CTkEntry(master=window, placeholder_text="Frecuencia")
    Entry_id21.place(x=150, y=370)  

    Label_id25 = Label(window, text="Hb", font=("Arial", 14), bg="#FFFFFF")
    Label_id25.place(x=10, y=410)
    Entry_id23 = customtkinter.CTkEntry(master=window, placeholder_text="Hb")
    Entry_id23.place(x=150, y=410)  

    Label_id26 = Label(window, text="Hm", font=("Arial", 14), bg="#FFFFFF")
    Label_id26.place(x=10, y=450)
    Entry_id24 = customtkinter.CTkEntry(master=window, placeholder_text="Hm")
    Entry_id24.place(x=150, y=450)  

    Label_id30 = Label(window, text="Cobertura", font=("Arial", 14), bg="#FFFFFF")
    Label_id30.place(x=10, y=490)
    Entry_id29 = customtkinter.CTkEntry(master=window, placeholder_text="Cobertura")
    Entry_id29.place(x=150, y=490)  

    Label_id31 = Label(window, text="Per. Añadidas", font=("Arial", 14), bg="#FFFFFF")
    Label_id31.place(x=10, y=530)
    Entry_id30 = customtkinter.CTkEntry(master=window, placeholder_text="Per. Añadidas")
    Entry_id30.place(x=150, y=530)  

    Label_id32 = Label(window, text="Margen", font=("Arial", 14), bg="#FFFFFF")
    Label_id32.place(x=10, y=570)
    Entry_id31 = customtkinter.CTkEntry(master=window, placeholder_text="Margen")
    Entry_id31.place(x=150, y=570)  

    radio_var = IntVar()
    RadioButton_id9 = customtkinter.CTkRadioButton(
        master=window,
        variable=radio_var,
        value=1,
        text="DOWNLINK",
        text_color="#000000",
        border_color="#000000",
        fg_color="#808080",
        hover_color="#2F2F2F",
    )
    RadioButton_id9.place(x=10, y=620)

    RadioButton_id10 = customtkinter.CTkRadioButton(
        master=window,
        variable=radio_var,
        value=2,
        text="UPLINK",
        text_color="#000000",
        border_color="#000000",
        fg_color="#808080",
        hover_color="#2F2F2F",
    )
    RadioButton_id10.place(x=10, y=660)  

    desplegable = ttk.Combobox(window, width=50, values=["Sector 1", "Sector 2", "Sector 3"])
    desplegable.place(x=10, y=700)

    desplegable2 = ttk.Combobox(window, width=50, values=["Okumura Hata"])
    desplegable2.place(x=10, y=740)

    Button_id22 = customtkinter.CTkButton(
        master=window,
        fg_color="#ec3642", #color of the button
        hover_color="RED", #color of the button when mouse is over
        font=("Montserrat", 16), #font used
        corner_radius=12, width=100, #radius of edges and total width
        text="Calcular",
        command=calcular_callback
    )
    Button_id22.place(x=170, y=640)

    # Configuración del mapa
    my_label = LabelFrame(window)
    my_label.pack(side=RIGHT)

    map_widget = tkintermapview.TkinterMapView(my_label, width=650, height=1000, corner_radius=0)
    map_widget.set_position(40.41, -3.7)
    map_widget.set_zoom(12)
    map_widget.pack()

    Button_buscar = customtkinter.CTkButton(
    master=window,
    fg_color="BLACK",  # Color del botón
    hover_color="BLACK",  # Color del botón al pasar el mouse
    font=("Montserrat", 16),  # Fuente utilizada
    text="Buscar",
    command=buscar_ciudad)

    Button_buscar.place(x=840, y=10)  # Ajustar la posición según sea necesario

    # Campo de entrada para la ciudad
    Entry_city = customtkinter.CTkEntry(master=window, placeholder_text="Nombre de la ciudad",width=350)
    Entry_city.place(x=480, y=10)  # Ajustar la posición según sea necesario

    LabelArea = Label(window, text="Area Territorio:", font=("Arial", 14), bg="#FFFFFF")
    LabelAreaset = Label(window, text="0", font=("Arial", 14), bg="#FFFFFF")
    LabelArea.place(x=10, y=780)
    LabelAreaset.place(x=150, y=780)

    LabelTotalArea = Label(window, text="Area Total Territorio:", font=("Arial", 14), bg="#FFFFFF")
    LabelTotalAreaset = Label(window, text="0", font=("Arial", 14), bg="#FFFFFF")
    LabelTotalArea.place(x=10, y=820)
    LabelTotalAreaset.place(x=200, y=820)

    Labelenodes = Label(window, text="eNodes necesarios:", font=("Arial", 14), bg="#FFFFFF")
    Labelenodesset = Label(window, text="0", font=("Arial", 14), bg="#FFFFFF")
    Labelenodes.place(x=10, y=860)
    Labelenodesset.place(x=200, y=860)


    return window, map_widget, Entry_id1, Entry_id2, Entry_id3, Entry_id13, Entry_id15, Entry_id16, Entry_id17, Entry_id21, Entry_id23, Entry_id24, Entry_id29, desplegable, Entry_id30, Entry_id31, radio_var, desplegable2