#Escreva uma função que receba um número inteiro não negativo n uma string s como parâmetros e retorne uma string que se repita exatamente n vezes.

def repeat_str(repeat, string):
    return repeat * string 

print(repeat_str(6, "I"))
print(repeat_str(5, "Hello"))
print(repeat_str(1,"Natanael"))