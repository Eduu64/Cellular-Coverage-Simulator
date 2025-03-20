from tkinter import *
from tkinter import ttk
import tkintermapview
import math
import customtkinter

class SIM():
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

    LS1 = [(0, 10), (30, 3), (60, 0), (90, 0), (120, 0), (150, 3), (180, 10), (210, 25), (240, 27), (270, 27), (300, 25), (330, 20)]
    LS2 = [(0, 27), (30, 27), (60, 25), (90, 20), (120, 10), (150, 3), (180, 0), (210, 0), (240, 0), (270, 3), (300, 10), (330, 25) ]
    LS3= [(0, 0), (30, 3), (60, 10), (90, 25), (120, 27), (150, 27), (180, 25), (210, 20), (240, 10), (270, 3), (300, 0), (330, 0)]
        
    



    def CalcularPds(self):
        a = 3.2 * (math.log10(11.75 * self.Hm) ** 2) - 4.97      
        print(a)

        for angulo,resultado in self.GTXS1:
            d = 1
            top = False
            while top == False :
                Lbs = (69.55 + 26.16 * math.log10(self.frec) - 13.82 * math.log10(self.Hb) - a + (44.9 - 6.55 * math.log10(self.Hb)) * math.log10(d/1000))
                d += self.steps
                aux = self.PTX + resultado - self.LTX - Lbs + self.GRX - self.LRX
                if aux < self.Smax:
                    top = True
                    print(d)
                    print(Lbs)
                    print(resultado)
                    print(aux)

                    auxLat =  math.radians(self.LAT)
                    auxLon =  math.radians(self.LON)
                    auxAng = math.radians(angulo)
                    newLat = math.asin(math.sin(auxLat)*math.cos(d/6371000)+math.cos(auxLat)*math.sin(d/6371000)*math.cos(auxAng) )
                    newLon = auxLon + math.atan2(math.sin(auxAng)*math.sin(d/6371000)*math.cos(auxLat),math.cos(d/6371000)-math.sin(auxLat)*math.sin(auxLat))
                    
                    newLat = math.degrees(newLat)
                    newLon = math.degrees(newLon)

                    newLon = (newLon + 540) % 360 - 180

                    self.Pd.append((angulo,newLat,newLon,aux))

        return self.Pd

    def __init__(self, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12):
        self.LON = value1
        self.LAT = value2
        self.PTX = value3
        self.GTXdBi = value4
        self.LTX = value5

        self.LRX = value6
        self.GRX = value7

        self.frec = value8
        self.Hb = value9
 
        
        self.Hm = value10
        self.steps = value11
        self.Smax = value12


        self.GTXS1 = [(angulo, self.GTXdBi - perdida) for angulo, perdida in self.LS1]
        self.GTXS2 = [(angulo, self.GTXdBi - perdida) for angulo, perdida in self.LS2]
        self.GTXS3 = [(angulo, self.GTXdBi - perdida) for angulo, perdida in self.LS3]

    



def calcular():
    try:
        value1 = float(Entry_id1.get())
        value2 = float(Entry_id2.get())
        value3 = int(Entry_id3.get())
        value4 = int(Entry_id13.get())
        value5 = int(Entry_id15.get())
        value6 = int(Entry_id16.get())
        value7 = int(Entry_id17.get())
        value8 = int(Entry_id21.get())
        value9 = int(Entry_id23.get())
        value10 = int(Entry_id24.get())
        value11 = int(Entry_id27.get())
        value12 = int(Entry_id29.get())
        print(value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12)
        Simu = SIM(value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12)

        Pd1= Simu.CalcularPds()
        print(Pd1)

        coords = [(lon, lat ) for angulo, lat, lon, Pd in Pd1]

        print(coords)

        marker_3 = map_widget.set_marker(value1, value2, text="")

        polygon_1 = map_widget.set_polygon(coords)

    
    except ValueError:
        print("Error: Asegúrate de ingresar solo números en todos los campos.")


def add_marker_event(coords):
    print("Add marker:", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="")




window = Tk()
window.geometry("1000x800")
window.configure(bg="#FFFFFF")

radio_var = IntVar()

Label_id14 = customtkinter.CTkLabel(
    master=window,
    text="Ltx",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id14.place(x=10, y=280)
Entry_id21 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Placeholder",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id21.place(x=110, y=400)
RadioButton_id9 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var,
    value=9,
    text="DOWNLINK",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    )
RadioButton_id9.place(x=10, y=620)
Entry_id29 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Placeholder",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id29.place(x=110, y=560)
Label_id26 = customtkinter.CTkLabel(
    master=window,
    text="Hm",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id26.place(x=10, y=440)
Label_id30 = customtkinter.CTkLabel(
    master=window,
    text="Cobertura",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id30.place(x=10, y=560)
RadioButton_id10 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var,
    value=10,
    text="UPLINK",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    )
RadioButton_id10.place(x=10, y=660)
Entry_id13 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Placeholder",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id13.place(x=110, y=240)
Label_id7 = customtkinter.CTkLabel(
    master=window,
    text="Parámetros",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id7.place(x=40, y=150)
Entry_id15 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Placeholder",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id15.place(x=110, y=280)
Label_id20 = customtkinter.CTkLabel(
    master=window,
    text="Frecuencia",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id20.place(x=10, y=400)
Entry_id27 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Placeholder",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id27.place(x=110, y=520)
Label_id19 = customtkinter.CTkLabel(
    master=window,
    text="Lrx",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id19.place(x=10, y=360)
Label_id8 = customtkinter.CTkLabel(
    master=window,
    text="Ptx",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id8.place(x=10, y=200)
Label_id6 = customtkinter.CTkLabel(
    master=window,
    text="Longitud",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id6.place(x=10, y=90)
Button_id22 = customtkinter.CTkButton(
    master=window,
    text="Calcular",
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=50,
    width=120,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    command=calcular
    )
Button_id22.place(x=160, y=630)
Entry_id1 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Placeholder",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id1.place(x=110, y=50)
Entry_id16 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Placeholder",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id16.place(x=110, y=360)
Label_id28 = customtkinter.CTkLabel(
    master=window,
    text="Steps",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id28.place(x=10, y=520)
Entry_id3 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Placeholder",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id3.place(x=110, y=200)
Label_id25 = customtkinter.CTkLabel(
    master=window,
    text="Hb",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id25.place(x=10, y=480)
Label_id5 = customtkinter.CTkLabel(
    master=window,
    text="Latitud",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id5.place(x=10, y=50)
Entry_id23 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Placeholder",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id23.place(x=110, y=480)
Label_id18 = customtkinter.CTkLabel(
    master=window,
    text="Grx",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id18.place(x=10, y=320)
Entry_id17 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Placeholder",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id17.place(x=110, y=320)
Entry_id2 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Placeholder",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id2.place(x=110, y=90)
Label_id4 = customtkinter.CTkLabel(
    master=window,
    text="Coordenadas BTS",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=150,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id4.place(x=30, y=10)
Label_id12 = customtkinter.CTkLabel(
    master=window,
    text="Gtx",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id12.place(x=10, y=240)
Entry_id24 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Placeholder",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id24.place(x=110, y=440)

desplegable = ttk.Combobox(window,width = 50)
desplegable.place(x=10, y=710)

my_label = LabelFrame(window)
my_label.pack(side=RIGHT)

map_widget = tkintermapview.TkinterMapView(my_label, width=650,height=1000)
map_widget.set_position(40.41, -3.7)
map_widget.set_zoom(12)
map_widget.pack()



window.mainloop()