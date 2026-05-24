def lerNotas():
    n = float(input("Entre com a nota do aluno (a): "))
    return n

def resultado(n1,n2):
    media = (n1+n2)/2
    print("Nota 01: ", n1)
    print("Nota 02: ", n2)
    print("A média é ", media, "Resultado: ", end="")
    if media>=7.0:
        print("Aprovado")
    else:
        print("Reprovado")

a= lerNotas()
b= lerNotas()
resultado(a,b)




