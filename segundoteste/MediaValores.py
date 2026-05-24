qtde = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while valor > 0.0 :
    soma = soma + valor
    qtde = qtde +1
    valor = float(input("Digite um valor: "))

media = soma/qtde
print("A media dos valores é: %.2f"%media)







