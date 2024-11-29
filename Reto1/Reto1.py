
import datetime
import matplotlib.pyplot as plt


# Lista para almacenar los experimentos
experimentos = []

# Función para agregar un experimento
def agregar_experimento():
    print("\n--- Agregar Experimento ---")
    nombre = input("Nombre del experimento: ")
    while True:
        fecha = input("Fecha de realización (DD/MM/AAAA): ")
        try:
            fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Fecha inválida. Intente nuevamente.")
    
    tipos_validos = ["Química", "Biología", "Física"]
    tipo = input(f"Tipo de experimento ({', '.join(tipos_validos)}): ")
    if tipo not in tipos_validos:
        print("Tipo inválido. Debe ser Química, Biología o Física.")
        return
    
    resultados = input("Ingrese los resultados numéricos separados por comas: ")
    try:
        resultados = [float(x) for x in resultados.split(",")]
    except ValueError:
        print("Los resultados deben ser números separados por comas.")
        return
    
    experimento = {
        "nombre": nombre,
        "fecha": fecha,
        "tipo": tipo,
        "resultados": resultados
    }
    experimentos.append(experimento)
    print("Experimento agregado con éxito.")

# Función para visualizar los experimentos
def ver_experimentos():
    print("\n--- Lista de Experimentos ---")
    if not experimentos:
        print("No hay experimentos registrados.")
        return
    for i, exp in enumerate(experimentos):
        print(f"{i + 1}. {exp['nombre']} - {exp['fecha']} - {exp['tipo']}")
        print(f"   Resultados: {exp['resultados']}")


# Función para calcular estadísticas básicas
def estadisticas():
    print("\n--- Cálculo de Estadísticas ---")
    ver_experimentos()  # Suponiendo que esta función lista los experimentos
    if not experimentos:
        return
    try:
        indice = int(input("Seleccione el número del experimento: ")) - 1
        exp = experimentos[indice]
    except (ValueError, IndexError):
        print("Selección inválida.")
        return
    
    resultados = exp["resultados"]
    promedio = sum(resultados) / len(resultados)
    maximo = max(resultados)
    minimo = min(resultados)
    
    # Mostrar estadísticas básicas
    print(f"\nEstadísticas de {exp['nombre']}:")
    print(f"  Promedio: {promedio:.2f}")
    print(f"  Máximo: {maximo}")
    print(f"  Mínimo: {minimo}")
    
    # Crear la gráfica de barras
    plt.figure(figsize=(8, 6))
    plt.bar(range(1, len(resultados) + 1), resultados, color='skyblue')
    plt.xlabel('Intentos')
    plt.ylabel('Resultado')
    plt.title(f"Resultados del Experimento: {exp['nombre']}")
    
    # Mostrar las estadísticas en el gráfico
    plt.axhline(promedio, color='r', linestyle='--', label=f'Promedio: {promedio:.2f}')
    plt.axhline(maximo, color='g', linestyle='--', label=f'Máximo: {maximo}')
    plt.axhline(minimo, color='b', linestyle='--', label=f'Mínimo: {minimo}')
    
    plt.legend()
    plt.show()

# Función para comparar experimentos
def comparar_experimentos():
    print("\n--- Comparación de Experimentos ---")
    ver_experimentos()
    if len(experimentos) < 2:
        print("Se necesitan al menos dos experimentos para comparar.")
        return
    
    try:
        indices = input("Seleccione los números de los experimentos a comparar (separados por comas): ")
        indices = [int(x) - 1  for x in indices.split(",")]
        seleccionados = [experimentos[i] for i in indices]
        
    except (ValueError, IndexError):
        print("Selección inválida.")
        return
    
    maximo_experimento = max(seleccionados, key=lambda x: max(x["resultados"]))
    minimo_experimento = min(seleccionados, key=lambda x: min(x["resultados"]))
    print(f"\nEl experimento con el mejor resultado es: {maximo_experimento['nombre']}")
    print(f"El experimento con el peor resultado es: {minimo_experimento['nombre']}")

# Función para generar un informe
def generar_informe():
    print("\n--- Generación de Informe ---")
    if not experimentos:
        print("No hay experimentos para generar un informe.")
        return
    
    nombre_archivo = "informe_experimentos.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:  # Especificamos la codificación UTF-8
        archivo.write("Informe de Experimentos Científicos\n")
        archivo.write("=" * 40 + "\n")
        for exp in experimentos:
            archivo.write(f"Nombre: {exp['nombre']}\n")
            archivo.write(f"Fecha: {exp['fecha']}\n")
            archivo.write(f"Tipo: {exp['tipo']}\n")
            archivo.write(f"Resultados: {exp['resultados']}\n")
            archivo.write("-" * 40 + "\n")
        archivo.write("Fin del informe.\n")
    print(f"Informe guardado en {nombre_archivo}")


# Menú principal
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar Experimento")
        print("2. Ver Experimentos")
        print("3. Calcular Estadísticas")
        print("4. Comparar Experimentos")
        print("5. Generar Informe")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_experimento()
        elif opcion == "2":
            ver_experimentos()
        elif opcion == "3":
            estadisticas()
        elif opcion == "4":
            comparar_experimentos()
        elif opcion == "5":
            generar_informe()
        elif opcion == "6":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Inicio del programa
menu()
