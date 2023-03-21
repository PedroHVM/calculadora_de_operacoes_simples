while True:
    numero1 = input('Digite o primeiro número: ')
    numero2 = input('Digite o segundo número: ')
    
    numeros_validos = None

    try:
        num_1_float = float(numero1)    
        num_2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números inseridos são inválidos.')
        continue
    operador = input('Qual operação deseja realizar? (+-*/) ')
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        print(f'{numero1} + {numero2} = ',num_1_float + num_2_float)
    elif operador == '-':
        print(f'{numero1} - {numero2} = ',num_1_float - num_2_float)
    elif operador == '/':
        print(f'{numero1} / {numero2} = ',num_1_float / num_2_float)
    elif operador == '*':
        print(f'{numero1} * {numero2} = ',num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break