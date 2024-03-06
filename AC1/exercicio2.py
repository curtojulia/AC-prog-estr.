'''
Atividade complementar 1
Programação Estruturada 
Júlia Dominguez Curto 
Exercício 2
'''
ano = int(input("Informe um ano: "))
print(ano % 4 == 0 and not ano % 100 == 0 or ano % 400 == 0)