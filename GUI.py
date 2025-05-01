from tkinter import *
from tkinter import ttk
import tkintermapview
import customtkinter
from calculations import calcular,calcular_auto
from API import buscar_ciudad
from Capacidad import ef, cap



customtkinter.deactivate_automatic_dpi_awareness()
customtkinter.set_appearance_mode("light")



window = Tk()

window.title("Cellular Coverage Simulator")

window.geometry("1000x900")

window.resizable(False, False)  # (ancho, alto)

window.configure(bg="#FFFFFF")

style = ttk.Style()
# Usar tema base 'default' para partir limpio
style.theme_use('default')

# ---------- Notebook ----------
style.configure("TNotebook",
                background="#FFFFFF",
                borderwidth=0,
                padding=6)

style.configure("TNotebook.Tab",
                background="#FFFFFF",
                padding=[10, 5],
                font=("Segoe UI", 10),
                focuscolor = "none",
                borderwidth=0)

style.map("TNotebook.Tab",
            background=[("selected", "#FFFFFF"),
                        ("active", "#D9EFFE")],
            foreground=[("selected", "#000000"),
                        ("!selected", "#666666")])


# ---------- Button ----------
style.configure("TButton",
                background="#FFFFFF",
                foreground="#1F2937",
                borderwidth=1,
                relief="flat",
                padding=10)

style.map("TButton",
            background=[("active", "#E5E7EB"),
                        ("pressed", "#D1D5DB"),
                        ("disabled", "#F9FAFB")],
            relief=[("pressed", "sunken"),
                    ("!pressed", "flat")],
            foreground=[("disabled", "#A0A3AC")])

style.map("TButton",
            highlightcolor=[("focus", "#3B82F6")],
            highlightthickness=[("focus", 2)],
            highlightbackground=[("focus", "#3B82F6")])

# ---------- Combobox ----------
style.layout("TCombobox",
    [('Combobox.downarrow', {'side': 'right', 'sticky': ''}),
     ('Combobox.padding', {'expand': '1', 'sticky': 'nswe',
       'children': [('Combobox.textarea', {'sticky': 'nswe'})]})])

style.configure("TCombobox",
    foreground="#1F2937",
    background="#F9FAFB",
    fieldbackground="#F9FAFB",
    borderwidth=1,
    relief="flat",
    padding=4,
    arrowsize=12)

# Aquí forzamos el fondo del Entry y desactivamos el azul de foco
style.map("TCombobox",
    fieldbackground=[("readonly", "#F9FAFB"), ("focus", "#F9FAFB")],
    background=[("active", "#F9FAFB"), ("focus", "#F9FAFB")],
    bordercolor=[("focus", "#D1D5DB")],
    arrowcolor=[("active", "#4B5563"), ("!active", "#4B5563")],
    foreground=[("focus", "#1F2937")])

style.configure("TScrollbar",
                     background="#F9FAFB",
                     troughcolor="#F9FAFB",
                     sliderlength=20,
                     sliderrelief="flat",
                     bordercolor="#F9FAFB")


# ---------- Entry ----------
style.configure("TEntry",
                foreground="#1F2937",
                fieldbackground="#FFFFFF",
                background="#FFFFFF",
                bordercolor="#D1D5DB",
                lightcolor="#D1D5DB",
                darkcolor="#D1D5DB",
                borderwidth=1,
                relief="flat",
                padding=0)

style.map("TEntry",
            fieldbackground=[("focus", "#FFFFFF"), ("!focus", "#FFFFFF")],
            bordercolor=[("focus", "#3B82F6"), ("!focus", "#D1D5DB")])
 # ---------- Treeview minimalista ----------
style.configure("Treeview",
                background="#FFFFFF",
                fieldbackground="#FFFFFF",
                foreground="#2E2E2E",
                bordercolor="#FFFFFF",
                borderwidth=0,
                relief="flat")

style.configure("Treeview.Heading",
                background="#F4F6FB",
                foreground="#333333",
                relief="flat",
                borderwidth=0,
                padding = 5,
                font=("Segoe UI", 10))

style.map("Treeview",
            background=[('selected', '#DCE7FF')],
            foreground=[('selected', '#1A4280')])


# Crear un Notebook para las pestañas
notebook = ttk.Notebook(window)
notebook.pack(fill=BOTH, expand=True)

# Crear la primera pestaña
tab1 = Frame(notebook)
tab1.configure(bg="#FFFFFF")
notebook.add(tab1, text='Simulador de Cobertura')

# Crear la segunda pestaña
tab2 = Frame(notebook)
tab2.configure(bg="#FFFFFF")
notebook.add(tab2, text='Simulador de Capacidad')

# Crear un frame para contener el canvas y el mapa
main_frame = Frame(tab1)
main_frame.configure(bg="#FFFFFF")
main_frame.pack(side=LEFT,fill=BOTH, expand=True)

