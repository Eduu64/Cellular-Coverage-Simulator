import math
import GUI
import tkinter as tk
from tkinter import messagebox

class Eficiencia:
    # Datos de CQI (tabla derecha de la imagen)
    cqi_data = {
        1: ("QPSK", 0.0762, 2),
        2: ("QPSK", 0.12, 2),
        3: ("QPSK", 0.193, 2),
        4: ("QPSK", 0.308, 2),
        5: ("QPSK", 0.449, 2),
        6: ("QPSK", 0.6016, 2),
        7: ("16QAM", 0.378, 4),
        8: ("16QAM", 0.490, 4),
        9: ("16QAM", 0.616, 4),
        10: ("64QAM", 0.466, 6),
        11: ("64QAM", 0.567, 6),
        12: ("64QAM", 0.666, 6),
        13: ("64QAM", 0.772, 6),
        14: ("64QAM", 0.873, 6),
        15: ("64QAM", 0.948, 6),
    }

    # Lista para guardar elecciones
    selected_cqis = []
    assigned_percentages = []
    eficiencia_espectral_unitaria = 0
    eficiencia_espectral = 0

    # Función al seleccionar un CQI
    def select_cqi(self):
        try:
            cqi = int(GUI.cqi_selector.get())
            percent = float(GUI.percent_entry.get())
        except ValueError:
            messagebox.showwarning("Error", "Introduce un valor válido.")
            return

        if percent <= 0 or percent > 100:
            messagebox.showerror("Error", "El porcentaje debe estar entre 0 y 100.")
            return

        if cqi in self.selected_cqis:
            messagebox.showinfo("Info", f"El CQI {cqi} ya ha sido seleccionado.")
            return

        total = sum(self.assigned_percentages) + percent

        if total > 100:
            messagebox.showerror("Error", f"El total de porcentaje excede 100%. Actualmente: {sum(self.assigned_percentages)}%.")
            return

        self.selected_cqis.append(cqi)
        self.assigned_percentages.append(percent)

        self.calculo_eficiencia(cqi,percent)
        self.update_history_table()

    def update_history_table(self):
        # Limpia y actualiza la tabla de selección
        for i in GUI.history_table.get_children():
            GUI.history_table.delete(i)

        for i, cqi in enumerate(self.selected_cqis):
            mod, rate, bits = self.cqi_data[cqi]
            GUI.history_table.insert("", "end", values=(cqi, mod, rate, bits, f"{self.assigned_percentages[i]}%"))

    def calculo_eficiencia(self,cqi,percent):
        mod, rate, bits = self.cqi_data[cqi]
        tasa_binaria_CQI = 168*1e3 * rate * bits
        eficiencia_espectral_unitaria = tasa_binaria_CQI/(200*1e3)
        self.eficiencia_espectral += (eficiencia_espectral_unitaria * (percent/100))
        GUI.eficiencia_var.set(self.eficiencia_espectral)
        GUI.entry_Ef.delete(0,tk.END)
        GUI.entry_Ef.insert(0,self.eficiencia_espectral)


    def reset_all(self):
        self.selected_cqis.clear()
        self.assigned_percentages.clear()
        self.update_history_table()
        GUI.eficiencia_var.set("0")
        GUI.cqi_selector.set("")
        GUI.percent_entry.delete(0, tk.END)
        self.eficiencia_espectral = 0

