"""
Atividade Complementar 3
Programação estruturada 
Júlia Dominguez Curto
  """

def determina_tipo_triangulo(l1,l2,l3):
    if (l2 + l3) > l1 and (l1 + l2) > l3 and (l1 + l3) > l2: 
        if l1==l2==l3:
            return  "triângulo equilátero"
        elif l1 != l2 != l3:
            return "triângulo escaleno"
        else:
            return "triângulo isósceles"
    else:
        return  "Não é um triângulo"


# exercício 2 

def dia_semana(num):
    if num == 1:
        return "Domingo"
    if num == 2:
        return "Segunda-feira"
    if num == 3:
        return "Terça-feira"
    if num == 4:
        return "Quarta-feira"
    if num == 5:
        return "Quinta-feira"
    if num == 6:
        return "Sexta-feira"
    if num == 7:
        return "Sábado"
    else:
        return "String vazia"
    



# exercício 3 

def soma(a, b):
    return a + b

def subtraçao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a,b):
    return a / b 

def cli():
    n1 = int(input("informe um numero:"))
    n2 = int(input("informe outro número:"))
    operaçao= input("informe a operação:")
   
    if operaçao == "soma":
        print(soma (n1,n2)) 
    elif operaçao == "subtração":
        print(subtraçao(n1,n2))
    elif operaçao == "multiplicação":
        print(multiplicacao(n1,n2))
    elif operaçao == "divisão":
        print(divisao(n1,n2))
    else:
        "Operação inválida"
    
def main():
    print(determina_tipo_triangulo(4, 4, 4)) 
    print(determina_tipo_triangulo(2, 4, 4)) 
    print(determina_tipo_triangulo(3, 4, 5)) 
    print(determina_tipo_triangulo(1, 1, 4))  
    print("-" * 40)
    print(dia_semana(3)) 
    print(dia_semana(5)) 
    print(dia_semana(7)) 
    print(dia_semana(10))
    print("-" * 40)
    cli()
    

main()