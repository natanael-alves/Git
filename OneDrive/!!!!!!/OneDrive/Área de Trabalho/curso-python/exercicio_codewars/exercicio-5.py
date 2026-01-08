# Você consegue encontrar a agulha no palheiro?

#Escreva uma função findNeedle()que receba uma arraylista cheia de lixo, mas que contenha um único elemento."needle"

#Após a sua função encontrar a agulha, ela deverá retornar uma mensagem (em formato de texto) que diga:

#"found the needle at position "Além disso, index encontrou a agulha, então:

#Exemplo (Entrada --> Saída)

def find_needle(haystack):
    position = 0

    for element in haystack: 
        if element == "needle":
            break

        position = position + 1

    return f"Found the needle at position {position}"

input_list = ["hay", "junk", "hay", "hay", "moreJunk", "randomJunk", "needle"]
print(find_needle(input_list))

