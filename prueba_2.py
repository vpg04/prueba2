def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar alumno")
    print("2. Mostrar todos los alumnos")
    print("3. Cerrar")

def agregar_alumno(lista_alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    lista_alumnos.append(nombre)
    print(f"Alumno {nombre} agregado.")

def mostrar_alumnos(lista_alumnos):
    if len(lista_alumnos) > 0:
        print("\n--- Lista de Alumnos ---")
        for alumno in lista_alumnos:
            print(alumno)
    else:
        print("No hay alumnos registrados.")

def main():
    lista_alumnos = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1/2/3): ")
        
        if opcion == '1':
            agregar_alumno(lista_alumnos)
        elif opcion == '2':
            mostrar_alumnos(lista_alumnos)
        elif opcion == '3':
            print("Cerrando el programa...")
            break
        else:
            print("Opción no válida, por favor elija una opción válida.")
    
if __name__ == "__main__":
    main()
