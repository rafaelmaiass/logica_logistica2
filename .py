#################################################################
print('Bem vindo a Companhia de Logistica Rafael Maia de Assis.')
#################################################################
def dimensoesObjeto():
    while True:        
        try:
            altura = int(input('Digite a altura (cm) do objeto: '))
            comprimento = int(input('Digite o comprimento (cm) do objeto: '))
            largura = int(input('Digite a largura (cm) do objeto: '))

            volume = altura * largura * comprimento

            print(f'O volume do objeto é: {volume}')

            if volume < 1000:
                return 10
            
            elif 1000 <= volume < 10000:
                return 20
            
            elif 10000 <= volume < 30000:
                return 30
                
            elif 30000 <= volume < 100000:
                return 50
                
            else:
                print('Não aceitamos objetos com dimensões tão grandes')
                print('Entre com as dimensões desejadas novamente.')
                continue

        except ValueError:
            print('Você digitou alguma dimensão não númerica')
            print('Por favor entre com as dimensões desejadas novamente.')
            continue
def pesoObjeto():
    while True:
        try:
            qual_peso = int(float(input('Digite o peso do objeto: ')))
            if qual_peso <= 0.1:
                return 1
                
            elif 0.1 <= qual_peso < 1:
                return 1.5
                
            elif 1 <= qual_peso < 10:
                return 2
                
            elif 10 <= qual_peso < 30:
                return 3
                
            else:
                print('Não aceitamos esse peso, tente novamente.')
                continue
        
        except ValueError:
            print('Você digitou algum peso do objeto com valor não númerico')
            print('Por favor entre com o peso desejado novamente.')
def rotaObjeto():
    while True:
        qual_rota = input(
            'Selecione a rota:\n'
            ' BR - De Belo Horizonte para Rio de Janeiro\n'
            ' BS - De Belo Horizonte para São Paulo\n'
            ' RB - Do Rio de Janeiro para Belo Horizonte\n'
            ' RS - Do Rio de Janeiro para São Paulo\n'
            ' SR - De São Paulo para Rio de janeiro\n'
            ' SB - De São Paulo para Belo Horizonte\n'
            '>> '
            ).lower()
                
        if qual_rota == 'rs':
            return 1
              
        elif qual_rota == 'sr':
            return 1
             
        elif qual_rota == 'bs':
            return 1.2
            
        elif qual_rota == 'sb':
            return 1.2
            
        elif qual_rota == 'br':
            return 1.5
              
        elif qual_rota == 'rb':
            return 1.5
            
        else:
            print(
                'Você digitou uma rota que não existe\n'
                'Por favor entre com a rota desejada novamente'
            )
            continue
#################################################################
total = dimensoesObjeto() * pesoObjeto() * rotaObjeto()
print(f'Total a pagar(R$): {total}')
