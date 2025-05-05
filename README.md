# 📡 **Simulador de Estaciones Móviles** / **Cellular Stations Simulator**

## 🚀 Descripción / Description  
**ES:**  
Herramienta diseñada para estimar la **cobertura y capacidad de redes móviles (LTE)** y simular los **patrones de radiación de estaciones base**. Utiliza **coordenadas geográficas** y **datos demográficos** para ofrecer cálculos precisos sobre la distribución de la señal.  

**EN:**  
A tool designed to estimate **mobile network (LTE) coverage and capacity**, and simulate **base station radiation patterns**. It leverages **geographic coordinates** and **demographic data** to provide accurate signal distribution calculations.

---

## 🛠️ Instrucciones de Uso / How to Use

### 📍 Estimación de Bases Necesarias / Estimate Required Base Stations  
**ES:**  
1. Rellenar los parámetros y elegir modelo de estudio y coordenadas. *(Clic derecho en el mapa → clic izquierdo para copiar coordenadas).*  
2. Seleccionar "Cálculo de eNodes".  
3. Hacer clic en **"Calcular"**.  
4. Añadir ciudades desde el buscador y hacer clic en **"Buscar"**.  

**EN:**  
1. Fill in parameters and select model and coordinates. *(Right-click on the map → left-click to copy coordinates).*  
2. Select "eNode Calculation".  
3. Click **"Calculate"**.  
4. Add cities from the search bar and click **"Search"**.

---

### 📡 Simulación de Radiación / Radiation Simulation  
**ES:**  
1. Ingresar parámetros, incluyendo coordenadas y modelo.  
2. Seleccionar el sector en el primer desplegable.  
3. Clic en **"Calcular"**.  

💡 Puedes automatizar los 3 sectores con clic derecho → **"Añadir BTS"**.

**EN:**  
1. Enter parameters, including coordinates and model.  
2. Select the sector from the dropdown menu.  
3. Click **"Calculate"**.  

💡 You can automate all 3 sectors with right-click → **"Add BTS"**.

---

### ⚙️ Eficiencia Espectral / Spectral Efficiency  
**ES:**  
1. Elegir valores de CQI con su porcentaje.  
2. Hacer clic en **"Añadir"**.  
3. Se envía automáticamente al simulador.  

**EN:**  
1. Select CQI values and percentages.  
2. Click **"Add"**.  
3. Values are automatically sent to the simulator.

---

### 📶 Simulación de Capacidad / Capacity Simulation  
**ES:**  
1. Ingresar los parámetros y eficiencia espectral (si no se calculó antes).  
2. Clic en **"Calcular"**.  

**EN:**  
1. Enter parameters and spectral efficiency (if not calculated earlier).  
2. Click **"Calculate"**.

⚠️ **Importante / Important**  
**ES:** Asegúrate de corregir las rutas de imágenes en el código para que se visualicen correctamente.  
**EN:** Make sure to correct image paths in the code so that visuals load properly.

---

## 📦 Librerías / Libraries Used  
Instalación rápida / Quick install:
```bash
pip install tkintermapview customtkinter geopy pyproj shapely requests
```
- `tkinter`  
- `tkintermapview`  
- `customtkinter`  
- `math`  
- `geopy`  
- `pyproj`  
- `shapely`  
- `requests`  

---

## 🎥 Demo
### 🔹 Interfaz de Usuario / User Interface
![image](https://github.com/user-attachments/assets/1e556c10-53c1-46f1-8d96-0a991e9ba9a5)

### 🔹 Estimación de bases en Cobertura / Coverage Estimation
![image](https://github.com/user-attachments/assets/affa2a6d-3fee-4b7e-be85-b18abe581454)

### 🔹 Ventana emergente auxiliar / Auxiliary Pop-up
![image](https://github.com/user-attachments/assets/2ba80318-d9f3-4ec7-864a-2ef85c0db97d)

### 🔹 Visualización de Resultados de Cobertura / Coverage Results
![image](https://github.com/user-attachments/assets/ec0525af-1576-4fc2-8912-9a7560973083)

### 🔹 Cálculo de Eficiencia Espectral a través de CQI (After release 12 3GPP) / CQI-based Spectral Efficiency
![image](https://github.com/user-attachments/assets/5b4b5d11-de4b-4840-97fd-45af243319b4)

## 🔹 Ventana emergente gestión de errores / Error Handling
![image](https://github.com/user-attachments/assets/439c73c4-8846-422e-b08c-8aa277590e61)

![image](https://github.com/user-attachments/assets/57e6bd71-7d81-4088-9ad4-1942ca367c47)

### 🔹 Cálculo Emplazamientos Voz y Datos / Voice & Data Sites
![image](https://github.com/user-attachments/assets/a062a77c-ba4c-4d4d-a95a-f8336b2790f5)

---