main_frame2 = Frame(tab1)
main_frame2.configure(bg="#FFFFFF")
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
frame.config(width=500, height=1000)
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
mapaFrame = Frame(main_frame2)
mapaFrame.pack(side=RIGHT)

map_widget = tkintermapview.TkinterMapView(mapaFrame, width=650, height=1000, corner_radius=0)
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

# CAPACIDAD
notebook2 = ttk.Notebook(tab2)
notebook2.pack(fill=BOTH, expand=True)

# Crear la primera pestaña
tab3 = Frame(notebook2)
tab3.configure(bg="#FFFFFF")
notebook2.add(tab3, text='Calculadora de Eficiencia Espectral')

# Crear la segunda pestaña
tab4 = Frame(notebook2)
tab4.configure(bg="#FFFFFF")
notebook2.add(tab4, text='Calculadora de Capacidad')

main_frame3 = Frame(tab3)
main_frame3.configure(bg="#FFFFFF")
main_frame3.pack()

main_frame4 = Frame(tab4)
main_frame4.configure(bg="#FFFFFF")
main_frame4.pack(side=LEFT,fill=BOTH, expand=True)
# ---------- Tabla con todos los datos ----------
label1 = Label(main_frame3, text="Tabla completa de CQI:", bg="#FFFFFF").pack(pady=5)
table_frame = Frame(main_frame3)
table_frame.configure(bg="#FFFFFF")
table_frame.pack()

tree = ttk.Treeview(table_frame, columns=("CQI", "Modulación", "CodeRate", "Bits/Simbolo"), show="headings")
tree.heading("CQI", text="CQI")
tree.heading("Modulación", text="Modulación")
tree.heading("CodeRate", text="Code Rate")
tree.heading("Bits/Simbolo", text="Bits/Simbolo")

for cqi, (mod, rate, bits) in ef.cqi_data.items():
    tree.insert("", "end", values=(cqi, mod, rate, bits))

tree.pack()

# ---------- Selector ----------
selector_frame = Frame(main_frame3)
selector_frame.configure(bg="#FFFFFF")
selector_frame.pack(pady=10)

label2 = Label(selector_frame, text="Selecciona un CQI:", bg="#FFFFFF").grid(row=0, column=0)
cqi_selector = ttk.Combobox(selector_frame, values=list(ef.cqi_data.keys()), width=5)
cqi_selector.grid(row=0, column=1, padx=5)

label3 = Label(selector_frame, text="Porcentaje (%):", bg="#FFFFFF").grid(row=0, column=2)
percent_entry = ttk.Entry(selector_frame, width=5)
percent_entry.grid(row=0, column=3, padx=5)

AñadirCQIBtn = customtkinter.CTkButton(master=selector_frame,
fg_color="BLACK",  # Color del botón
hover_color="BLACK",  # Color del botón al pasar el mouse
font=("Montserrat", 12),  # Fuente utilizada
text="Añadir",
command=ef.select_cqi).grid(row=0, column=4, padx=5)

# ---------- Tabla de selecciones ----------
label4 = Label(main_frame3, text="CQIs seleccionados y porcentaje asignado:", bg='#FFFFFF').pack(pady=5)
history_table = ttk.Treeview(main_frame3, columns=("CQI", "Modulación", "CodeRate", "Bits/Simbolo", "Porcentaje"), show="headings")
for col in ("CQI", "Modulación", "CodeRate", "Bits/Simbolo", "Porcentaje"):
    history_table.heading(col, text=col)
history_table.pack(pady=10)

# ---------- Eficiencia Espectral ----------

bottom_frame = Frame(main_frame3)
bottom_frame.configure(bg="#FFFFFF")
bottom_frame.pack(pady=10)

label5 = Label(bottom_frame, text="Eficiencia Espectral:", bg="#FFFFFF").grid(row=0, column=0)
eficiencia_var = StringVar(value=ef.eficiencia_espectral)
label6 = Label(bottom_frame, textvariable=eficiencia_var, bg="#FFFFFF").grid(row=0, column=1, padx=10)

reinicio= customtkinter.CTkButton(master=bottom_frame,
fg_color="BLACK",  # Color del botón
hover_color="BLACK",  # Color del botón al pasar el mouse
font=("Montserrat", 12),  # Fuente utilizada
text="Reiniciar",
command=ef.reset_all).grid(row=0, column=2, padx=20)


# ---------- Calculo Capacidad ----------

