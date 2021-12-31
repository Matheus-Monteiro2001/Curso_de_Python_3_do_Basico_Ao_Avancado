nome = 'Matheus'
idade = 20 #int
altura = 1.90 #float
e_maior = idade > 18 #bool
peso = 90
imc = peso/(altura**2)

print( nome, 'tem', idade, 'de anos de idade e seu imc e', imc)
print(f'{nome} tem {idade} de anos de idade e seu imc e {imc:.2f}')
print('{} tem {} de anos de idade e seu imc e {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} de anos de idade e seu imc e {2} {1} {2}'.format(nome, idade, imc))
print('{n} tem {i} de anos de idade e seu imc e {im}'.format(n = nome, i = idade, im = imc))
