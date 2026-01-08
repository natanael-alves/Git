# Dado um vetor de números inteiros, sua solução deve encontrar o menor número inteiro.
#Por exemplo:
#Dada [34, 15, 88, 2]a sua solução, retornará 2
#Dada [34, -345, -1, 100] a sua solução, retornará -345
#Para efeitos deste kata, pode assumir que o array fornecido não estará vazio.

def find_smallest_int(lista):
    menor = lista[0]

    for item in lista:
        if item < menor :
            menor = item
    
    return menor

lista_entrada = [34, 15, 88, 2 , 10]
print(find_smallest_int(lista_entrada))

lista_entrada = [34, -345, -1, 100]
print(find_smallest_int(lista_entrada))