class Capacidad:

    def erlang_b(self, A, N):
        numerator = (A ** N) / math.factorial(N)
        denominator = sum((A ** k) / math.factorial(k) for k in range(N + 1))
        return numerator / denominator
    
    def erlangs(self, N, Pb, epsilon=1e-4, max_A=2000, debug=False):
        A = 0.0
        while A < max_A:
            Pb1 = self.erlang_b(A, N)
            if debug:
                print(f"Trying A={A:.4f}, Pb1={Pb1:.6f}")
            if abs(Pb1 - Pb) < epsilon:
                return A
            A += 0.01
        if debug:
            print("No suitable A found within max_A")
        return None  
    
    def calcular_capacidad_voz(self, Bv_MHz, Ef, RbCODEC_bps, trafico_usuario_mErlang, poblacion_cliente, Pb):
        Bv_Hz = Bv_MHz * 1e6
        N_canales_voz = (Bv_Hz * Ef) / (RbCODEC_bps * 1e3)
        #print(f"N_canales_voz: {N_canales_voz}")
        N_canales_voz_neto = int(N_canales_voz * 0.85)  # restamos 15% para señalización
        #print(f"N_canales_voz_neto: {N_canales_voz_neto}")
        trafico_total_voz = self.erlangs(N_canales_voz_neto, Pb / 100)
        #print(f"trafico_total_voz: {trafico_total_voz}")
        if trafico_total_voz is None:
            print("Error: No se pudo calcular el tráfico total de voz. Verifique los parámetros de entrada.")
            return None
        trafico_usuario_Erlang = trafico_usuario_mErlang / 1000
        #print(f"trafico_usuario_Erlang: {trafico_usuario_Erlang}")
        if trafico_usuario_Erlang == 0:
            print("Error: trafico_usuario_Erlang es cero, no se puede dividir.")
            return None
        N_usuarios_voz_sector = trafico_total_voz / trafico_usuario_Erlang
        N_usuarios_voz_emplazamiento = N_usuarios_voz_sector * 3
        if N_usuarios_voz_emplazamiento == 0:
            print("Error: N_usuarios_voz_emplazamiento es cero, no se puede dividir.")
            return None
        N_emplazamientos_voz = poblacion_cliente / N_usuarios_voz_emplazamiento
        return N_emplazamientos_voz
    
    def calcular_capacidad_datos(self,Btotal_MHz, Bv_MHz, Ef, load_sector, Trafico_usuario_GB_mes, porcentaje_BH, poblacion_cliente):
        Bd_MHz = Btotal_MHz - Bv_MHz

        C_T_Mbps = Ef * Bd_MHz 
        C_media_Mbps = C_T_Mbps * (load_sector/100)
        C_media_Gbps = C_media_Mbps / 1000

        Trafico_diario_BH_Gbps = ((Trafico_usuario_GB_mes / 30) * (porcentaje_BH/100) * (8)) / 3600

        N_usuarios_sector = C_media_Gbps / Trafico_diario_BH_Gbps
        N_usuarios_emplazamiento = N_usuarios_sector * 3

        N_emplazamientos_datos = poblacion_cliente / N_usuarios_emplazamiento

        return N_emplazamientos_datos
    
    def calcular_capacidad(self):

        val_Btotal_MHz = float(GUI.entry_Btotal_MHz.get())
        val_Bv_MHz = float(GUI.entry_Bv_MHz.get())
        val_Ef = float(GUI.entry_Ef.get())
        val_Pb = float(GUI.entry_Pb.get())
        val_RbCODEC_bps = float(GUI.entry_RbCODEC_bps.get())
        val_trafico_usuario_mErlang = float(GUI.entry_trafico_usuario_mErlang.get())
        val_Trafico_usuario_GB_mes = float(GUI.entry_Trafico_usuario_GB_mes.get())
        val_porcentaje_BH = float(GUI.entry_porcentaje_BH.get())
        val_load_sector = float(GUI.entry_load_sector.get())
        val_poblacion_cliente = int(GUI.entry_poblacion_cliente.get())

        N_emplazamientos_voz = self.calcular_capacidad_voz(val_Bv_MHz, val_Ef, val_RbCODEC_bps, val_trafico_usuario_mErlang, val_poblacion_cliente, val_Pb)
        N_emplazamientos_datos = self.calcular_capacidad_datos(val_Btotal_MHz, val_Bv_MHz, val_Ef, val_load_sector, val_Trafico_usuario_GB_mes, val_porcentaje_BH, val_poblacion_cliente)

        GUI.label_resultados1_set.configure(text= math.ceil(N_emplazamientos_voz))
        GUI.label_resultados2_set.configure(text=math.ceil(N_emplazamientos_datos))

ef = Eficiencia()
cap = Capacidad()
    











