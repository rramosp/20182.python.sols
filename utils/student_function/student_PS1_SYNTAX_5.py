## Ejercicio del estudiante



def perfecto(n):
    suma = 0
    for i in xrange(1, n):
        if n % i == 0:
            suma += i
    return suma == n
