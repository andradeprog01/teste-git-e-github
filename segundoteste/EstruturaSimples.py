A = input("Informe um valor para a variavel A: ")
B = input("Informe um valor para a variavel B: ")

if A>B:
    aux = A
    A = B
    B = aux
    print("O valor de A agora é:  ", A)
    print("O valor de B agora é:  ", B)
else:
    print("O valor de A permanece o mesmo: ", A)
    print("O valor de B permanece o mesmo: ", B)