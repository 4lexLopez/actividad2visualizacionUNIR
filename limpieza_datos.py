import pandas as pd

# -------------------------------------------------------------
# 1. CREACIÓN DE UN ARCHIVO DE PRUEBA (Para que puedas ejecutarlo)
# -------------------------------------------------------------
# Creamos un diccionario con datos duplicados, nulos y textos con espacios.
datos_ficticios = {
    'Nombre': [' Carlos ', 'Ana', 'Carlos ', 'Luis', 'Sofia', 'Pedro'],
    'Edad': [25, 17, 25, None, 32, 19],
    'Ciudad': ['Bogota', 'Medellin', 'Bogota', 'Cali', 'Bogota', 'Bogota'],
    'Ingresos': [1500, 800, 1500, 1200, None, 950]
}

# Guardamos el archivo inicial para simular tu archivo real
df_inicial = pd.DataFrame(datos_ficticios)
df_inicial.to_csv('datos_sucios.csv', index=False)
print("--- Archivo 'datos_sucios.csv' creado con éxito ---")


# -------------------------------------------------------------
# 2. PROCESO DE LIMPIEZA Y FILTRADO REAL
# -------------------------------------------------------------

# Paso A: Cargar el archivo de datos
df = pd.read_csv('datos_sucios.csv')
print("\nDatos originales cargados:")
print(df)

# Paso B: Limpieza de Datos
# 1. Eliminar filas completamente duplicadas
df = df.drop_duplicates()

# 2. Corregir textos: quitar espacios en blanco al inicio/final y estandarizar
df['Nombre'] = df['Nombre'].astype(str).str.strip()
df['Ciudad'] = df['Ciudad'].astype(str).str.strip()

# 3. Manejar valores nulos (NaN)
# Reemplazamos los ingresos faltantes con el promedio de la columna
promedio_ingresos = df['Ingresos'].mean()
df['Ingresos'] = df['Ingresos'].fillna(promedio_ingresos)

# Eliminamos filas que aún tengan nulos en la columna 'Edad'
df = df.dropna(subset=['Edad'])

print("\nDatos después de la limpieza:")
print(df)

# Paso C: Filtrado de Datos
# Filtramos solo las personas mayores de edad (>= 18) que vivan en 'Bogota'
condicion_edad = df['Edad'] >= 18
condicion_ciudad = df['Ciudad'] == 'Bogota'

df_filtrado = df[condicion_edad & condicion_ciudad]
print("\nDatos finales filtrados (Mayores de 18 en Bogota):")
print(df_filtrado)


# -------------------------------------------------------------
# 3. EXPORTAR EL RESULTADO
# -------------------------------------------------------------
# Guardamos los datos limpios en un nuevo archivo CSV sin el índice numérico
df_filtrado.to_csv('datos_limpios.csv', index=False)
print("\n--- ¡Proceso completado! Archivo 'datos_limpios.csv' guardado ---")|q