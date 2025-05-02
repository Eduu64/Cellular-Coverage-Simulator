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

window.geometry("1000x800")

window.resizable(True, True)  # (ancho, alto)

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
    selectbackground = "#F9FAFB",
    selectforeground = "#1F2937",  
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
                     sliderlength=40,
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
 # ---------- Treeview ----------

style.configure("Treeview",
                background="#FFFFFF",
                fieldbackground="#FFFFFF",
                foreground="#2E2E2E",
                bordercolor="#FFFFFF",
                borderwidth=0,
                relief="flat",
                highlightthickness=0,  
                selectbackground="#DCE7FF",
                selectforeground="#1A4280")

style.configure("Treeview.Heading",
                background="#F4F6FB",
                foreground="#333333",
                relief="flat",
                borderwidth=0,
                padding=5,
                font=("Segoe UI", 10),
                highlightthickness=0)  

style.map("Treeview",
          background=[('selected', '#DCE7FF')],
          foreground=[('selected', '#1A4280')])






# Crear un Notebook para las pestañas
notebook = ttk.Notebook(window)
notebook.pack(fill=BOTH, expand=True)

# Crear la primera pestaña
tab1 = Frame(notebook)
tab1.configure(background="#FFFFFF")
notebook.add(tab1, text='Simulador de Cobertura')

# Crear la segunda pestaña
tab2 = Frame(notebook)
tab2.configure(background="#FFFFFF")
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
canvas.configure(background="#FFFFFF",highlightbackground="#FFFFFF",highlightcolor="#FFFFFF")
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
frame.configure(bg="#FFFFFF")
canvas.create_window((0, 0), window=frame, anchor='nw')

# Entradas para la interfaz gráfica
frame_coordenadas = Frame(frame, bg="#FFFFFF")
frame_coordenadas.pack(anchor='w', pady=10)

label_id4 = ttk.Label(frame_coordenadas, text="Coordenadas BTS", width=15, font=("Arial", 12), background="#FFFFFF")
label_id4.pack(padx=100)

# Latitud
frame_latitud = Frame(frame, bg="#FFFFFF")
frame_latitud.pack(anchor='w', pady=5)
label_id5 = ttk.Label(frame_latitud, text="Latitud", width=15, font=("Arial", 12), background="#FFFFFF")
label_id5.pack(side='left')
entry_latitud = customtkinter.CTkEntry(frame_latitud, placeholder_text="Latitud")
entry_latitud.pack(side='left', fill='both', expand=True)

# Longitud
frame_longitud = Frame(frame, bg="#FFFFFF")
frame_longitud.pack(anchor='w', pady=5)
label_id6 = ttk.Label(frame_longitud, text="Longitud", width=15, font=("Arial", 12), background="#FFFFFF")
label_id6.pack(side='left')
entry_longitud = customtkinter.CTkEntry(frame_longitud, placeholder_text="Longitud")
entry_longitud.pack(side='left', fill='both', expand=True)

# Parámetros
frame_parametros = Frame(frame, bg="#FFFFFF")
frame_parametros.pack(anchor='w', pady=10)
label_id4_param = ttk.Label(frame_parametros, text="Parametros", width=15, font=("Arial", 12), background="#FFFFFF")
label_id4_param.pack(padx=100)

# Potencia Tx
frame_ptx = Frame(frame, bg="#FFFFFF")
frame_ptx.pack(anchor='w', pady=5)
label_ptx = ttk.Label(frame_ptx, text="Potencia Tx", width=15, font=("Arial", 12), background="#FFFFFF")
label_ptx.pack(side='left')
entry_potenciatx = customtkinter.CTkEntry(frame_ptx, placeholder_text="Ptx")
entry_potenciatx.pack(side='left', fill='x', expand=True)
label_ptx2 = ttk.Label(frame_ptx, text="dBm", font=("Arial", 10), background="#FFFFFF")
label_ptx2.pack(side='left', padx=10)

