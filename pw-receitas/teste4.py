print('Cheguei atrasado professor posso entrar?')
faltas= int(input('Quantas faltas você possui? '))
if faltas==1 or faltas==2:
    print('Pode entrar!')
elif faltas>=3:
    print('Você não pode entrar, e esta suspenso!')
