from tkinter import *
from tkinter import ttk
import tkinter as ttk
import math
from GUI import create_gui, a  # Importa la función para crear la GUI
from geopy.geocoders import Nominatim



class SIM():

    LS1 = [(0, 13), (30, 3), (60, 0), (90, 0), (120, 0), (150, 3), (180, 13), (210, 20), (240, 30), (270, 40), (300, 30), (330, 20)]
    LS2 = [(0, 30), (30, 40), (60, 30), (90, 20), (120, 13), (150, 3), (180, 0), (210, 0), (240, 0), (270, 3), (300, 13), (330, 20)]
    LS3 = [(0, 0), (30, 3), (60, 13), (90, 20), (120, 30), (150, 40), (180, 30), (210, 20), (240, 13), (270, 3), (300, 0), (330, 0)]
    
    def __init__(self, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value12, value13, value14, value15, value16, value17):
       
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


        self.LAT = value1
        self.LON = value2
        
        self.PTX = value3

        self.frec = value8
        self.Hb = value9
        self.Hm = value10
        self.Smax = value12
        self.PerdidasAñadidas = value13
        self.Margen = value14

        self.type_location = value16
        self.modelo = value17

        self.GTXS1 = [(angulo, self.GTXdBi - perdida) for angulo, perdida in self.LS1]
        self.GTXS2 = [(angulo, self.GTXdBi - perdida) for angulo, perdida in self.LS2]
        self.GTXS3 = [(angulo, self.GTXdBi - perdida) for angulo, perdida in self.LS3]


    def calcular_a_hm(self):
        
        if self.type_location == "city":
            if self.frec <= 200:
                return 8.29 * (math.log10(1.54 * self.Hm))**2 - 1.1
            else:
                return 3.2 * (math.log10(11.75 * self.Hm))**2 - 4.97
        else:
            return (1.1 * math.log10(self.frec) - 0.7) * self.Hm - (1.56 * math.log10(self.frec) - 0.8)
        

    def calcular_coordenadas(self, d, angulo):

        R = 6378  # Radio de la Tierra en metros
        phi1 = math.radians(self.LAT)  # Convertir latitud a radianes
        lambda1 = math.radians(self.LON)   # Convertir longitud a radianes
        ang = math.radians((angulo) % 360 )       # Convertir ángulo a radianes 

        Dang = d / R  # Distancia angular

        # Cálculo de φ2 y λ2 usando las fórmulas proporcionadas
        phi2 = math.asin(math.sin(phi1) * math.cos(Dang) + math.cos(phi1) * math.sin(Dang) * math.cos(ang))
        lambda2 = lambda1 + math.atan2(math.sin(ang) * math.sin(Dang) * math.cos(phi1), math.cos(Dang) - math.sin(phi1) * math.sin(phi2))
       
        # Convertir de radianes a grados
        newLat = math.degrees(phi2)
        newLongrad = math.degrees(lambda2)

        newLon = (newLongrad + 540) % 360 - 180 

       
        return newLat, newLon




    def Calculard(self, value):
        Pd = []

        if value == "Sector 1":
            G = self.GTXS1 
        elif value == "Sector 2":
            G = self.GTXS2
        else:
            G = self.GTXS3

        #print(G)
        a =  self.calcular_a_hm()
        #print(a)

        for angulo, gananciatx in G:
                
                if self.modelo == "Okumura Hata":
                
                    if self.type_location == "village":
                        d = 10**((self.PTX - self.Smax  + gananciatx + self.GRX - self.LTX -self.LRX - self.PerdidasAñadidas -self.Margen -69.55-26.16*math.log10(self.frec)+13.82*math.log10(self.Hb)+a + 2*(math.log10(self.frec/28)**2) + 5.4)/(44.9-6.55*math.log10(self.Hb)))
                    elif self.type_location == "hamlet":
                        d = 10**((self.PTX - self.Smax  + gananciatx + self.GRX - self.LTX -self.LRX - self.PerdidasAñadidas -self.Margen -69.55-26.16*math.log10(self.frec)+13.82*math.log10(self.Hb)+a + 4.78*(math.log10(self.frec))**2 - 18.33*math.log10(self.frec) + 40.94)/(44.9-6.55*math.log10(self.Hb)))
                    else:
                        d = 10**((self.PTX - self.Smax  + gananciatx + self.GRX - self.LTX -self.LRX - self.PerdidasAñadidas -self.Margen -69.55-26.16*math.log10(self.frec)+13.82*math.log10(self.Hb)+a)/(44.9-6.55*math.log10(self.Hb)))
                    
                    newLat, newLon = self.calcular_coordenadas(d, angulo)
                    Pd.append((angulo, d, newLat, newLon))

                else:

                    print("Error en el modelo escogido")

        return Pd
    

