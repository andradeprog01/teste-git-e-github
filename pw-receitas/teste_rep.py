senhas=['abc','1234567','felipe13','theto','brab1234']
for senha in senhas:
    if len(senha)<6:
        print(senha,'é invalida!')
    elif len(senha)>=6:
        print(senha,'é valida!')