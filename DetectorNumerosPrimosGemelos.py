def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
