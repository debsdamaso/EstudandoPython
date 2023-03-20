# Decisão composto: Se Então Senão (if else)
'''
if <condição>:
    <bloco verdadeiro>
else:
    <bloco falso>
'''

# Exemplo: Dada uma idade, verificar se é maior de idade ou não
'''
idade = int(input("Digite a idade: "))
if idade >= 18:
    print("Maior de idade!")
else:
    print("Menor de idade!")
'''

# Complemento: O que falta ou o contrário.
'''
tanque = 50l
tem 20l
complemento 30

>   <=
>=  <
==  !=
!=  ==
<   >=
<=  >
'''

# Correção do desconto e cupom
'''
venda = float(input("Digite a venda: "))
cupom = input("Tem cupom? [s]im ou [n]ão?")

if venda > 500:
    venda = venda * 0.88
else:
    venda = venda * 0.94

if cupom == "s" or cupom == "S":
    venda = venda - 50

print(f"Valor da venda R$ {venda:.2f}")
'''

# Sintaxes: do If encadeado
'''
# Raiz
if condicao1:
    bloco 1
else:
    if condicao2:
        bloco 2
    else:
        if condicao3:
            bloco 3
        else:
            bloco falso

# Utilizando o elif
if condicao1:
    bloco1
elif condicao2:
    bloco2
elif condicao3:
    bloco3
else:
    bloco falso
'''

# Correção do numero positivo, negativo ou nulo
# Forma Raiz
# num = float(input("Digite um numero: "))
# if num > 0:
#     print("Positivo!")
# else:
#     if num < 0:
#         print("Negativo!")
#     else:
#         print("Nulo!")

# Forma Raiz
num = float(input("Digite um numero: "))
if num > 0:
    print("Positivo!")
elif num < 0:
    print("Negativo!")
else:
    print("Nulo!")