''' FAZER UM PROGRAMA QUE CALCULE O PROCESSO RELACIONADO A NOTAS DE UM ALUNO
DA FIAP.

PRIMEIRO SEMESTRE (SEM1) -----------------------
CHECKPOINT: Pegar 3 notas do usuário e excluir a menor para fazer a media simples por dois.
CP1 * 1 = 10
CP2 * 1 = 10
CP3 X
Os CPs tem peso de 20% na média.

SPRINT (CHALLENGE): Pegar duas notas do usuário e Calcular a média simples por 2.
SP1 * 1 = 10
SP2 * 1 = 10
Os SPs tem peso de 20% na média.

GLOBAL SOLUTION: Pegar a nota do usuário. Tem peso de 60%.
GS * 6 = 10

MEDIA SEMESTRAL = CPs * 2 + SPs * 2 + GS * 6
                    2    +   2    +  6

SEGUNDO SEMESTRE (SEM2) -----------------------
CHECKPOINT: Pegar 3 notas do usuário e excluir a menor para fazer a media simples por dois.
CP1 * 1 = 10
CP2 * 1 = 10
CP3 X
Os CPs tem peso de 20% na média.

SPRINT (CHALLENGE): Pegar duas notas do usuário e Calcular a média simples por 2.
SP1 * 1 = 10
SP2 * 1 = 10
Os SPs tem peso de 20% na média.

GLOBAL SOLUTION: Pegar a nota do usuário. Tem peso de 60%.
GS * 6 = 10

MEDIA SEMESTRAL = CPs * 2 + SPs * 2 + GS * 6
                        2    +   2    +  6
-----------------------------------
MEDIA FINAL = SEM1 * 4 + SEM2 * 6
10 * 4 + 10 * 60
4      +  6                10
EXIBIR TODAS AS MÉDIAS - CPs - SPs - SEM1 e SEM2 '''

#primeira parte: checkpoint, excluir a menor nota e fazer média/2
print("Digite as notas do PRIMEIRO SEMESTRE abaixo ")
CP1 = float(input("Digite a nota do primeiro checkpoint: "))
CP2 = float(input("Digite a nota do segundo checkpoint: "))
CP3 = float(input("Digite a nota do segundo checkpoint: "))
menor_CP = min(CP1, CP2, CP3)
med_CP = (CP1 + CP2 + CP3 - menor_CP) / 2
# vai ter 20% de peso

#segunda parte, sprint/challenge:
SP1 = float(input("Digite a nota do primeiro sprint: "))
SP2 = float(input("Digite a nota do segundo sprint: "))
med_SP = (SP1 + SP2) / 2
#vai ter 20% de peso

#terceira parte, global solution
GS = float(input("Digite a nota do Global Solution: "))
#vai ter 60% de peso

#quarta parte, média do primeiro semestre:
#MEDIA SEMESTRAL = CPs * 2 + SPs * 2 + GS * 6

med_SEM1 = med_CP * 0.20 + med_CP * 0.20 + GS * 0.60
print(f"A MÉDIA DO PRIMEIRO SEMESTRE É (40%): {med_SEM1}")

#MEDIA SEGUNDO SEMESTRE
#primeira parte: checkpoint, excluir a menor nota e fazer média/2
print("Agora digite as notas do SEGUNDO SEMESTRE abaixo ")
CP4 = float(input("Digite a nota do primeiro checkpoint: "))
CP5 = float(input("Digite a nota do segundo checkpoint: "))
CP6 = float(input("Digite a nota do segundo checkpoint: "))
menor_CP2 = min(CP4, CP5, CP6)
med_CP2 = (CP4 + CP5 + CP6 - menor_CP) / 2
# vai ter 20% de peso

#segunda parte, sprint/challenge:
SP3 = float(input("Digite a nota do primeiro sprint: "))
SP4 = float(input("Digite a nota do segundo sprint: "))
med_SP2 = (SP3 + SP4) / 2
#vai ter 20% de peso

#terceira parte, global solution
GS2 = float(input("Digite a nota do Global Solution: "))
#vai ter 60% de peso

#quarta parte, média do segundo semestre:
#MEDIA SEMESTRAL = CPs * 2 + SPs * 2 + GS * 6
med_SEM2 = med_CP2 * 0.20 + med_CP2 * 0.20 + GS2 * 0.60
print(f"A MÉDIA DO SEGUNDO SEMESTRE É (60%): {med_SEM2}")

# NOTA FINAL DE TUDO
'''MEDIA FINAL = SEM1 * 4 + SEM2 * 6 
                   10 * 4 + 10 * 60
                     4    +  6    10
EXIBIR TODAS AS MÉDIAS 
- CPs 
- SPs 
- SEM1 e SEM2 '''
med_fim = (med_SEM1 * 0.4 + med_SEM2 * 0.6 )
print(f"A MÉDIA FINAL É: {med_fim}")
if med_fim >= 6 :
    print("Você foi APROVADO")
elif med_fim < 4:
    print("Você foi REPROVADO DIRETO")
elif med_fim >= 4 and med_fim < 6 :
    exam = float(input("Digite o valor do exame: "))
    med_exame = (med_fim + exam) / 2
    if med_exame > 6:
        print(f"APROVADO por exame com média: {med_exame}")
    else :
        print(f"REPROVADO no exame com média: {med_exame}")

print('\nFIM\n')