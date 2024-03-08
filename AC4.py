'''
Atividade complementar 4
Programação Estruturada 
Júlia Dominguez Curto 
Exercício em aula
'''


def ler_nome():
    """Retorna o nome do aluno inserido pelo usuário."""
    return input("Informe o seu nome: ")

def ler_notas():
    """Lê as notas de AP1, AP2, AS e AC do aluno, e retorna essas notas."""
    nota1 = float(input("Informe sua nota na AP1: "))
    nota2 = float(input("Informe sua nota na AP2: "))
    nota3 = float(input("Informe sua nota na AS: "))
    nota4 = float(input("Informe sua nota na AC: "))
    return nota1, nota2, nota3, nota4

def analisar_subst(ap1, ap2, asub):
    if ap1<= ap2 and asub > ap1:
        return asub, ap2
    if ap2<=ap1 and  asub> ap2:
        return asub, ap1
    return ap1, ap2
    """
    Retorna as duas notas a serem usadas no cálculo.
    A AS deve substituir a AP1 ou AP2 se for maior que elas.
    """

def calcular_media(ap1, ap2, asub, ac):
    """Calcula e retorna a média final do aluno."""
    prova1, prova2 = analisar_subst(ap1, ap2, asub)
    return (prova1 + prova2) * 0.4 + ac * 0.2

def aluno_foi_aprovado(media):
    """Retorna True se a média foi suficiente para aprovação do aluno."""
    return media >= 7

def notas_sao_validas(ap1, ap2, asub, ac):
    if 0 <= ap1 <= 10 and 0 <= ap2 <= 10 and 0 <= asub <= 10 and 0 <= ac <= 10:
        return ap1,ap2,asub,ac
    return "Dado inválido"

    """Retorna True se todas as notas estão entre 0 e 10, inclusive."""

def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            media = calcular_media(ap1, ap2, asub, ac)
            print("Média final:", media)
            if aluno_foi_aprovado(media):
                print("Aluno foi aprovado.")
            else:
                print("Aluno foi reprovado.")

main()



