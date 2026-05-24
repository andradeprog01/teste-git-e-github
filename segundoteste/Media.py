notaA = float(input("Entre com a primeira nota: "))
notaB = float(input("Entre com a segunda nota: "))

media = (notaA + notaB)/2


if media >= 7.0 :
    print("Média: %.1f "% media, "Aluno aprovado")
elif media < 7 and media > 5 :
    print("Média: %.1f " % media, "Solicitar revisao")
else:
    print("Média: %.1f " % media, "Aluno reprovado")
