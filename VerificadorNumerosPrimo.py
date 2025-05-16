num = int(input("Ingresa un número: "))

if num <= 1:
    print("No es primo")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
