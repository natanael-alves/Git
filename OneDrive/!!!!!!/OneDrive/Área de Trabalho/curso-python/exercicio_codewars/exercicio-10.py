def difference_in_ages(lista_idade):
    maior = lista_idade[0]
    menor = lista_idade[0]

    for item in lista_idade:
        if item < menor:
            menor = item

        if item > maior:
            maior = item

    
    diferenca = maior - menor
    tupla_resultado = (menor, maior, diferenca)

    return tupla_resultado

lista_entrada = [57, 81, 14, 7, 32, 99]
print(difference_in_ages(lista_entrada))