# Ganancia Tx
frame_gtx = Frame(frame, bg="#FFFFFF")
frame_gtx.pack(anchor='w', pady=5)
label_gtx = ttk.Label(frame_gtx, text="Ganancia Tx", width=15, font=("Arial", 12), background="#FFFFFF")
label_gtx.pack(side='left')
entry_gananciatx = customtkinter.CTkEntry(frame_gtx, placeholder_text="Gtx")
entry_gananciatx.pack(side='left', fill='x', expand=True)
label_gtx2 = ttk.Label(frame_gtx, text="dBi", font=("Arial", 10), background="#FFFFFF")
label_gtx2.pack(side='left', padx=10)

# Ltx
frame_ltx = Frame(frame, bg="#FFFFFF")
frame_ltx.pack(anchor='w', pady=5)
label_ltx = ttk.Label(frame_ltx, text="Ltx", width=15, font=("Arial", 12), background="#FFFFFF")
label_ltx.pack(side='left')
entry_ltx = customtkinter.CTkEntry(frame_ltx, placeholder_text="Ltx")
entry_ltx.pack(side='left', fill='x', expand=True)
label_ltx2 = ttk.Label(frame_ltx, text="dB", font=("Arial", 10), background="#FFFFFF")
label_ltx2.pack(side='left', padx=10)
# Grx
frame_grx = Frame(frame, bg="#FFFFFF")
frame_grx.pack(anchor='w', pady=5)
label_grx = ttk.Label(frame_grx, text="Grx", width=15, font=("Arial", 12), background="#FFFFFF")
label_grx.pack(side='left')
entry_gananciarx = customtkinter.CTkEntry(frame_grx, placeholder_text="Grx")
entry_gananciarx.pack(side='left', fill='x', expand=True)
label_grx2 = ttk.Label(frame_grx, text="dBi", font=("Arial", 10), background="#FFFFFF")
label_grx2.pack(side='left', padx=10)

# Lrx
frame_lrx = Frame(frame, bg="#FFFFFF")
frame_lrx.pack(anchor='w', pady=5)
label_lrx = ttk.Label(frame_lrx, text="Lrx", width=15, font=("Arial", 12), background="#FFFFFF")
label_lrx.pack(side='left')
entry_lrx = customtkinter.CTkEntry(frame_lrx, placeholder_text="Lrx")
entry_lrx.pack(side='left', fill='x', expand=True)
label_lrx2 = ttk.Label(frame_lrx, text="dB", font=("Arial", 10), background="#FFFFFF")
label_lrx2.pack(side='left', padx=10)

# Frecuencia
frame_frecuencia = Frame(frame, bg="#FFFFFF")
frame_frecuencia.pack(anchor='w', pady=5)
label_frecuencia = ttk.Label(frame_frecuencia, text="Frecuencia", width=15, font=("Arial", 12), background="#FFFFFF")
label_frecuencia.pack(side='left')
entry_frecuencia = customtkinter.CTkEntry(frame_frecuencia, placeholder_text="Frecuencia")
entry_frecuencia.pack(side='left', fill='x', expand=True)
label_frecuencia2 = ttk.Label(frame_frecuencia, text="MHz", font=("Arial", 10), background="#FFFFFF")
label_frecuencia2.pack(side='left', padx=10)

# Hb
frame_hb = Frame(frame, bg="#FFFFFF")
frame_hb.pack(anchor='w', pady=5)
label_hb = ttk.Label(frame_hb, text="Altura base", width=15, font=("Arial", 12), background="#FFFFFF")
label_hb.pack(side='left')
entry_alturabase = customtkinter.CTkEntry(frame_hb, placeholder_text="Hb")
entry_alturabase.pack(side='left', fill='x', expand=True)
label_hb2 = ttk.Label(frame_hb, text="m", font=("Arial", 10), background="#FFFFFF")
label_hb2.pack(side='left', padx=10)

# Hm
frame_hm = Frame(frame, bg="#FFFFFF")
frame_hm.pack(anchor='w', pady=5)
label_hm = ttk.Label(frame_hm, text="Altura Móvil", width=15, font=("Arial", 12), background="#FFFFFF")
label_hm.pack(side='left')
entry_alturamovil = customtkinter.CTkEntry(frame_hm, placeholder_text="Hm")
entry_alturamovil.pack(side='left', fill='x', expand=True)
label_hm2 = ttk.Label(frame_hm, text="m", font=("Arial", 10), background="#FFFFFF")
label_hm2.pack(side='left', padx=10)

