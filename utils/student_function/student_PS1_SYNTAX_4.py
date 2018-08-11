## Ejercicio del estudiante


def fibonacci(n):
    f_1=1
    f_2=1
    suma=0
    if(n<3):
        return 1
    for i in xrange(3,n+1):
        suma=f_1+f_2
        f_1=f_2
        f_2=suma
    
    return suma
