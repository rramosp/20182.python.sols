## Ejercicio del estudiante

def palindromo(n):
    
    digitos = [int(i) for i in str(n)]
    
    for i in xrange(len(digitos)):
        if(digitos[i]!=digitos[-(i+1)]):
            return False
    return True

