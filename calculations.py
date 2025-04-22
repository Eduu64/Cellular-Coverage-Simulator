from models import SIM
from tkinter import *
import GUI
from geopy.geocoders import Nominatim
from AreaBTS import a

def calcular():
    try:
        # Obtener valores de las entradas
        value1 = float(GUI.Entry_id1.get())
        value2 = float(GUI.Entry_id2.get())
        value3 = float(GUI.Entry_id3.get())
        value4 = float(GUI.Entry_id13.get())
        value5 = float(GUI.Entry_id15.get())
        value6 = float(GUI.Entry_id17.get())
        value7 = float(GUI.Entry_id16.get())
        value8 = float(GUI.Entry_id21.get())
        value9 = float(GUI.Entry_id23.get())
        value10 = float(GUI.Entry_id24.get())
        value12 = float(GUI.Entry_id29.get())
        sector = GUI.desplegable.get()
        value13 = float(GUI.Entry_id30.get())
        value14 = float(GUI.Entry_id31.get())
        value15 = float(GUI.radio_var.get())
        modelo = GUI.desplegable2.get()

        geolocator = Nominatim(timeout=10,user_agent="Celullar coverage simulator")

        
        location = geolocator.reverse(f"{value1}, {value2}")  # Pasa las coordenadas como una tupla
        value16 = location.raw.get('address', {})

        if 'hamlet' in value16:
            print("hamlet")
            value16 = 'hamlet'
        elif 'village' in value16:
            print("village")
            value16 = 'village'
        elif 'town' in value16:
            print("town")
            value16 = 'town'
        elif 'city' in value16:
            print("city")
            value16 = 'city'
        else:
            print("campo")
            value16 = 'campo'

        # Crear instancia de la clase SIM
        sim = SIM(value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value12, value13, value14, value15, value16, modelo)
        Pd = sim.Calculard(sector)
        print(Pd)

        if not Pd:
            print("No se encontraron distancias válidas.")
            return

        coordenadas = [(lat, lon) for angulo, d, lat, lon in Pd]

        if not coordenadas:
            print("No se generaron coordenadas válidas.")
            return

        # Lógica para mostrar resultados en el mapa
        if sector != "Cálculo eNodes":
            try:
            
                icon = PhotoImage(file="Proyecto2\Img\Antena.png")  # Cambiar path relativa en cada caso
                GUI.map_widget.set_marker(value1, value2, text="BTS", icon=icon)
        
            except Exception :

                GUI.map_widget.set_marker(value1, value2, text="BTS") # Si no encuentra path de la imagen pone default
            
            polygon_color = "black" if sector == "Sector 1" else "blue" if sector == "Sector 2" else "red"
            GUI.map_widget.set_polygon(coordenadas, fill_color=polygon_color, outline_color=polygon_color, border_width=5)

            max_value = max(Pd, key=lambda x: x[1])
            d_bts = max_value[1]*1.82

            x = 90 if sector == "Sector 1" else 210 if sector == "Sector 2" else 330
            dr_bts_latitude, dr_bts_longitude = sim.calcular_coordenadas(d_bts, x)
            try:
                icon = PhotoImage(file="Proyecto2\Img\cross.png")  # Cambiar path relativa en cada caso
                GUI.map_widget.set_marker(dr_bts_latitude, dr_bts_longitude, text = "", icon=icon)

            except Exception :
                GUI.map_widget.set_marker(dr_bts_latitude, dr_bts_longitude, text = "")        
        else:
            for item in Pd:
                if item[0] == 330:
                    d_max = item[1]
                    break
            area_km2 = (1.95) * (d_max ** 2)
            print(f"Área de cobertura: {area_km2} km²")
            a.setAreaeNode(area_km2)


    except ValueError as e:
        print(f'Error al calcular Area: {e}')


def calcular_auto(coords):
    """
    Agrega un marcador en el mapa y establece las coordenadas en los campos de entrada.

    :param coords: Coordenadas (latitud, longitud) donde se agregará el marcador.
    """
    print("Add marker:", coords)

    GUI.Entry_id1.delete(0, END)  # Limpiar el campo de latitud
    GUI.Entry_id2.delete(0, END)  # Limpiar el campo de longitud

    GUI.Entry_id1.insert(0, coords[0])  # Insertar latitud
    GUI.Entry_id2.insert(0, coords[1])  # Insertar longitud

    sectores = ["Sector 1", "Sector 2", "Sector 3"]

    for s in sectores:
        try:
            GUI.desplegable.set(s)  # Establecer el sector en el desplegable
            calcular()  # Llamar a la función calcular
        except Exception as e:
            print(f"Error al calcular para el sector {s}: {e}")