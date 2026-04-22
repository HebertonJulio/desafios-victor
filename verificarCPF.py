def validaCPF(cpf):
    while True:
    # primeiro digito
        # cpf = input("Informe seu CPF: ")
        # valida quantidade de digitos
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            print("CPF Inválido, Caracteres ou Tudo Igual.")
            cpf = input("Informe seu CPF: ")
        else:
            print("Seu CPF tem 11 digitos")
            break
    
    contador = 10
    somaDigito1 = 0

    for digito in cpf[:9]:
        somaDigito1 = somaDigito1 + int(digito) * contador 
        contador = contador - 1

    resto = somaDigito1 % 11
    resultadoDigitoUm = 11 - resto
    if resultadoDigitoUm >= 10:
        resultadoDigitoUm = 0


     # segundo digito
    somaDigito2 = 0
    contador = 11
    for digito in cpf [:9]:
        somaDigito2 = somaDigito2 + int(digito) * contador
        contador = contador - 1
    somaDigito2 = somaDigito2 + resultadoDigitoUm * 2   ## aqui para adicionar o penultimo digito na conta

    restoDigito2 = somaDigito2 % 11 
    resultadoDigito2 = 11 - restoDigito2
    if resultadoDigito2 >= 10:
        resultadoDigito2 = 0
            
    if int(cpf[9]) == resultadoDigitoUm and int(cpf[10]) == resultadoDigito2: 
        print("CPF válido.")
    else: 
        print("CPF inválido.")
      

cpf = input("Informe seu CPF: ")
validaCPF(cpf)


























