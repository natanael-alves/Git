# Nesta tarefa simples, você recebe um número e precisa torná-lo negativo. Mas talvez o número já seja negativo?

def make_negative( number ):
    if number > 0:
        return number * -1
    
    return number

print(make_negative(1))
print(make_negative(-5))
print(make_negative(0))
print(make_negative(100))
print(make_negative(-100))