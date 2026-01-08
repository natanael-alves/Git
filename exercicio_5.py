idade = int(input("Informe sua idade: "))

if idade >= 18 and idade <=60 :
    print("Parabéns, você já pode tirar sua CNH")
    print("Dirija com cuidado ! ")
elif idade < 18:
    print("Poxa, que pena. Você ainda não pode tirar sua CNH.") 
else:
    print("Você não pode mais tirar a CNH.")