from tkinter import *
import tkintermapview
import math

class BTS():
    LON = 0
    LAT = 0

    PTX = 0

    GTXdBi = 0

    GTXS1 = []
    GTXS2 = []
    GTXS3 = []

    LTX = 0
    GRX = 0
    LRX = 0

    Hm = 0
    Hb = 0

    frec = 0

    steps = 100

    Smax = -100

    Pd = []

    sectores = {
            "sector1": [
                (0, 0), (30, 0), (60, 3), (90, 10),(120, 25), (150, 27), (180, 27), (210, 25), (240, 20), (270, 10),(300, 3), (330, 0)
            ],
            "sector2": [
                (0, 27), (30, 27), (60, 25), (90, 20), (120, 10), (150, 3), (180, 0), (210, 0), (240, 0), (270, 3), (300, 10), (330, 25)
            ],
            "sector3": [
                (0, 0), (30, 3), (60, 10), (90, 25), (120, 27), (150, 27), (180, 25), (210, 20), (240, 10), (270, 3), (300, 0), (330, 0)
            ]
        }
    

    Pdisponiblesectores = {
        "PdS1": [],
        "PdS2": [],
        "PdS3": []
    }
    
    

    def CalcularPds(self):
        d = 1
        a = (1.1*math.log10(self.frec)-0.7)*self.Hm-(1.56*math.log10(self.frec)-0.8)
        while( aux <= self.Smax):
            Lbs = 69.55 + 26.16 * math.log10(self.frec) - 13.82 * math.log10(self.Hb) - a + (44.9 - 6.55 * math.log10(self.Hb)) * math.log10(d/1000)
            d = d + self.steps

            for angulo,resultado in self.GTXS1:
                aux = self.PTX + resultado - self.LTX - Lbs + self.GRX - self.LRX
                auxLat = (self.LAT+(math.cos(angulo)*d)/111320)
                auxLon =  (self.LON+(math.sin(angulo)*d)/111320)
                self.Pd = [(angulo,auxLat,auxLon,aux)]



    def set_LON(self, value):
        self.LON = value

    def set_LAT(self, value):
        self.LAT = value

    def set_PTX(self, value):
        self.PTX = value

    def set_GTXdBi(self, value):
        self.GTXdBi = value
        self.GTXS1 = [(angulo, self.GTXdBi - perdida) for angulo, perdida in self.sectores["sector1"]]
        self.GTXS2 = [(angulo, self.GTXdBi - perdida) for angulo, perdida in self.sectores["sector2"]]
        self.GTXS3 = [(angulo, self.GTXdBi - perdida) for angulo, perdida in self.sectores["sector3"]]

    def set_LTX(self, value):
        self.LTX = value
    
    def set_GRX(self, value):
        self.GRX = value
    
    def set_LRX(self, value):
        self.LRX = value




def add_marker_event(coords):
    print("Add marker:", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="")



root = Tk()
root.geometry("1000x800")

my_label = LabelFrame(root)
my_label.pack(side=RIGHT)

map_widget = tkintermapview.TkinterMapView(my_label, width=600,height=1000)
map_widget.set_position(40.41, -3.7)
map_widget.set_zoom(10)

map_widget.add_right_click_menu_command(label="Añadir BTS",
                                        command=add_marker_event,
                                        pass_coords=True)

map_widget.pack()

root.mainloop()
