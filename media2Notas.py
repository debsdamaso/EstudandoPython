'''
PRIMEIRO SEMESTRE (SEM1)

CP1 * 1 = 10
CP2 * 1 = 10
CP3 X

SP1 * 1 = 10
SP2 * 1 = 10

GS * 6 = 10

MEDIA SEMESTRAL = CP * 2 + SP * 2 + GS * 6
                     2   +   2    +  6

SEGUNDO SEMESTRE (SEM2)

CP1 * 1 = 10
CP2 * 1 = 10
CP3 X

SP1 * 1 = 10
SP2 * 1 = 10

GS * 6 = 10

MEDIA SEMESTRAL = CP * 2 + SP * 2 + GS * 6
                     2   +   2    +  6

--------------------
MEDIA FINAL = SEM1 * 4 + SEM2 * 6
               10 * 4 + 10 * 60
               4      +  6
               10
'''

# V1. Dadas duas notas pelo usuário, calcular a media e verificar se ele está
#     Aprovado (media de ao menos 6)
'''
n1 = float(input("Digite a Nota 1: "))
n2 = float(input("Digite a Nota 2: "))

med = (n1 + n2) / 2

if med >= 6:
    print(f"Aprovado com media {med}")
else:
    print(f"Reprovado com media {med}")
'''
# v2. Considerando o enunciado anterior, verificar se as notas são válidas ou não.
'''
ENTRADA - Nota 1: 7   Nota 2: 8       SAÍDA: Aprovado com média 7.5
ENTRADA - Nota 1: 2   Nota 2: 4       SAÍDA: Reprovado com média 3
ENTRADA - Nota 1: 3   Nota 2: 15      SAÍDA: A segunda nota é invalida
ENTRADA - Nota 1: -4                  SAÍDA: A primeira nota é invalida
'''
'''
n1 = float(input("Digite a Nota 1: "))
if n1 >= 0 and n1 <= 10:
    # nota1 valida
    n2 = float(input("Digite a Nota 2: "))
    if n2 >= 0 and n2 <= 10:
        # nota2 válida
        med = (n1 + n2) / 2
        if med >= 6:
            print(f"Aprovado com média {med}")
        else:
            print(f"Reprovado com média {med}")
    else:
        print(f"A nota 2 '{n2}' é inválida")
else:
    print(f"A nota 1 '{n1}' é inválida")

print("Obrigado por utilizar o nosso programa")
'''
# Consistência de dados - verificar se os dados são validos

# v3. Considerando o enunciado anterior, caso o aluno não seja aprovado, verificar
# se ele tem a possibilidade de fazer exame (entre 4 e 5.9 se estiver abaixo de 4
# o aluno está reprovado direto); se sim, solicitar a
# nota de exame (consistir) e calcular a media final considerando a media com a nota
# de exame e verificar se ele passou por exame (media de ao menos 6).
'''
ENTRADA - Nota 1: 7   Nota 2: 8       SAÍDA: Aprovado direto com média 7.5
ENTRADA - Nota 1: 2   Nota 2: 4       SAÍDA: Reprovado direto com média 3
ENTRADA - Nota 1: 5   Nota 2: 6  "Exame"  EXAME: 4.5      SAÍDA: Reprovado em exame com media 5
ENTRADA - Nota 1: 4   Nota 2: 5  "Exame"  EXAME: 10       SAÍDA: Aprovado em exame com media 7.25
ENTRADA - Nota 1: 4   Nota 2: 5  "Exame"  EXAME: 34       SAÍDA: Nota de exame inválida
'''
n1 = float(input("Digite a Nota 1: "))
if n1 >= 0 and n1 <= 10:
    # nota1 valida
    n2 = float(input("Digite a Nota 2: "))
    if n2 >= 0 and n2 <= 10:
        # nota2 válida
        med = (n1 + n2) / 2
        if med >= 6:
            print(f"Aprovado com média {med}")
        else:
            if med >= 4:
                # Exame
                ex = float(input("Digite a Nota do Exame: "))
                if ex >= 0 and ex <= 10:
                    media_final = (med + ex) / 2
                    if media_final >= 6:
                        print(f"Aprovado em exame com media {media_final}")
                    else:
                        print(f"Reprovado em exame com media {media_final}")
                else:
                    print("Nota de Exame inválida")

            else:
                print(f"Reprovado direto com média {med}")
    else:
        print(f"A nota 2 '{n2}' é inválida")
else:
    print(f"A nota 1 '{n1}' é inválida")

print("Obrigado por utilizar o nosso programa")