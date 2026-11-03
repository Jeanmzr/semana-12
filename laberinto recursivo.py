lab = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

n = len(lab)
fin = (n - 1, n - 1)   
def rutas_rec(f, c):
    if f >= n or c >= n or lab[f][c] == 1:        
        return 0
    if (f, c) == fin:                           
        return 1
    return rutas_rec(f + 1, c) + rutas_rec(f, c + 1)  

a = rutas_rec(1, 0)   
b = rutas_rec(0, 1)    
print("Caminos desde A:", a)
print("Caminos desde B:", b)
print("Suma A + B:", a + b)
print("Caminos desde el inicio:", rutas_rec(0, 0))