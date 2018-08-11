## Ejercicio del estudiante

def cambio(n):
    change=[0,0,0]
    if (n<1 or n>99):
        return None
    else:
        change[2]=n//25
        n-=change[2]*25
        change[1]=n//10
        change[0]=n%10
        return change

     
    