def calcular():

    try:

        value1 = float(Entry_id1.get())
        value2 = float(Entry_id2.get())
        value3 = float(Entry_id3.get())
        value4 = float(Entry_id13.get())
        value5 = float(Entry_id15.get())
        value6 = float(Entry_id17.get())
        value7 = float(Entry_id16.get())
        value8 = float(Entry_id21.get())
        value9 = float(Entry_id23.get())
        value10 = float(Entry_id24.get())
        value12 = float(Entry_id29.get())
        sector = desplegable.get()
        value13 = float(Entry_id30.get())
        value14 = float(Entry_id31.get())
        value15 = float(radio_var.get())
        modelo = desplegable2.get()

        #print(f"value1: {value1}, value2: {value2}, value3: {value3}, value4: {value4}, value5: {value5}, " f"value6: {value6}, value7: {value7}, value8: {value8}, value9: {value9}, value10: {value10}, " f"value12: {value12}, sector: {sector}, value13: {value13}, value14: {value14}, value15: {value15}, modelo: {modelo}")

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

        #print(location.raw)  # Imprime la información de la ubicación
        #print(value16)


        sim = SIM(value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value12, value13, value14, value15, value16, modelo)
        Pd = sim.Calculard(sector)
        
        # Verifica que Pd no esté vacío
        if not Pd:
            print("No se encontraron distancias válidas.")
            return

        print(Pd)
        coordenadas = [(lat, lon) for angulo, d, lat, lon in Pd]

        # Verifica que coords no esté vacío
        if not coordenadas:
            print("No se generaron coordenadas válidas.")
            return

        if sector != "Cálculo eNodes":
            
            try:
            
                icon = PhotoImage(file="Proyecto\Antena.png")  # Cambiar path relativa en cada caso
                marker_2 = map_widget.set_marker(value1, value2, text="BTS", icon=icon)
        
            except Exception :

                marker_2 = map_widget.set_marker(value1, value2, text="BTS") # Si no encuentra path de la imagen pone default

            polygon_color = "black" if sector == "Sector 1" else "blue" if sector == "Sector 2" else "red"
            map_widget.set_polygon(coordenadas, fill_color = polygon_color, outline_color=polygon_color, border_width=5)



            max_value = (max(Pd, key=lambda x: x[1]))
            d_bts = (max_value[1])*1.82

            print(f'Maxima distancia: {d_bts}')

            if sector == "Sector 1":
                x = 90
            elif sector == "Sector 2":
                x = 210
            elif sector == "Sector 3":
                x = 330
            else:  
                None
            

            dr_bts_latitude, dr_bts_longitude  = sim.calcular_coordenadas(d_bts,x)

            try:
                icon = PhotoImage(file="Proyecto\cross.png")  # Cambiar path relativa en cada caso
                map_widget.set_marker(dr_bts_latitude, dr_bts_longitude, text = "", icon=icon)

            except Exception :
                map_widget.set_marker(dr_bts_latitude, dr_bts_longitude, text = "")

           
         
        else:
                
                for item in Pd:
                    if item[0] == 330:
                        d_max = item[1]  # Accedemos a distancia maxima
                        break

                # Calculamos el área en metros cuadrados
                area_km2 = ((9*math.sqrt(3))/(8))*(d_max**2) # Area celda trisectorial

                print(f"Área de cobertura: {area_km2} km²")
                a.setAreaeNode(area_km2)


    except ValueError:
        print(f'Error:{ValueError}')




# Crear la GUI y ejecutar la aplicación
window, map_widget, Entry_id1, Entry_id2, Entry_id3, Entry_id13, Entry_id15, Entry_id16, Entry_id17, Entry_id21, Entry_id23, Entry_id24, Entry_id29, desplegable, Entry_id30, Entry_id31, radio_var, desplegable2 = create_gui(calcular)

def calcular_auto(coords):
    print("Add marker:", coords)
    Entry_id1.delete(0, ttk.END)
    Entry_id2.delete(0, ttk.END)
    Entry_id1.insert(0,coords[0])
    Entry_id2.insert(0,coords[1])

    sectores = {"Sector 1", "Sector 2", "Sector 3"}

    for s in sectores:
        try:
            desplegable.set(s)
            calcular()
        except Exception:
            print(Exception)
    

map_widget.add_right_click_menu_command(label="Add BTS",
                                        command=calcular_auto,
                                        pass_coords=True)

window.mainloop()
