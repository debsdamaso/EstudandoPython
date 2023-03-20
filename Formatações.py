# FORMATAÇÕES DO PRINT
nome = "Edson"
idade = 48
salario = 34537.94745345
# Forma 1 - Separando com vírgulas
print(nome, idade, salario)
# Forma 2
print("Nome: ", nome, "Idade: ", idade, "Salario:", salario)
# Forma 3
print("Nome: ", nome, "\nIdade: ", idade, "\nSalario:", salario) # O \n força a mudança de linha
# Forma 4 - Utilizando o format()
print("Nome: {} Idade: {} Salario: {}".format(nome, idade, salario))
# Forma 5                                        ÍNDICES         0      1      2
print("Nome: {0} Idade: {1} Salario: {2} - Obrigado {0}".format(nome, idade, salario))
# Forma 6
print("Nome: {n} Idade: {i} Salario: {s} ".format(n = nome, i = idade, s = salario))
# Forma 7 - utilizando o print'f'
print(f"Nome: {nome} Idade: {idade} Salario: {salario}")
# Forma 8 - utilizando o print'f'
idade  = 8
print(f"Nome.......: {nome} \nIdade......: {idade:05d} \nSalario....: {salario:.2f}")
valor1 = 45.93838
valor2 = 234.1
valor3 = 234244.0
valor4 = 2
print("Extrato:")
print(f"Valor 1: R$ {valor1:10.2f}")
print(f"Valor 2: R$ {valor2:10.2f}")
print(f"Valor 3: R$ {valor3:10.2f}")
print(f"Valor 4: R$ {valor4:10.2f}")
print(f"""
    Extrato:
    R$ {valor1:10.2f}
    R$ {valor2:10.2f}
    R$ {valor3:10.2f}
    R$ {valor4:10.2f}
""")



# CASTING - Modificação do tipo da variável
"""
TIPO        PYTHON
Inteiro:    int()
Real:       float()
Texto:      str()
Lógico:     bool()
"""

# Exemplo utilizando casting
'''
# valor = input("Digite o valor: ") # O input lê somente dados texto (str)
# valor = float(valor) # Casting

valor = float(input("Digite o valor: "))


resp = valor + valor # o sinal de + soma ou concatena valores
print("Dobro: " + str(resp))

print(valor, type(valor))
'''
