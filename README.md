# 📡 Cellular Coverage Simulator

## 🚀 Descripción
Herramienta diseñada para estimar la cobertura de redes celulares (LTE) y simular la radiación de estaciones base. Utiliza coordenadas geográficas y datos demográficos para ofrecer cálculos precisos sobre la distribución de la señal.

---

## 🛠️ Instrucciones de Uso

### 📍 Estimación de Bases Necesarias
1. **Rellenar los parámetros**, y elegir modelo de estudio además de las coordenadas, para que el programa estime la demografía de la localidad. *(Puedes copiar las coordenadas haciendo clic derecho en el mapa y luego clic izquierdo sobre ellas).*  
2. **Seleccionar la opción** "Cálculo de eNodes" en el primer desplegable.  
3. **Hacer clic en** el botón **"Calcular"**.  
4. **Añadir las ciudades** en el buscador y hacer clic en **"Buscar"**.  

### 📡 Simulación de Radiación de la Base
1. **Rellenar los parámetros**, incluyendo las coordenadas y el modelo de estudio. *(Puedes copiar las coordenadas haciendo clic derecho en el mapa y luego clic izquierdo sobre ellas).*  
2. **Seleccionar el sector** a analizar en el primer desplegable.  
3. **Hacer clic en** el botón **"Calcular"**.

### 🕡 Cálculo de Eficiencia Espectral
1. **Elegir CQI**, incluyendo el porcentaje que aplica a cada nivel de calidad según los requerimientos que nos piden.*
2. **Hacer clic en** el botón de **"Añadir"**.
3. Automaticamente se enviará el valor al simulador de capacidad.

### 📦 Simulación de Capacidad de la Base
1. **Rellenar los parámetros**, incluyendo la eficiencia espectral si anteriormente no se ha calculado*  
3. **Hacer clic en** el botón **"Calcular"**.

💡 **Nota:** Puedes automatizar el estudio de los tres sectores y la adición de coordenadas haciendo clic derecho en el mapa y luego clic izquierdo sobre **"Añadir BTS"**.  

⚠️ **Importante** <br/>

Para poder usar las imágenes en el proyecto, debes cambiar el path dentro del código. Asegúrate de que las rutas de las imágenes en tu entorno de desarrollo sean correctas, de lo contrario, el programa no podrá cargarlas correctamente.

---

## 📦 Librerías Utilizadas
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

## 🎥 Demostración
### 🔹 Interfaz de Usuario
![image](https://github.com/user-attachments/assets/1e556c10-53c1-46f1-8d96-0a991e9ba9a5)

### 🔹 Estimación de bases en Cobertura
![image](https://github.com/user-attachments/assets/affa2a6d-3fee-4b7e-be85-b18abe581454)

### 🔹 Ventana emergente auxiliar
![image](https://github.com/user-attachments/assets/2ba80318-d9f3-4ec7-864a-2ef85c0db97d)

### 🔹 Visualización de Resultados de Cobertura
![image](https://github.com/user-attachments/assets/ec0525af-1576-4fc2-8912-9a7560973083)

### 🔹 Cálculo de Eficiencia Espectral a través de CQI (After release 12 3GPP)
![image](https://github.com/user-attachments/assets/5b4b5d11-de4b-4840-97fd-45af243319b4)

## 🔹 Ventana emergente gestión de errores
![image](https://github.com/user-attachments/assets/439c73c4-8846-422e-b08c-8aa277590e61)

![image](https://github.com/user-attachments/assets/57e6bd71-7d81-4088-9ad4-1942ca367c47)

### 🔹 Cálculo Emplazamientos Voz y Datos
![image](https://github.com/user-attachments/assets/a062a77c-ba4c-4d4d-a95a-f8336b2790f5)

---


