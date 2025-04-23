from tkinter import *
from tkinter import ttk
import tkintermapview
import customtkinter
from calculations import calcular,calcular_auto
from API import buscar_ciudad



window = Tk()

window.title("Cellular Coverage Simulator")

window.geometry("1000x900")

# Bloquear el redimensionamiento de la ventana
window.resizable(False, False)  # (ancho, alto)

window.configure(bg="#FFFFFF")

style = ttk.Style()
style.theme_use('default')

# Cambiar el fondo del Notebook
style.configure('TNotebook', background='white', borderwidth=0)
style.configure('TNotebook.Tab', background='white',focuscolor='none',  borderwidth=0, padding=[10, 5])

# También cambiar el fondo de los frames dentro de cada pestaña
style.configure('TFrame', background='white')

style.configure('TCombobox',
                fieldbackground='white',   # fondo del campo
                background='white',        # fondo del menú desplegable
                foreground='black',
                arrowcolor='gray',
                bordercolor='lightgray',
                lightcolor='white',
                darkcolor='white'
                )


# Crear un Notebook para las pestañas
notebook = ttk.Notebook(window)
notebook.pack(fill=BOTH, expand=True)

# Crear la primera pestaña
tab1 = Frame(notebook)
notebook.add(tab1, text='Simulador de Cobertura')

# Crear la segunda pestaña
tab2 = Frame(notebook)
notebook.add(tab2, text='Simulador de Capacidad')

notebook = ttk.Notebook(window, style='custom.TNotebook')

# Crear un frame para contener el canvas y el mapa
main_frame = Frame(tab1)
main_frame.pack(side=LEFT,fill=BOTH, expand=True)

main_frame2 = Frame(tab1)
main_frame2.pack(side=RIGHT,fill=BOTH, expand=True)