# Btotal_MHz
frame_btotal = Frame(main_frame4, bg="#FFFFFF")
frame_btotal.pack(anchor='w', pady=10)
label_btotal = ttk.Label(frame_btotal, text="Btotal_MHz: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_btotal.pack(side='left')
entry_Btotal_MHz = customtkinter.CTkEntry(frame_btotal)
entry_Btotal_MHz.pack(side='left', fill='x', expand=True)

# Bv_MHz
frame_bv = Frame(main_frame4, bg="#FFFFFF")
frame_bv.pack(anchor='w', pady=10)
label_bv = ttk.Label(frame_bv, text="Bv_MHz: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_bv.pack(side='left')
entry_Bv_MHz = customtkinter.CTkEntry(frame_bv)
entry_Bv_MHz.pack(side='left', fill='x', expand=True)

# Ef
frame_ef = Frame(main_frame4, bg="#FFFFFF")
frame_ef.pack(anchor='w', pady=10)
label_ef = ttk.Label(frame_ef, text="Ef: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_ef.pack(side='left')
entry_Ef = customtkinter.CTkEntry(frame_ef)
entry_Ef.pack(side='left', fill='x', expand=True)

# Pb
frame_pb = Frame(main_frame4, bg="#FFFFFF")
frame_pb.pack(anchor='w', pady=10)
label_pb = ttk.Label(frame_pb, text="Pb: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_pb.pack(side='left')
entry_Pb = customtkinter.CTkEntry(frame_pb)
entry_Pb.pack(side='left', fill='x', expand=True)

# RbCODEC_bps
frame_rbcodec = Frame(main_frame4, bg="#FFFFFF")
frame_rbcodec.pack(anchor='w', pady=10)
label_rbcodec = ttk.Label(frame_rbcodec, text="RbCODEC: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_rbcodec.pack(side='left')
entry_RbCODEC_bps = customtkinter.CTkEntry(frame_rbcodec)
entry_RbCODEC_bps.pack(side='left', fill='x', expand=True)

# trafico_usuario_mErlang
frame_trafico_me = Frame(main_frame4, bg="#FFFFFF")
frame_trafico_me.pack(anchor='w', pady=10)
label_trafico_me = ttk.Label(frame_trafico_me, text="trafico_usuario_mErlang: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_trafico_me.pack(side='left')
entry_trafico_usuario_mErlang = customtkinter.CTkEntry(frame_trafico_me)
entry_trafico_usuario_mErlang.pack(side='left', fill='x', expand=True)

# Trafico_usuario_GB_mes
frame_trafico_gb = Frame(main_frame4, bg="#FFFFFF")
frame_trafico_gb.pack(anchor='w', pady=10)
label_trafico_gb = ttk.Label(frame_trafico_gb, text="Trafico_usuario_GB_mes: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_trafico_gb.pack(side='left')
entry_Trafico_usuario_GB_mes = customtkinter.CTkEntry(frame_trafico_gb)
entry_Trafico_usuario_GB_mes.pack(side='left', fill='x', expand=True)

# porcentaje_BH
frame_porcentaje = Frame(main_frame4, bg="#FFFFFF")
frame_porcentaje.pack(anchor='w', pady=10)
label_porcentaje = ttk.Label(frame_porcentaje, text="porcentaje_BH: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_porcentaje.pack(side='left')
entry_porcentaje_BH = customtkinter.CTkEntry(frame_porcentaje)
entry_porcentaje_BH.pack(side='left', fill='x', expand=True)

# load_sector
frame_load = Frame(main_frame4, bg="#FFFFFF")
frame_load.pack(anchor='w', pady=10)
label_load = ttk.Label(frame_load, text="load_sector: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_load.pack(side='left')
entry_load_sector = customtkinter.CTkEntry(frame_load)
entry_load_sector.pack(side='left', fill='x', expand=True)

# poblacion_cliente
frame_poblacion = Frame(main_frame4, bg="#FFFFFF")
frame_poblacion.pack(anchor='w', pady=10)
label_poblacion = ttk.Label(frame_poblacion, text="poblacion_cliente: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_poblacion.pack(side='left')
entry_poblacion_cliente = customtkinter.CTkEntry(frame_poblacion)
entry_poblacion_cliente.pack(side='left', fill='x', expand=True)

# Submit button
submit_btn = customtkinter.CTkButton(
    master=main_frame4,
    fg_color="#ec3642", #color of the button
    hover_color="RED", #color of the button when mouse is over
    font=("Montserrat", 16), #font used
    corner_radius=12, width=100, #radius of edges and total width
    text="Calcular",
    command=cap.calcular_capacidad
)
submit_btn.pack(pady=20, anchor='w')

# Resultados
frame_resultado1 = Frame(main_frame4, bg="#FFFFFF")
frame_resultado1.pack(anchor='w', pady=10)

label_resultados1 = ttk.Label(frame_resultado1, text="Emplazamientos por Voz: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_resultados1.pack(side='left')
label_resultados1_set = ttk.Label(frame_resultado1, text="", width=10, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_resultados1_set.pack(side='left')

frame_resultado2 = Frame(main_frame4, bg="#FFFFFF")
frame_resultado2.pack(anchor='w', pady=10)

label_resultados2 = ttk.Label(frame_resultado2, text="Emplazamientos por Datos: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_resultados2.pack(side='left')
label_resultados2_set = ttk.Label(frame_resultado2, text="", width=10, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_resultados2_set.pack(side='left')
