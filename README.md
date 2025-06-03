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
1. Añadir ciudades desde el buscador y hacer clic en **"Añadir"**.  
2. Rellenar los parámetros y elegir modelo de estudio.   
3. Hacer clic en **"Calcular"**.  

**EN:**  
1. Add cities from the search bar and click **"Add"**.
2. Fill in parameters and select model and coordinates. 
3. Click **"Calculate"**.

![5](https://github.com/user-attachments/assets/7ab65f99-3f16-4d74-acff-72c5314557d8)

---

### 📡 Simulación de Radiación / Radiation Simulation  
**ES:**  
1. Ingresar parámetros, incluyendo coordenadas y modelo.  *(Clic derecho en el mapa → clic izquierdo para copiar coordenadas).*
2. Clic en **"Calcular"**.  

💡 Puedes automatizar la posición ubicación de estación con clic derecho → **"Añadir BTS"**.

**EN:**  
1. Enter parameters, including coordinates and model.  *(Right-click on the map → left-click to copy coordinates).*  
2. Click **"Calculate"**.  

💡 You can automate the station placement by right-clicking → **"Add BTS"**.

![2](https://github.com/user-attachments/assets/aa538959-73c6-48a4-994e-89f493ae7b11)

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

![3](https://github.com/user-attachments/assets/277ff0e5-74f1-4efd-8a4f-ea37f8e9d66f)

---

### 📶 Simulación de Capacidad / Capacity Simulation  
**ES:**  
1. Ingresar los parámetros y eficiencia espectral (si no se calculó antes).  
2. Clic en **"Calcular"**.  

**EN:**  
1. Enter parameters and spectral efficiency (if not calculated earlier).  
2. Click **"Calculate"**.

![4](https://github.com/user-attachments/assets/66ea2880-8598-4fbe-a693-12c9749fb7bc)

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
### 🔹 Simulación de cobertura / Coverage simulation
![image](https://github.com/user-attachments/assets/4256128e-8a24-4d80-b034-9eaa97c37c0d)
![image](https://github.com/user-attachments/assets/f08dcfe1-217b-41e4-8aea-dc61e473805f)

### 🔹 Estimación de bases en Cobertura / Coverage Estimation
![image](https://github.com/user-attachments/assets/4afa6d37-f91e-4ec5-bf40-ea79751fee9e)
![image](https://github.com/user-attachments/assets/163b395c-5b7c-4e0c-a6d3-c9cc505c6c16)

### 🔹 Ventana emergente auxiliar / Auxiliary Pop-up
![image](https://github.com/user-attachments/assets/4fa62e3c-42e2-4de9-a2ff-5e01aeba16f9)

### 🔹 Cálculo de Eficiencia Espectral a través de CQI (After release 12 3GPP) / CQI-based Spectral Efficiency
![image](https://github.com/user-attachments/assets/5b4b5d11-de4b-4840-97fd-45af243319b4)

## 🔹 Ventana emergente gestión de errores / Error Handling
![image](https://github.com/user-attachments/assets/439c73c4-8846-422e-b08c-8aa277590e61)

![image](https://github.com/user-attachments/assets/57e6bd71-7d81-4088-9ad4-1942ca367c47)

### 🔹 Cálculo Emplazamientos Voz y Datos / Voice & Data Sites
![image](https://github.com/user-attachments/assets/d2700c19-2874-4132-ba07-d2d660a0f762)

---


