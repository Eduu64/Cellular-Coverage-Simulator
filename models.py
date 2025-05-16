import math
from tkinter import *
import GUI

class SIM:
    
    def __init__(self, Id, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value12, value13, value14, value15, value16, value17):
        """
        Inicializa la clase SIM con los parámetros necesarios para el cálculo.

        :param lat: Latitud de la ubicación.
        :param lon: Longitud de la ubicación.
        :param ptx: Potencia de transmisión.
        :param gtx: Ganancia de transmisión.
        :param ltx: Pérdidas de transmisión.
        :param grx: Ganancia de recepción.
        :param lrx: Pérdidas de recepción.
        :param freq: Frecuencia de operación.
        :param hb: Altura de la antena base.
        :param hm: Altura del receptor.
        :param smax: Máxima señal permitida.
        :param perdidas_anadidas: Pérdidas adicionales.
        :param margen: Margen de seguridad.
        :param tipo_ubicacion: Tipo de ubicación (ciudad, pueblo, etc.).
        :param modelo: Modelo de propagación (Okumura Hata, COST231, etc.).
        """
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

        # Cálculo de las ganancias por sector
        self.GTXS1 = [(angulo, self.GTXdBi - perdida) for angulo, perdida in self.LS1]
        self.GTXS2 = [(angulo, self.GTXdBi - perdida) for angulo, perdida in self.LS2]
        self.GTXS3 = [(angulo, self.GTXdBi - perdida) for angulo, perdida in self.LS3]

        self.sectores = {
        "Sector 1": self.GTXS1,
        "Sector 2": self.GTXS2,
        "Sector 3": self.GTXS3,
        }

        self.Pd = {sector: [] for sector in self.sectores}

        self.Id = Id

        self.x = None 
        self.y = None  
        self.z = None  
        self.boundary_estacion = {}
    # Definición de las pérdidas por sector
    LS1 = [(0, 13), (30, 3), (60, 0), (90, 0), (120, 0), (150, 3), (180, 13), (210, 20), (240, 30), (270, 40), (300, 30), (330, 20)]
    LS2 = [(0, 30), (30, 40), (60, 30), (90, 20), (120, 13), (150, 3), (180, 0), (210, 0), (240, 0), (270, 3), (300, 13), (330, 20)]
    LS3 = [(0, 0), (30, 3), (60, 13), (90, 20), (120, 30), (150, 40), (180, 30), (210, 20), (240, 13), (270, 3), (300, 0), (330, 0)]


    def calcular_a_hm(self):
        """
        Calcula la altura efectiva del receptor (Hm) según el tipo de ubicación y frecuencia.
        
        :return: Altura efectiva del receptor.
        """
        if self.type_location == "city":
            if self.frec <= 200:
                return 8.29 * (math.log10(1.54 * self.Hm))**2 - 1.1
            else:
                return 3.2 * (math.log10(11.75 * self.Hm))**2 - 4.97
        else:
            return (1.1 * math.log10(self.frec) - 0.7) * self.Hm - (1.56 * math.log10(self.frec) - 0.8)

    def calcular_coordenadas(self, d, angulo):
        """
        Calcula las nuevas coordenadas basadas en la distancia y el ángulo.

        :param d: Distancia desde la ubicación original.
        :param angulo: Ángulo de dirección.
        :return: Nuevas coordenadas (latitud, longitud).
        """
        R = 6371  # Radio de la Tierra en kilómetros
        phi1 = math.radians(self.LAT)  # Convertir latitud a radianes
        lambda1 = math.radians(self.LON)  # Convertir longitud a radianes
        ang = math.radians((angulo))  # Convertir ángulo a radianes

        Dang = d / R  # Distancia angular

        # Cálculo de φ2 y λ2 usando las fórmulas proporcionadas
        phi2 = math.asin(math.sin(phi1) * math.cos(Dang) + math.cos(phi1) * math.sin(Dang) * math.cos(ang))
        lambda2 = lambda1 + math.atan2(math.sin(ang) * math.sin(Dang) * math.cos(phi1), math.cos(Dang) - math.sin(phi1) * math.sin(phi2))

        # Convertir de radianes a grados
        newLat = math.degrees(phi2)
        newLon = math.degrees(lambda2)

        return newLat, newLon

    def Calculard(self):
        """
        Calcula las distancias y coordenadas para el sector seleccionado.

        :param value: Sector seleccionado.
        :return: Lista de distancias y coordenadas.
        """

        a = self.calcular_a_hm()

        for sector, lista_ganancia in self.sectores.items():
            for angulo, gananciatx in lista_ganancia:
                if self.modelo == "Okumura Hata":
                    d = self._calcular_distancia_okumura_hata(gananciatx, a)
                elif self.modelo == "COST231":
                    d = self._calcular_distancia_cost231(gananciatx, a)
                else:
                    print("Error en el modelo escogido")
                    break

                newLat, newLon = self.calcular_coordenadas(d, angulo)
                self.Pd[sector].append((angulo, d, newLat, newLon))

    def calcular_boundary(self):

        if not self.Pd:
            print("No se encontraron distancias válidas.")
            return
                
        # Lógica para mostrar resultados en el mapa
        try:
        
            icon = PhotoImage(file="Proyecto2\Img\Antena.png")  # Cambiar path relativa en cada caso
            self.estacion = GUI.map_widget.set_marker(self.LAT, self.LON, text=f"BTS {self.Id}", icon=icon)
    
        except Exception :

            self.estacion = GUI.map_widget.set_marker(self.LAT, self.LON, text=f"BTS {self.Id}") # Si no encuentra path de la imagen pone default
            
        
        for sector, lista_ganancia in self.sectores.items():
            coordenadas = [(lat, lon) for angulo, d, lat, lon in self.Pd[sector]]
            self.boundary_estacion[sector] = GUI.map_widget.set_polygon(coordenadas, fill_color="black", outline_color="black", border_width=4)
        
        max_value_tupla = max(self.Pd["Sector 1"], key=lambda x: x[1]) #distancia mas larga
        #Extraer y ordenar las distancias únicas
        distancias_unicas = sorted({x[1] for x in self.Pd["Sector 1"]}, reverse=True)        
        #Obtener la segunda más alta (si existe)
        if len(distancias_unicas) >= 2:
            Segmax_value = distancias_unicas[1]
            max_value = max_value_tupla[1]

            #Buscar la tupla que tenga esa distancia
            #segundo_valor = next(x for x in Pd if x[1] == max_value)
        else:
            Segmax_value = None  # Si no hay suficientes valores distintos    

        d_bts = max_value + Segmax_value 

        dr_bts_latitude1, dr_bts_longitude1 = self.calcular_coordenadas(d_bts, 90)
        dr_bts_latitude2, dr_bts_longitude2 = self.calcular_coordenadas(d_bts, 210)
        dr_bts_latitude3, dr_bts_longitude3 = self.calcular_coordenadas(d_bts, 330)


        try:
            icon = PhotoImage(file="Proyecto2\Img\cross.png")  # Cambiar path relativa en cada caso

            self.x = GUI.map_widget.set_marker(dr_bts_latitude1, dr_bts_longitude1, text = "", icon=icon)
            self.y = GUI.map_widget.set_marker(dr_bts_latitude2, dr_bts_longitude2, text = "", icon=icon)
            self.z = GUI.map_widget.set_marker(dr_bts_latitude3, dr_bts_longitude3, text = "", icon=icon)
        
        except Exception :
            self.x = GUI.map_widget.set_marker(dr_bts_latitude1, dr_bts_longitude1, text = "")
            self.y = GUI.map_widget.set_marker(dr_bts_latitude2, dr_bts_longitude2, text = "")
            self.z = GUI.map_widget.set_marker(dr_bts_latitude3, dr_bts_longitude3, text = "")


    
    def _calcular_distancia_okumura_hata(self, gananciatx, a):
        """
        Calcula la distancia usando el modelo Okumura Hata.

        :param gananciatx: Ganancia de transmisión.
        :param a: Altura efectiva del receptor.
        :return: Distancia calculada.
        """
        if self.type_location == "village":
            return 10**((self.PTX - self.Smax + gananciatx + self.GRX - self.LTX - self.LRX - self.PerdidasAñadidas - self.Margen - 69.55 - 26.16 * math.log10(self.frec) + 13.82 * math.log10(self.Hb) + a + 2 * (math.log10(self.frec / 28)**2) + 5.4) / (44.9 - 6.55 * math.log10(self.Hb)))
        elif self.type_location == "hamlet":
            return 10**((self.PTX - self.Smax + gananciatx + self.GRX - self.LTX - self.LRX - self.PerdidasAñadidas - self.Margen - 69.55 - 26.16 * math.log10(self.frec) + 13.82 * math.log10(self.Hb) + a + 4.78 * (math.log10(self.frec))**2 - 18.33 * math.log10(self.frec) + 40.94) / (44.9 - 6.55 * math.log10(self.Hb)))
        else:
            return 10**((self.PTX - self.Smax + gananciatx + self.GRX - self.LTX - self.LRX - self.PerdidasAñadidas - self.Margen - 69.55 - 26.16 * math.log10(self.frec) + 13.82 * math.log10(self.Hb) + a) / (44.9 - 6.55 * math.log10(self.Hb)))

    def _calcular_distancia_cost231(self, gananciatx, a):
        """
        Calcula la distancia usando el modelo COST231.

        :param gananciatx: Ganancia de transmisión.
        :param a: Altura efectiva del receptor.
        :return: Distancia calculada.
        """
        if self.type_location == "city":
            return 10**((self.PTX - self.Smax + gananciatx + self.GRX - self.LTX - self.LRX - self.PerdidasAñadidas - self.Margen - 46.3 - 33.6 * math.log10(self.frec) + 13.82 * math.log10(self.Hb) + a - 3) / (44.9 - 6.55 * math.log10(self.Hb)))
        else:
            return 10**((self.PTX - self.Smax + gananciatx + self.GRX - self.LTX - self.LRX - self.PerdidasAñadidas - self.Margen - 46.3 - 33.6 * math.log10(self.frec) + 13.82 * math.log10(self.Hb) + a) / (44.9 - 6.55 * math.log10(self.Hb)))
        