# Crear un canvas dentro del frame principal
canvas = Canvas(main_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Crear una scrollbar y vincularla al canvas
scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configurar el canvas para que use la scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind(
    '<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)


# Crear un frame dentro del canvas
frame = Frame(canvas)
frame.config(width=500, height=900)
frame.configure(bg="#FFFFFF")
canvas.create_window((0, 0), window=frame, anchor='nw')

# Entradas para la interfaz gráfica
Label_id4 = Label(frame, text="Coordenadas BTS", font=("Arial", 14), bg="#FFFFFF")
Label_id4.place(x=100, y=10)

Label_id5 = Label(frame, text="Latitud", font=("Arial", 14), bg="#FFFFFF")
Label_id5.place(x=10, y=50)
Entry_id1 = customtkinter.CTkEntry(master=frame, placeholder_text="Latitud")
Entry_id1.place(x=150, y=50)  

Label_id6 = Label(frame, text="Longitud", font=("Arial", 14), bg="#FFFFFF")
Label_id6.place(x=10, y=90)
Entry_id2 = customtkinter.CTkEntry(master=frame, placeholder_text="Longitud")
Entry_id2.place(x=150, y=90)  

Label_id4 = Label(frame, text="Parametros", font=("Arial", 14), bg="#FFFFFF")
Label_id4.place(x=100, y=130)

Label_id8 = Label(frame, text="Ptx", font=("Arial", 14), bg="#FFFFFF")
Label_id8.place(x=10, y=170)
Entry_id3 = customtkinter.CTkEntry(master=frame, placeholder_text="Ptx")
Entry_id3.place(x=150, y=170)  

Label_id12 = Label(frame, text="Gtx", font=("Arial", 14), bg="#FFFFFF")
Label_id12.place(x=10, y=210)
Entry_id13 = customtkinter.CTkEntry(master=frame, placeholder_text="Gtx")
Entry_id13.place(x=150, y=210)  

Label_id14 = Label(frame, text="Ltx", font=("Arial", 14), bg="#FFFFFF")
Label_id14.place(x=10, y=250)
Entry_id15 = customtkinter.CTkEntry(master=frame, placeholder_text="Ltx")
Entry_id15.place(x=150, y=250)  

Label_id18 = Label(frame, text="Grx", font=("Arial", 14), bg="#FFFFFF")
Label_id18.place(x=10, y=290)
Entry_id16 = customtkinter.CTkEntry(master=frame, placeholder_text="Grx")
Entry_id16.place(x=150, y=290)  

Label_id19 = Label(frame, text="Lrx", font=("Arial", 14), bg="#FFFFFF")
Label_id19.place(x=10, y=330)
Entry_id17 = customtkinter.CTkEntry(master=frame, placeholder_text="Lrx")
Entry_id17.place(x=150, y=330)  

Label_id20 = Label(frame, text="Frecuencia", font=("Arial", 14), bg="#FFFFFF")
Label_id20.place(x=10, y=370)
Entry_id21 = customtkinter.CTkEntry(master=frame, placeholder_text="Frecuencia")
Entry_id21.place(x=150, y=370)  

Label_id25 = Label(frame, text="Hb", font=("Arial", 14), bg="#FFFFFF")
Label_id25.place(x=10, y=410)
Entry_id23 = customtkinter.CTkEntry(master=frame, placeholder_text="Hb")
Entry_id23.place(x=150, y=410)  

Label_id26 = Label(frame, text="Hm", font=("Arial", 14), bg="#FFFFFF")
Label_id26.place(x=10, y=450)
Entry_id24 = customtkinter.CTkEntry(master=frame, placeholder_text="Hm")
Entry_id24.place(x=150, y=450)  

Label_id30 = Label(frame, text="Cobertura", font=("Arial", 14), bg="#FFFFFF")
Label_id30.place(x=10, y=490)
Entry_id29 = customtkinter.CTkEntry(master=frame, placeholder_text="Cobertura")
Entry_id29.place(x=150, y=490)  

Label_id31 = Label(frame, text="Per. Añadidas", font=("Arial", 14), bg="#FFFFFF")
Label_id31.place(x=10, y=530)
Entry_id30 = customtkinter.CTkEntry(master=frame, placeholder_text="Per. Añadidas")
Entry_id30.place(x=150, y=530)  

Label_id32 = Label(frame, text="Margen", font=("Arial", 14), bg="#FFFFFF")
Label_id32.place(x=10, y=570)
Entry_id31 = customtkinter.CTkEntry(master=frame, placeholder_text="Margen")
Entry_id31.place(x=150, y=570)  

radio_var = IntVar()
RadioButton_id9 = customtkinter.CTkRadioButton(
    master=frame,
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
    master=frame,
    variable=radio_var,
    value=2,
    text="UPLINK",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
)
RadioButton_id10.place(x=10, y=660)  

desplegable = ttk.Combobox(frame, width=50, values=["Cálculo eNodes","Sector 1", "Sector 2", "Sector 3"])
desplegable.place(x=10, y=700)

desplegable2 = ttk.Combobox(frame, width=50, values=["Okumura Hata","COST231"])
desplegable2.place(x=10, y=740)

Button_id22 = customtkinter.CTkButton(
    master=frame,
    fg_color="#ec3642", #color of the button
    hover_color="RED", #color of the button when mouse is over
    font=("Montserrat", 16), #font used
    corner_radius=12, width=100, #radius of edges and total width
    text="Calcular",
    command=calcular
)
Button_id22.place(x=170, y=640)

# Configuración del mapa
my_label = LabelFrame(main_frame2)
my_label.pack(side=RIGHT)

map_widget = tkintermapview.TkinterMapView(my_label, width=650, height=1000, corner_radius=0)
map_widget.set_position(40.41, -3.7)
map_widget.set_zoom(12)
map_widget.pack()

Button_buscar = customtkinter.CTkButton(
master=main_frame2,
fg_color="BLACK",  # Color del botón
hover_color="BLACK",  # Color del botón al pasar el mouse
font=("Montserrat", 16),  # Fuente utilizada
text="Buscar",
command=buscar_ciudad)

Button_buscar.place(x=435, y=10)  # Ajustar la posición según sea necesario

# Campo de entrada para la ciudad
Entry_city = customtkinter.CTkEntry(master=main_frame2, placeholder_text="Nombre de la ciudad",width=350)
Entry_city.place(x=75, y=10)  # Ajustar la posición según sea necesario

LabelArea = Label(frame, text="Area Territorio:", font=("Arial", 14), bg="#FFFFFF")
LabelAreaset = Label(frame, text="0", font=("Arial", 14), bg="#FFFFFF")
LabelArea.place(x=10, y=780)
LabelAreaset.place(x=150, y=780)

LabelTotalArea = Label(frame, text="Area Total Territorio:", font=("Arial", 14), bg="#FFFFFF")
LabelTotalAreaset = Label(frame, text="0", font=("Arial", 14), bg="#FFFFFF")
LabelTotalArea.place(x=10, y=820)
LabelTotalAreaset.place(x=200, y=820)

Labelenodes = Label(frame, text="Estimación eNodes necesarios:", font=("Arial", 14), bg="#FFFFFF")
Labelenodesset = Label(frame, text="0", font=("Arial", 14), bg="#FFFFFF")
Labelenodes.place(x=10, y=860)
Labelenodesset.place(x=300, y=860)

map_widget.add_right_click_menu_command(label="Add BTS",
                                        command=calcular_auto,
                                        pass_coords=True)