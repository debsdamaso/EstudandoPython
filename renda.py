# calculando o Salario Liquido - forma 1 - elif

# parte 1: IR
# parte 2: INSS
# parte 3: Salario - IR - INSS

    # EXERCICIO 1  = IR
sal = float(input("Salário: "))

#parte 1: ver imposto de renda
if sal >= 0 and sal <= 1903.98:
    IR = 0

if sal > 1903.99 and sal <= 2826.65:
    IR = sal * 0.075 - 142.80

if sal > 2826.66 and sal <= 3751.05:
    IR = sal * 0.15 - 354.80

if sal > 3751.06 and sal <= 4664.68:
    IR = sal * 0.225 - 636.13

if sal > 4664.68:
    IR = sal * 0.275 - 869.36

# exercicio 2: INSS + IR
#parte 2 : ver inss
if sal >= 0 and sal <= 1302:
    inss = sal * 0.075

if sal > 1302 and sal <= 2572.29:
    inss = sal * 0.09

if sal > 2572.29 and sal <= 3856.94:
    inss = sal * 0.12

if sal > 3856.94 and sal <= 7507.49:
    inss = sal * 0.14

#parte 3 : somar inss e ir
SalLiq = sal - inss - IR

#parte 4: mostrar salario liquido
#imprima SalLiq
print ("O salário líquido é: ", SalLiq)