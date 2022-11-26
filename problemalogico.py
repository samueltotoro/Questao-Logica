from time import sleep
print('\n')
print('''Sabendo que X = 8 e Y = 9, analize a seguinte situação lógica e responda:

            
            Se ((Y + (330.6 / 6)) == (X ** 2)):
                    Z = X % 2
                senao:
                    Nao( X != 10) E ( Y > 9 ):
                        Z = Y // 4
        

A) Z = 0
B) Z = 2
C) Z = 2.25
D) Z = 4
E) Nenhuma das alternativas anteriores.
''')

res = str(input("Qual das alternativas, possui o valor correto de Z? ")).upper()

for c in range(4, 0, -1):
    print('Carregando[{}]'.format(c))
    sleep(2)

if res == 'E':
    print('\n')
    print('=' * 10, " PARABÉNS, VOCÊ ACERTOU! ", '=' * 10)

else:
    print('\n')
    print('*' * 10, ' SINTO MUITO, VOCÊ ERROU! ', '*' * 10)

