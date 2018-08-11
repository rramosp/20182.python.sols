## Ejercicio del estudiante

def cadena(s):
    
    char=[i for i in str(s)]
    resultado=[False]
    vocal=['a','e','i','o','u']
    
    if(len(s)%2==0):
        medio=len(s)//2
    else:
        medio=len(s)//2+1
    
    cont_vocales=0
    aux=1
    inverso=''
    for i in s:
        #vocales
        for j in vocal:
            if(i==j):
                cont_vocales+=1
        if (medio==aux):
            for j in vocal:
                if(i==j):
                     resultado[0]=True
        inverso=i+inverso
        aux+=1
    resultado+=[cont_vocales,len(s)-cont_vocales,inverso]
    return resultado
    