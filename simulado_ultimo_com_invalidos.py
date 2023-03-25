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
if CP1 < 0 or CP1 > 10 :
    print("A ultima nota é inválida")
else :
    CP2 = float(input("Digite a nota do segundo checkpoint: "))
    if CP2 < 0 or CP2 > 10 :
        print("A ultima nota é inválida")
    else:
        CP3 = float(input("Digite a nota do terceiro checkpoint: "))
        if CP3 < 0 or CP3 > 10 :
            print("A ultima nota é inválida")
        else :
            menor_CP = min(CP1, CP2, CP3)
            med_CP = (CP1 + CP2 + CP3 - menor_CP) / 2
# vai ter 20% de peso

#segunda parte, sprint/challenge:
            SP1 = float(input("Digite a nota do primeiro sprint: "))
            if SP1 < 0 or SP1 > 10 :
                print("A ultima nota é inválida")
            else :
                SP2 = float(input("Digite a nota do segundo sprint: "))
                if SP2 < 0 or SP2 > 10 :
                    print("A ultima nota é inválida")
                else :
                    med_SP1 = (SP1 + SP2) / 2
#vai ter 20% de peso

#terceira parte, global solution
                    GS = float(input("Digite a nota do Global Solution: "))
                    if GS < 0 or GS > 10:
                        print("A nota do Global está inválida")
                    else:
#vai ter 60% de peso

#quarta parte, média do primeiro semestre:
#MEDIA SEMESTRAL = CPs * 2 + SPs * 2 + GS * 6

                        med_SEM1 = med_CP * 0.20 + med_SP1 * 0.20 + GS * 0.60
                        print(f"A MÉDIA DO PRIMEIRO SEMESTRE É (40%): {med_SEM1}")

#MEDIA SEGUNDO SEMESTRE
#primeira parte: checkpoint, excluir a menor nota e fazer média/2
                        print("Agora digite as notas do SEGUNDO SEMESTRE abaixo ")
                        CP4 = float(input("Digite a nota do primeiro checkpoint: "))
                        if CP4 < 0 or CP4 > 10 :
                            print("A ultima nota é inválida")
                        else :
                            CP5 = float(input("Digite a nota do segundo checkpoint: "))
                            if CP5 < 0 or CP5 > 10 :
                                print("A ultima nota é inválida")
                            else:
                                CP6 = float(input("Digite a nota do terceiro checkpoint: "))
                                if CP6 < 0 or CP6 > 10 :
                                    print("A ultima nota é inválida")
                                else :
                                    menor_CP2 = min(CP4, CP5, CP6)
                                    med_CP2 = (CP4 + CP5 + CP6 - menor_CP2) / 2
# vai ter 20% de peso

#segunda parte, sprint/challenge:
                                    SP3 = float(input("Digite a nota do primeiro sprint: "))
                                    if SP3 < 0 or SP3 > 10 :
                                        print("A ultima nota está inválida")
                                    else:
                                        SP4 = float(input("Digite a nota do segundo sprint: "))
                                        if SP4 < 0 or SP4 > 10:
                                            print("A ultima nota está inválida")
                                        else:
                                            med_SP2 = (SP3 + SP4) / 2
#vai ter 20% de peso

#terceira parte, global solution
                                        GS2 = float(input("Digite a nota do Global Solution: "))
                                        if GS2 < 0 or GS2 > 10:
                                            print("Nota do Global está inválida")
#vai ter 60% de peso
                                        else:
#quarta parte, média do segundo semestre:
#MEDIA SEMESTRAL = CPs * 2 + SPs * 2 + GS * 6
#ADICIONAR MEDIA FINAL

                                            med_SEM2 = med_CP2 * 0.20 + med_SP2 * 0.20 + GS2 * 0.60
                                            print(f"A MÉDIA DO SEGUNDO SEMESTRE É (60%): {med_SEM2}")
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