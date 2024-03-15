"""
Atividade Complementar 5
Programação - 15/03/2024
Júlia Curto
"""
import random 



def main():
    vida_avent = 100
    ataq_avent = random.randint(10,20)
    def_avent = random.randint(1,5)
    vida_monst = random.randint(60 , 80)
    ataq_monst = random.randint(20,30)
    rodada = 1
    print("Aventureiro:", vida_avent, "- att", ataq_avent , "- def",  def_avent)
    print("Monstro:",  vida_monst, " - att", ataq_monst)
    while vida_avent > 0 and vida_monst > 0:
        print("Rodada", rodada)
        vida_monst = vida_monst - random.randint(1,ataq_avent)
        if vida_monst <= 0:
            break 
        vida_avent = vida_avent - (random.randint(1, ataq_monst) - def_avent) 
        if vida_avent <= 0:
            break
        print("Aventureiro:", vida_avent, "- att", ataq_avent , "- def",  def_avent)
        print("Monstro:",  vida_monst, " - att", ataq_monst)
        rodada += 1
    if vida_monst <= 0:
        print("Você venceu!")
    elif vida_avent <= 0:
        print("Você perdeu!")









main() 