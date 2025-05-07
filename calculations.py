from models import SIM
from tkinter import *
import GUI 
from geopy.geocoders import Nominatim
from AreaBTS import a
import math

SIMULACIONES = []

Id = 0

def calcular():
    global Id, SIMULACIONES
    try:
        # Obtener valores de las entradas
        value1 = float(GUI.entry_latitud.get())
        value2 = float(GUI.entry_longitud.get())
        value3 = float(GUI.entry_potenciatx.get())
        value4 = float(GUI.entry_gananciatx.get())
        value5 = float(GUI.entry_ltx.get())
        value6 = float(GUI.entry_lrx.get())
        value7 = float(GUI.entry_gananciarx.get())
        value8 = float(GUI.entry_frecuencia.get())
        value9 = float(GUI.entry_alturabase.get())
        value10 = float(GUI.entry_alturamovil.get())
        value12 = float(GUI.entry_cobertura.get())
        value13 = float(GUI.entry_perdidasanadidas.get())
        value14 = float(GUI.entry_margen.get())
        value15 = float(GUI.radio_var.get())
        modelo = GUI.desplegable2.get()

        geolocator = Nominatim(timeout=10,user_agent="Celullar Station simulator")

        
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
        sim = SIM(Id, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value12, value13, value14, value15, value16, modelo)
        sim.Calculard()
        print(sim.Pd)
        sim.calcular_boundary()
        SIMULACIONES.append(sim) 
        valores_actuales = list(GUI.desplegable3['values'])
        valores_actuales.append(f"BTS {Id}")
        GUI.desplegable3['values'] = valores_actuales        
        Id += 1
        
    except ValueError as e:
        print(f'Error al calcular Area: {e}')


def calcular_auto(coords):
    """
    Agrega un marcador en el mapa y establece las coordenadas en los campos de entrada.

    :param coords: Coordenadas (latitud, longitud) donde se agregará el marcador.
    """
    print("Add marker:", coords)

    GUI.entry_latitud.delete(0, END)  # Limpiar el campo de latitud
    GUI.entry_longitud.delete(0, END)  # Limpiar el campo de longitud

    GUI.entry_latitud.insert(0, coords[0])  # Insertar latitud
    GUI.entry_longitud.insert(0, coords[1])  # Insertar longitud

    calcular()  # Llamar a la función calcular

def borrar_BTS():
        try:
            sectores = ['Sector 1', 'Sector 2', 'Sector 3']
            Id_bts = GUI.desplegable3.get()
            _ , Id = Id_bts.split()
            bts = SIMULACIONES[int(Id)]
                       
            if bts.x is not None:
                bts.x.delete()
            else:
                print("El objeto bts no tiene el marcador 'x' o es None.")
            if bts.y is not None:
                bts.y.delete()
            else:
                print("El objeto bts no tiene el marcador 'y' o es None.")
            if bts.z is not None:
                bts.z.delete()
            else:
                print("El objeto bts no tiene el marcador 'z' o es None.")
                
            for sector in sectores:
                if sector in bts.boundary_estacion:
                    if bts.boundary_estacion[sector] is not None:
                        bts.boundary_estacion[sector].delete()
                    else:
                        print(f"El sector '{sector}' no tiene un límite definido o es None.")
                else:
                    print(f"El sector '{sector}' no está en boundary_estacion.")
                    
            if hasattr(bts, 'estacion'):
                bts.estacion.delete()
            else:
                print("El objeto bts no tiene el atributo 'estacion'.")

            if f"BTS {Id}" in GUI.desplegable3['values']:
                valores_actuales = list(GUI.desplegable3['values'])
                valores_actuales.remove(f"BTS {Id}")
                GUI.desplegable3['values'] = valores_actuales
                GUI.desplegable3.set('')  # Limpiar el ComboBox

        except Exception as e:
            print(f"Error en borrar_BTS: {e}")

def calculareNodes():
    try:
        # Obtener valores de las entradas
        value3 = float(GUI.entry_potenciatx2.get())
        value4 = float(GUI.entry_gananciatx2.get())
        value5 = float(GUI.entry_ltx2.get())
        value6 = float(GUI.entry_lrx2.get())
        value7 = float(GUI.entry_gananciarx2.get())
        value8 = float(GUI.entry_frecuencia2.get())
        value9 = float(GUI.entry_alturabase2.get())
        value10 = float(GUI.entry_alturamovil2.get())
        value12 = float(GUI.entry_cobertura2.get())
        value13 = float(GUI.entry_perdidasanadidas2.get())
        value14 = float(GUI.entry_margen2.get())
        value15 = float(GUI.radio_var2.get())
        modelo = GUI.desplegable22.get()

        GUI.entry_potenciatx.delete(0, END)
        GUI.entry_potenciatx.insert(0, value3) 

        GUI.entry_gananciatx.delete(0, END)
        GUI.entry_gananciatx.insert(0, value4)

        GUI.entry_ltx.delete(0, END)
        GUI.entry_ltx.insert(0, value5)

        GUI.entry_lrx.delete(0, END)
        GUI.entry_lrx.insert(0, value6)

        GUI.entry_gananciarx.delete(0, END)
        GUI.entry_gananciarx.insert(0, value7)

        GUI.entry_frecuencia.delete(0, END)
        GUI.entry_frecuencia.insert(0, value8)

        GUI.entry_alturabase.delete(0, END)
        GUI.entry_alturabase.insert(0, value9)

        GUI.entry_alturamovil.delete(0, END)
        GUI.entry_alturamovil.insert(0, value10)

        GUI.entry_cobertura.delete(0, END)
        GUI.entry_cobertura.insert(0, value12)

        GUI.entry_perdidasanadidas.delete(0, END)
        GUI.entry_perdidasanadidas.insert(0, value13)

        GUI.entry_margen.delete(0, END)
        GUI.entry_margen.insert(0, value14)

        GUI.radio_var.set(value15)

        GUI.desplegable2.set(modelo)

        geolocator = Nominatim(timeout=10,user_agent="Celullar Station simulator")
        
        location_types = []

        for ciudad in a.Area:
            location = geolocator.geocode(ciudad)
            if location:
                #print(location.raw)
                address = location.raw.get('address', {})
                if 'hamlet' in address:
                    location_types.append('hamlet')
                elif 'village' in address:
                    location_types.append('village')
                elif 'town' in address:
                    location_types.append('town')
                elif 'city' or 'suburb' in address:
                    location_types.append('city')
                else:
                    location_types.append('campo')
             
        for prioridad in ['city', 'town', 'village', 'hamlet', 'campo']:
            if prioridad in location_types:
                value16 = prioridad
                print(value16)
                break

        value1 = location.latitude
        value2 = location.longitude

        # Crear instancia de la clase SIM
        sim = SIM(Id, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value12, value13, value14, value15, value16, modelo)
        sim.Calculard()
        print(sim.Pd)
        max_value_tupla = max(sim.Pd["Sector 1"], key=lambda x: x[1]) #distancia mas larga
        d_max = max_value_tupla[1]

        area_efectiva_km2 = (1.95) * (d_max ** 2)
        a.AreaEfectivaCobertura = area_efectiva_km2

        eNodes = a.AreaTotal/ area_efectiva_km2
        a.eNodes = eNodes

        GUI.label_enodes_set.config(text=math.ceil(a.eNodes))
        GUI.label_area_efectiva_set.config(text=str(round(area_efectiva_km2,2)))
        
    except ValueError as e:
        print(f'Error al calcular Area: {e}')