# RSRP
frame_cobertura = Frame(frame, bg="#FFFFFF")
frame_cobertura.pack(anchor='w', pady=5)
label_cobertura = ttk.Label(frame_cobertura, text="RSRP", width=15, font=("Arial", 12), background="#FFFFFF")
label_cobertura.pack(side='left')
entry_cobertura = customtkinter.CTkEntry(frame_cobertura, placeholder_text="Cobertura")
entry_cobertura.pack(side='left', fill='x', expand=True)
label_cobertura2 = ttk.Label(frame_cobertura, text="dBm", font=("Arial", 10), background="#FFFFFF")
label_cobertura2.pack(side='left', padx=10)

# Per. Añadidas
frame_per_anadidas = Frame(frame, bg="#FFFFFF") #sin ñ por si da problemas
frame_per_anadidas.pack(anchor='w', pady=5)
label_PA = ttk.Label(frame_per_anadidas, text="Per. Añadidas", width=15, font=("Arial", 12), background="#FFFFFF")
label_PA.pack(side='left')
entry_perdidasanadidas = customtkinter.CTkEntry(frame_per_anadidas, placeholder_text="Per. Añadidas")
entry_perdidasanadidas.pack(side='left', fill='x', expand=True)
label_PA2 = ttk.Label(frame_per_anadidas, text="dB", font=("Arial", 10), background="#FFFFFF")
label_PA2.pack(side='left', padx=10)

# Margen
frame_margen = Frame(frame, bg="#FFFFFF")
frame_margen.pack(anchor='w', pady=5)
label_m = ttk.Label(frame_margen, text="Margen (SF/FF)", width=15, font=("Arial", 12), background="#FFFFFF")
label_m.pack(side='left')
entry_margen = customtkinter.CTkEntry(frame_margen, placeholder_text="Margen")
entry_margen.pack(side='left', fill='x', expand=True)
label_m2 = ttk.Label(frame_margen, text="dB", font=("Arial", 10), background="#FFFFFF")
label_m2.pack(side='left', padx=10)

# Radio Buttons DOWNLINK / UPLINK
frame_radio = Frame(frame, bg="#FFFFFF")
frame_radio.pack(anchor='w', pady=10)
radio_var = customtkinter.IntVar()

radio_bt_downlink = customtkinter.CTkRadioButton(
    master=frame_radio,
    variable=radio_var,
    value=1,
    text="DOWNLINK",
    radiobutton_height=18,
    radiobutton_width=18,
    border_width_checked=5,
    border_color="#888",
    fg_color="red",
    hover_color="#ff4d4d",
    text_color="#222"
)
radio_bt_downlink.pack(side='left', padx=10)

radio_bt_uplink = customtkinter.CTkRadioButton(
    master=frame_radio,
    variable=radio_var,
    value=2,
    text="UPLINK",
    radiobutton_height=18,
    radiobutton_width=18,
    border_width_checked=5,
    border_color="#888",
    fg_color="red",
    hover_color="#ff4d4d",
    text_color="#222"
)
radio_bt_uplink.pack(side='left', padx=10)

# Desplegable 1: selección cálculo
frame_desplegable1 = Frame(frame, bg="#FFFFFF")
frame_desplegable1.pack(anchor='w', pady=5)
desplegable = ttk.Combobox(frame_desplegable1, width=50, values=["Cálculo eNodes", "Sector 1", "Sector 2", "Sector 3"])
desplegable.pack(fill='x', expand=True)

# Desplegable 2: selección modelo
frame_desplegable2 = Frame(frame, bg="#FFFFFF")
frame_desplegable2.pack(anchor='w', pady=5)
desplegable2 = ttk.Combobox(frame_desplegable2, width=50, values=["Okumura Hata", "COST231"])
desplegable2.pack(fill='x', expand=True)

