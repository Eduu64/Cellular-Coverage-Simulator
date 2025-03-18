from tkinter import *
import tkintermapview

class BTS():
    LON = 0
    LAT = 0

    PTX = 0

    GTXdBi = 0
    GTXdB = 0

    GTXS1 = []
    GTXS2 = []
    GTXS3 = []

    LTX = 0
    GRX = 0
    LRX = 0

    sectores = {
            "sector1": [
                (0, 0), (10, 0), (20, 0), (30, 0), (40, 0), (50, 0), (60, 0), (70, 0), (80, 0), (90, 0),
                (100, 0), (110, 0), (120, 0), (130, 0), (140, 0), (150, 0), (160, 0), (170, 0), (180, 0), (190, 0),
                (200, 0), (210, 0), (220, 0), (230, 0), (240, 0), (250, 0), (260, 0), (270, 0), (280, 0), (290, 0),
                (300, 0), (310, 0), (320, 0), (330, 0), (340, 0), (350, 0), (360, 0)
            ],
            "sector2": [
                (0, 0), (10, 0), (20, 0), (30, 0), (40, 0), (50, 0), (60, 0), (70, 0), (80, 0), (90, 0),
                (100, 0), (110, 0), (120, 0), (130, 0), (140, 0), (150, 0), (160, 0), (170, 0), (180, 0), (190, 0),
                (200, 0), (210, 0), (220, 0), (230, 0), (240, 0), (250, 0), (260, 0), (270, 0), (280, 0), (290, 0),
                (300, 0), (310, 0), (320, 0), (330, 0), (340, 0), (350, 0), (360, 0)
            ],
            "sector3": [
                (0, 0), (10, 0), (20, 0), (30, 0), (40, 0), (50, 0), (60, 0), (70, 0), (80, 0), (90, 0),
                (100, 0), (110, 0), (120, 0), (130, 0), (140, 0), (150, 0), (160, 0), (170, 0), (180, 0), (190, 0),
                (200, 0), (210, 0), (220, 0), (230, 0), (240, 0), (250, 0), (260, 0), (270, 0), (280, 0), (290, 0),
                (300, 0), (310, 0), (320, 0), (330, 0), (340, 0), (350, 0), (360, 0)
            ]
        }
    

    Pdisponiblesectores = {
        "PdS1": [],
        "PdS2": [],
        "PdS3": []
    }
    
    
    def __init__(self):
        self.GTXdB = self.GTXdBi - 2,15
        self.GTXS1 = [(angulo, self.GTXdB - perdida) for angulo, perdida in self.sectores["sector1"]]
        self.GTXS2 = [(angulo, self.GTXdB - perdida) for angulo, perdida in self.sectores["sector2"]]
        self.GTXS3 = [(angulo, self.GTXdB - perdida) for angulo, perdida in self.sectores["sector3"]]

    def set_LON(self, value):
        self.LON = value

    def set_LAT(self, value):
        self.LAT = value

    def set_PTX(self, value):
        self.PTX = value

    def set_GTXdBi(self, value):
        self.GTXdBi = value

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