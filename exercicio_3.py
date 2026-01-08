nota1 = float(input("Por favor, digite a primeira nota: "))
nota2 = float(input("Por favor, digite a segunda nota: "))

media = (nota1 + nota2)/ 2
media_round = round(media, 1)

print(f"A média das notas é: {media_round}")