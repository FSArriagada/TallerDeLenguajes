import math
from functools import reduce

# ==========================================
# 1. Descuentos e Impuestos
# ==========================================
def calcular_rebaja(monto, porcentaje):
    return monto * (1 - porcentaje / 100)

def sumar_impuesto(monto, porcentaje):
    return monto * (1 + porcentaje / 100)

def procesar_totales(datos, operacion):
    # Usando sum() con un generador en lugar de un bucle for tradicional
    return sum(operacion(item['precio'], item['porcentaje']) for item in datos.values())

separador = "-" * 80
print(separador)
print("Iva: ")
datos_prueba = {'1': {'precio': 100, 'porcentaje': 20}, '2': {'precio': 100, 'porcentaje': 21}}
print(procesar_totales(datos_prueba, sumar_impuesto))
print("\nDescuento: ")
print(procesar_totales(datos_prueba, calcular_rebaja))
print(separador)

# ==========================================
# 2. Calculadora Matemática
# ==========================================
def operar_math():
    limite = int(input('Número: '))
    operador = input('Función (sin, cos, tan, exp, log): ')
    print("\nResultados: ")
    
    # Alternativa segura y más limpia a eval()
    funcion_matematica = getattr(math, operador)
    
    for val in range(1, limite + 1):
        print(f"{val} = {funcion_matematica(val)}")

operar_math()
print(separador)

# ==========================================
# 3. Mapeo de Funciones (Aplicar función)
# ==========================================
def transformar_elementos(accion, elementos):
    # Comprensión de lista en lugar de un for con .append()
    return [accion(e) for e in elementos]

def sumar_uno(x):
    return x + 1

def evaluar_paridad(x):
    return 'par' if x % 2 == 0 else 'impar'

print("Valores incrementados: ", transformar_elementos(sumar_uno, [1, 2, 3, 4, 5]))
print("\nPar o impar: ", transformar_elementos(evaluar_paridad, [1, 2, 3, 4, 5]))
print(separador)

# ==========================================
# 4. Filtro Booleano
# ==========================================
def extraer_si(condicion, elementos):
    # Comprensión de lista en lugar de for + if
    return [e for e in elementos if condicion(e)]

def verificar_par(n):
    return n % 2 == 0

def verificar_impar(n):
    return n % 2 != 0

print("Par: ", extraer_si(verificar_par, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("\nImpar: ", extraer_si(verificar_impar, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(separador)

# ==========================================
# 5. Diccionario de longitudes de palabras
# ==========================================
def mapear_longitudes(oracion):
    # Generador de diccionario simplificado
    return {palabra: len(palabra) for palabra in oracion.split()}

print("Longitud palabras: ")
print(mapear_longitudes('oid mortales el grito sagrado'))
print(separador)

# ==========================================
# 6. Lista de Calificaciones
# ==========================================
def estado_notas_lista(notas):
    # Comprensión de lista en lugar de map/lambda
    return ["aprobado" if nota >= 4 else "desaprobado" for nota in notas]

print("calificaciones: ")
print(estado_notas_lista([8, 7, 2, 4]))
print(separador)

# ==========================================
# 7. Diccionario de Calificaciones
# ==========================================
def boletin_diccionario(materias):
    # Comprensión de diccionario en lugar de dict(map(lambda...))
    return {materia.upper(): ("aprobado" if nota >= 4 else "desaprobado") 
            for materia, nota in materias.items()}

print("Diccionario de calificaciones: ")
print(boletin_diccionario({'matematicas': 8, 'ingles': 7, 'biologia': 2, 'lengua': 4}))
print(separador)

# ==========================================
# 8. Diccionario de Calificaciones Aprobadas
# ==========================================
def filtrar_aprobadas(materias):
    boletin_completo = boletin_diccionario(materias)
    return {materia: estado for materia, estado in boletin_completo.items() if estado == 'aprobado'}

print("Solo Aprobadas: ")
print(filtrar_aprobadas({'matematicas': 8, 'ingles': 7, 'biologia': 2, 'lengua': 4}))
print(separador)

# ==========================================
# 9. Módulo de un vector
# ==========================================
def calcular_distancia(coordenadas):
    # Cálculo directo usando índices para evitar el enredo de reduce
    eje_x = (coordenadas[0][0] - coordenadas[0][1]) ** 2
    eje_y = (coordenadas[1][0] - coordenadas[1][1]) ** 2
    return math.sqrt(eje_x + eje_y)

print("Resultado: ", calcular_distancia([[2, -3], [1, 2]]))
print(separador)

# ==========================================
# 10. Valores Atípicos (Outliers)
# ==========================================
def promedio(valores):
    return sum(valores) / len(valores)

def desvio_estandar(valores):
    media_actual = promedio(valores)
    varianza = sum((x - media_actual) ** 2 for x in valores)
    return math.sqrt(varianza / (len(valores) - 1))

def obtener_z(item, valores):
    return (item - promedio(valores)) / desvio_estandar(valores)

def buscar_outliers(valores):
    # Simplificado usando abs() para chequear atípicos
    return [v for v in valores if abs(obtener_z(v, valores)) > 3]

print(buscar_outliers([1, 2, 3, 34]))