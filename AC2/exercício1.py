'''
Atividade complementar 1
Programação Estruturada 
Júlia Dominguez Curto 
Exercício 1
'''

def eq_seg_grau(a, b, c):
    r1 = (-b + ((b**2 - 4*a*c)**0.5)) / (2 * a)
    r2 = (-b - ((b**2 - 4*a*c)**0.5)) / (2 * a)
    return r1 , r2 


print("-" * 30)

def bissexto(ano):
    bis = ano % 4 == 0 and not ano % 100 == 0 or ano % 400 == 0
    return bis

print("-" * 30)


def calcula_salario(num_horas, valor_hora, irpf = 0.275):
    salario = (num_horas * valor_hora) 
    salario_liquido  = salario -  salario * irpf
    return salario_liquido



def main():
    print(eq_seg_grau(2, 16, 3))
    print(bissexto(2024))
    print(bissexto(1995))
    print(bissexto(2012))
    print(bissexto(1900))
    print(calcula_salario(100,100))
    
main()
