def automata(palabra):
    estado_actual = 'e0'
    estados_aceptacion = {'e4'}  # Estado final de aceptación
    delta = {
        ('e0', '0'): 'e1',
        ('e1', '1'): 'e2',
        ('e2', '1'): 'e3',
        ('e3', '0'): 'e4',
        ('e3', '1'): 'e2',
        ('e4', '0'): 'e4'
    }
    for simbolo in palabra:
        if (estado_actual, simbolo) in delta:
            estado_actual = delta[(estado_actual, simbolo)]
            
        else:
            return False

    return estado_actual in estados_aceptacion


# Bucle principal
while True:
    palabra = input("Introduce la palabra (0 y 1) o escribe 'salir': ").strip()
    if palabra.lower() == "salir":
        print("Programa finalizado.")
        break

    if automata(palabra):
        print("Palabra aceptada")
    else:
        print("Palabra rechazada")
