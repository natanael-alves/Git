# Considere um array/lista de ovelhas onde algumas ovelhas podem estar faltando em seus lugares. 
# Precisamos de uma função que conte o número de ovelhas presentes no array (verdadeiro significa presente).

def count_sheeps(sheep):
    count = 0
    for item in sheep:
        if item == True:
            count += 1
    return count

input_list = [
        False,  False,  True,  False,
        True,  False,  False,  False ,
        False,  False, False,  False,
        False,  False, False, False ,
        False,  False,  False,  False ,
        False, False, False,  False
        ]

print(count_sheeps(input_list))