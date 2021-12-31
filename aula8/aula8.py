"""
*Criar variaveis para nome (str), idade (int),
*altura (float) e peso ano atual (int)
*obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
*obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
*obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
*exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = "Matheus"
idade = 20
altura = 1.80
peso = 80
ano_atual = 2021
ano_de_nascimento = ano_atual - idade
imc = (peso/(altura**2))

print(f'O {nome} tem {idade} anos com {altura:.2f} de altura, {peso}Kg com a data de nascimento em {ano_de_nascimento} com o seu IMC igual a {imc:.2f}')

"""
nome = 'Luiz'
idade = 32
altura = 1.80
peso = 80.5
ano_atual = 2019
nascimento = ano_atual - idade
imc = peso / altuera ** 2

print(f'O {nome} tem {idade} anos e {altura} altura.')
print(f'O {nome} peso {peso} e seu imc {imc:.2f}.')
print(f'O {nome} nasceu em {nascimento}.')
"""
