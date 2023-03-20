# calculando o inss - forma 1 - elif

sal = float(input("Salário: "))

if sal >= 0 and sal <= 1302:
    inss = sal * 0.075

if sal > 1302 and sal <= 2572.29:
    inss = sal * 0.09

if sal > 2572.29 and sal <= 3856.94:
    inss = sal * 0.12

if sal > 3856.94 and sal <= 7507.49:
    inss = sal * 0.14

#else: #errado
    #inss = 1051.05
    #ta errado pq vai dar esse valor pra quase tudo, até pra um salario de 1000


#corrigir e terminar aí embaixo depois

elif sal <= 3856.94:
    inss = sal * 0.12

