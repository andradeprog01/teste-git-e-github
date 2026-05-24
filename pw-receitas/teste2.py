salario_mensal=input("Entre com o salario mensal do funcionario:")
horas_trabalhadas=input("Entre com o numero de horas trabalhadas no mes:")
valor_hora= float(salario_mensal)/int(horas_trabalhadas)
print("O  valor da hora trabalhada é de: ",valor_hora)
if valor_hora<100:
    print('Você é pobre!')
else:
    print('Você é rico!')