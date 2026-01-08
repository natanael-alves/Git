#Crie uma função que receba um número inteiro como argumento e retorne verdadeiro "Even"para números pares ou "Odd"falso para números ímpares.

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    
    return "Odd"

print(even_or_odd(10))
print(even_or_odd(5))
print(even_or_odd(0))
print(even_or_odd(-4))