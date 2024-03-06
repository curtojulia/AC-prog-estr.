'''
Atividade complementar 1
Programação Estruturada 
Júlia Dominguez Curto 
Exercício 1
'''

a = int(input("Informe coeficiete a: "))
b = int(input("Informe coeficiete b: "))
c = int(input("Informe coeficiete c: "))

r1 = (-b + ((b**2 - 4*a*c)**0.5)) / (2 * a)
r2 = (-b - ((b**2 - 4*a*c)**0.5)) / (2 * a)

print("A primeira raiz é:", r1)
print("A segunda raiz é:", r2)
