def automata(palabra):
    estado_actual = 'e0'
    estados_aceptacion = {'e4'}  # según tu cuaderno
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
            return False  # transición no definida → rechazo

    return estado_actual in estados_aceptacion


# Lectura desde teclado
palabra = input("Introduce la palabra (solo 0 y 1): ")
if automata(palabra):
    print(" Palabra aceptada")
else:
    print(" Palabra rechazada")