# Botón Calcular
frame_boton = Frame(frame, bg="#FFFFFF")
frame_boton.pack(anchor='w', pady=15)
button_id22 = customtkinter.CTkButton(
    master=frame_boton,
    fg_color="#ec3642",  # color del botón
    hover_color="RED",  # color cuando el cursor está encima
    font=("Montserrat", 16),
    corner_radius=12,
    width=100,
    text="Calcular",
    command=calcular
)
button_id22.pack(padx=100)

# Configuración del mapa
mapaFrame = Frame(main_frame2)
mapaFrame.pack(side=RIGHT,fill=BOTH, expand=True)

map_widget = tkintermapview.TkinterMapView(mapaFrame, width=650, height=1000, corner_radius=0)
map_widget.set_position(40.41, -3.7)
map_widget.set_zoom(12)
map_widget.pack(fill=BOTH, expand=True)

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

# Area Territorio
frame_area = Frame(frame, bg="#FFFFFF")
frame_area.pack(anchor='w', pady=5)

label_area = ttk.Label(frame_area, text="Area Territorio:", font=("Arial", 12), background="#FFFFFF")
label_area.pack(side='left')

label_area_set = Label(frame_area, text="0", font=("Arial", 12), background="#FFFFFF")
label_area_set.pack(side='left', padx=(10,0))

# Area Total Territorio
frame_area_total = Frame(frame, bg="#FFFFFF")
frame_area_total.pack(anchor='w', pady=5)
label_total_area = ttk.Label(frame_area_total, text="Area Total Territorio:", font=("Arial", 12), background="#FFFFFF")
label_total_area.pack(side='left')
label_total_area_set = Label(frame_area_total, text="0", font=("Arial", 12), background="#FFFFFF")
label_total_area_set.pack(side='left', padx=(10,0))

# Estimación eNodes necesarios
frame_enodes = Frame(frame, bg="#FFFFFF")
frame_enodes.pack(anchor='w', pady=5)
label_enodes = ttk.Label(frame_enodes, text="Estimación eNodes necesarios:", font=("Arial", 12), background="#FFFFFF")
label_enodes.pack(side='left')
label_enodes_set = ttk.Label(frame_enodes, text="0", font=("Arial", 12), background="#FFFFFF")
label_enodes_set.pack(side='left', padx=(10,0))


