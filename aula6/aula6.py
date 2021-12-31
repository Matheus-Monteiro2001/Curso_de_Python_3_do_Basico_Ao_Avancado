'''
Iniciar com letra, pode conter numeros, separar _, letras minusculas
'''

nome = 'Matheus'
idade = 20 #int
altura = 1.90 #float
e_maior = idade > 18 #bool
peso = 90
imc = peso/(altura**2)

#data_1 = True #bool
#data_atual = 2019 #int

print("Nome: ",nome)
print("Idade: ",idade)
print("Altura: ",altura)
print("E maior: ",e_maior)

#print(nome, type(nome))

print(idade * altura)

print( nome, 'tem', idade, 'de idade e seu imc e', imc)