import random
a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terceiro Aluno: '))
lista = [a1, a2, a3]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')