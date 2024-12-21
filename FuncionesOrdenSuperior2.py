def divisor(x):
    def dividiendo(y):
       return y / x
    return dividiendo
    
divide = divisor(2)
print(divide(10))
