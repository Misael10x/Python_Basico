import functools


factorial = [5,4,3,2,1]
resultado = functools.reduce (lambda x,y: x*y, factorial)
print(resultado)
