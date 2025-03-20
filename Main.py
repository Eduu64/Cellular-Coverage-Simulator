from tkinter import *
import math
import numpy as np
from GUI import create_gui  # Importa la función para crear la GUI

class SIM():
    def __init__(self, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15):
       
        #UPLINK//DOWNLINK
        if value15 == 1:
            self.GTXdBi = value4
            self.LTX = value5
            self.LRX = value6
            self.GRX = value7
        else:
            self.GTXdBi = value7 #7
            self.LTX = value6 #6
            self.LRX = value5 #5
            self.GRX = value4 #4



        self.LON = value1
        self.LAT = value2
        
        self.PTX = value3

        self.frec = value8
        self.Hb = value9
        self.Hm = value10
        self.steps = value11
        self.Smax = value12
        self.PerdidasAñadidas = value13
        self.Margen = value14

        self.GTXS1 = [(angulo, self.GTXdBi - perdida) for angulo, perdida in self.LS1]
        self.GTXS2 = [(angulo, self.GTXdBi - perdida) for angulo, perdida in self.LS2]
        self.GTXS3 = [(angulo, self.GTXdBi - perdida) for angulo, perdida in self.LS3]

    LS1 = [(0, 13), (30, 3), (60, 0), (90, 0), (120, 0), (150, 3), (180, 13), (210, 20), (240, 30), (270, 40), (300, 30), (330, 20)]
    LS2 = [(0, 30), (30, 40), (60, 30), (90, 20), (120, 13), (150, 3), (180, 0), (210, 0), (240, 0), (270, 3), (300, 13), (330, 20)]
    LS3 = [(0, 0), (30, 3), (60, 13), (90, 20), (120, 30), (150, 40), (180, 30), (210, 20), (240, 13), (270, 3), (300, 0), (330, 0)]

    def calcular_Lbs(self, d):
        return (69.55 + 26.16 * math.log10(self.frec) - 13.82 * math.log10(self.Hb) + (44.9 - 6.55 * math.log10(self.Hb)) * math.log10(d))

    def calcular_coordenadas(self, d, angulo):
        R = 6371  # Radio de la Tierra en metros
        phi1 = math.radians(self.LAT)  # Convertir latitud a radianes
        lambda1 = math.radians(self.LON)   # Convertir longitud a radianes
        ang = math.radians(angulo)       # Convertir ángulo a radianes

        Dang = d / R  # Distancia angular

        # Cálculo de φ2 y λ2 usando las fórmulas proporcionadas
        phi2 = math.asin(math.sin(phi1) * math.cos(Dang) + math.cos(phi1) * math.sin(Dang) * math.cos(ang))
        lambda2 = lambda1 + math.atan2(math.sin(ang) * math.sin(Dang) * math.cos(phi1), math.cos(Dang) - math.sin(phi1) * math.sin(phi2))

        # Convertir de radianes a grados
        newLat = math.degrees(phi2)
        newLon = math.degrees(lambda2)
        return newLat, newLon

    def CalcularPds(self, value):
        Pd = []
        G = self.GTXS1 if value == "Sector 1" else self.GTXS2 if value == "Sector 2" else self.GTXS3 
        a =  3.2 * (math.log10(11.75 * self.Hm) ** 2) - 4.97

        for angulo, gananciatx in G:
            d = 1 / 1000  # Inicializa la distancia en km
            while True:
                Lbs = self.calcular_Lbs(d)
                aux = self.PTX + gananciatx - self.LTX - Lbs + self.GRX - self.LRX -self.PerdidasAñadidas - self.Margen
                if aux <= self.Smax:
                    newLat, newLon = self.calcular_coordenadas(d, angulo)
                    Pd.append((angulo, d, newLat, newLon, aux))
                    break  # Salir del bucle si se encuentra una distancia válida
                else:
                    d += (self.steps / 1000)  # Incrementar la distancia
                    continue

        return Pd
    

def calcular():
    try:
        value1 = float(Entry_id1.get())
        value2 = float(Entry_id2.get())
        value3 = int(Entry_id3.get())
        value4 = int(Entry_id13.get())
        value5 = int(Entry_id15.get())
        value6 = int(Entry_id17.get())
        value7 = int(Entry_id16.get())
        value8 = int(Entry_id21.get())
        value9 = int(Entry_id23.get())
        value10 = int(Entry_id24.get())
        value11 = int(Entry_id27.get())
        value12 = int(Entry_id29.get())
        sector = desplegable.get()
        value13 = int(Entry_id30.get())
        value14 = int(Entry_id31.get())
        value15 = int(radio_var.get())

        marker_2 = map_widget.set_marker(value1, value2, text="BTS")

        sim = SIM(value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15)
        Pd = sim.CalcularPds(sector)
        #print(Pd)

        # Verifica que Pd no esté vacío
        if not Pd:
            print("No se encontraron distancias válidas.")
            return

        coords = [(lon, lat) for angulo, d, lat, lon, Pd in Pd]

        # Verifica que coords no esté vacío
        if not coords:
            print("No se generaron coordenadas válidas.")
            return

        polygon_color = "black" if sector == "Sector 1" else "blue" if sector == "Sector 2" else "red"
        map_widget.set_polygon(coords, fill_color=None, outline_color=polygon_color, border_width=5)

    except ValueError:
        print("Error: Asegúrate de ingresar solo números en todos los campos.")


# Crear la GUI y ejecutar la aplicación
window, map_widget, Entry_id1, Entry_id2, Entry_id3, Entry_id13, Entry_id15, Entry_id16, Entry_id17, Entry_id21, Entry_id23, Entry_id24, Entry_id27, Entry_id29, desplegable, Entry_id30, Entry_id31, radio_var = create_gui(calcular)

window.mainloop()