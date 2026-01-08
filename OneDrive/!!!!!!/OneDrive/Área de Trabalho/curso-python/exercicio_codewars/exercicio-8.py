#O primeiro século abrange o período do ano 1 até o ano 100, inclusive ; o segundo século, do ano 101 até o ano 200, inclusive ; e assim por diante.
#Tarefa
#Dado um ano, retorne o século em que ele se encontra.

def century(ano):
    parte_inteira = ano // 100
    parte_decimal = ano % 100

    if parte_decimal > 0:
        parte_inteira += 1
    
    return parte_inteira

print(century(2025))
print(century(1601))
print(century(1900))