frame_AUX = Frame(frame, bg="#FFFFFF")
frame_AUX.pack(anchor='w', pady=20)

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
bottom_frame.configure(background="#FFFFFF")
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
label_btotal = ttk.Label(frame_btotal, text="Bandwith Total: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_btotal.pack(side='left')
entry_Btotal_MHz = customtkinter.CTkEntry(frame_btotal)
entry_Btotal_MHz.pack(side='left', fill='x', expand=True)
label_btotal2 = ttk.Label(frame_btotal, text="MHz", width=10, anchor='w', font=("Arial", 10), background="#FFFFFF", padding=[5,0])
label_btotal2.pack(side='left')

# Bv_MHz
frame_bv = Frame(main_frame4, bg="#FFFFFF")
frame_bv.pack(anchor='w', pady=10)
label_bv = ttk.Label(frame_bv, text="Bandwith Voz: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_bv.pack(side='left')
entry_Bv_MHz = customtkinter.CTkEntry(frame_bv)
entry_Bv_MHz.pack(side='left', fill='x', expand=True)
label_bv2 = ttk.Label(frame_bv, text="MHz", width=10, anchor='w', font=("Arial", 10), background="#FFFFFF", padding=[5,0])
label_bv2.pack(side='left')

# Ef
frame_ef = Frame(main_frame4, bg="#FFFFFF")
frame_ef.pack(anchor='w', pady=10)
label_ef = ttk.Label(frame_ef, text="Eficiencia Espectral: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_ef.pack(side='left')
entry_Ef = customtkinter.CTkEntry(frame_ef)
entry_Ef.pack(side='left', fill='x', expand=True)
label_ef2 = ttk.Label(frame_ef, text="bps/Hz", width=10, anchor='w', font=("Arial", 10), background="#FFFFFF", padding=[5,0])
label_ef2.pack(side='left')

# Pb
frame_pb = Frame(main_frame4, bg="#FFFFFF")
frame_pb.pack(anchor='w', pady=10)
label_pb = ttk.Label(frame_pb, text="Probabilidad de Bloqueo: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_pb.pack(side='left')
entry_Pb = customtkinter.CTkEntry(frame_pb)
entry_Pb.pack(side='left', fill='x', expand=True)
label_pb2 = ttk.Label(frame_pb, text="%", width=10, anchor='w', font=("Arial", 10), background="#FFFFFF", padding=[5,0])
label_pb2.pack(side='left')

# RbCODEC_bps
frame_rbcodec = Frame(main_frame4, bg="#FFFFFF")
frame_rbcodec.pack(anchor='w', pady=10)
label_rbcodec = ttk.Label(frame_rbcodec, text="RbCODEC: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_rbcodec.pack(side='left')
entry_RbCODEC_bps = customtkinter.CTkEntry(frame_rbcodec)
entry_RbCODEC_bps.pack(side='left', fill='x', expand=True)
label_rbcodec2 = ttk.Label(frame_rbcodec, text="Kbps", width=10, anchor='w', font=("Arial", 10), background="#FFFFFF", padding=[5,0])
label_rbcodec2.pack(side='left')

# trafico_usuario_mErlang
frame_trafico_me = Frame(main_frame4, bg="#FFFFFF")
frame_trafico_me.pack(anchor='w', pady=10)
label_trafico_me = ttk.Label(frame_trafico_me, text="Tráfico usuario móvil: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_trafico_me.pack(side='left')
entry_trafico_usuario_mErlang = customtkinter.CTkEntry(frame_trafico_me)
entry_trafico_usuario_mErlang.pack(side='left', fill='x', expand=True)
label_trafico_me2 = ttk.Label(frame_trafico_me, text="mErlangs", width=10, anchor='w', font=("Arial", 10), background="#FFFFFF", padding=[5,0])
label_trafico_me2.pack(side='left')

# Trafico_usuario_GB_mes
frame_trafico_gb = Frame(main_frame4, bg="#FFFFFF")
frame_trafico_gb.pack(anchor='w', pady=10)
label_trafico_gb = ttk.Label(frame_trafico_gb, text="Tráfico usuario mensual: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_trafico_gb.pack(side='left')
entry_Trafico_usuario_GB_mes = customtkinter.CTkEntry(frame_trafico_gb)
entry_Trafico_usuario_GB_mes.pack(side='left', fill='x', expand=True)
label_trafico_gb2 = ttk.Label(frame_trafico_gb, text="GB/mes", width=10, anchor='w', font=("Arial", 10), background="#FFFFFF", padding=[5,0])
label_trafico_gb2.pack(side='left')
# porcentaje_BH
frame_porcentaje = Frame(main_frame4, bg="#FFFFFF")
frame_porcentaje.pack(anchor='w', pady=10)
label_porcentaje = ttk.Label(frame_porcentaje, text="Porcentaje de Tráfico en BH: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_porcentaje.pack(side='left')
entry_porcentaje_BH = customtkinter.CTkEntry(frame_porcentaje)
entry_porcentaje_BH.pack(side='left', fill='x', expand=True)
label_porcentaje2 = ttk.Label(frame_porcentaje, text="%", width=10, anchor='w', font=("Arial", 10), background="#FFFFFF", padding=[5,0])
label_porcentaje2.pack(side='left')

# load_sector
frame_load = Frame(main_frame4, bg="#FFFFFF")
frame_load.pack(anchor='w', pady=10)
label_load = ttk.Label(frame_load, text="Carga del sector: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
label_load.pack(side='left')
entry_load_sector = customtkinter.CTkEntry(frame_load)
entry_load_sector.pack(side='left', fill='x', expand=True)
label_load2 = ttk.Label(frame_load, text="%", width=10, anchor='w', font=("Arial", 10), background="#FFFFFF", padding=[5,0])
label_load2.pack(side='left')

# poblacion_cliente
frame_poblacion = Frame(main_frame4, bg="#FFFFFF")
frame_poblacion.pack(anchor='w', pady=10)
label_poblacion = ttk.Label(frame_poblacion, text="Población cliente: ", width=30, anchor='w', font=("Arial", 12), background="#FFFFFF")
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
