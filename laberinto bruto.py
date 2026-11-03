matriz = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
N = len(matriz)
def fuerza_bruta(f0, c0):
    if matriz[f0][c0] == 1:
        return 0
    bajadas = (N - 1) - f0              
    pasos = bajadas + (N - 1) - c0     
    total = 0
    for mask in range(2 ** pasos):
        if bin(mask).count("1") != bajadas:
            continue
        f, c = f0, c0
        libre = True
        for k in range(pasos):
            if mask >> k & 1:
                f += 1
            else:
                c += 1

            if matriz[f][c] == 1:
                libre = False
                break

        if libre:
            total += 1

    return total
print("LABERINTO:")
for fila in matriz:
    print(fila)
a = fuerza_bruta(1, 0)  
b = fuerza_bruta(0, 1)      
print("\nCaminos desde A:", a)
print("Caminos desde B:", b)
print("Suma A + B:", a + b)
print("\nCantidad de caminos posibles:", fuerza_bruta(0, 0))