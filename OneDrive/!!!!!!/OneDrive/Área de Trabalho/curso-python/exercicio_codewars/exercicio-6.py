# Dado um conjunto de números, retorne o inverso aditivo de cada um. Cada número positivo se torna negativo e os negativos se tornam positivos.

def invert(list):
    invert_list = []

    for item in list:
        inverted_item = item * -1
        invert_list.append(inverted_item)

    return invert_list

input_list = [1, 2, 3, 4, 5]
print(invert(input_list))

input_list = [1, -2, 3, -4, 5]
print(invert(input_list))