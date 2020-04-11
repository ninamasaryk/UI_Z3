from pomocne_funkcie import *
from mnozenie import *

pocet_pociatocna_generacia=10
pravdepodobnosť_krizenia=0.9
pravdepodobnost_mutacie=0.1

while (1):
    print("Zadaj vstup")
    a=int(input())
    b=int(input())
    mapa = [[0]*(a+2) for _ in range(b+2)]
    #oramuj(mapa,a,b)
    pocet_kamenov=int(input())
    for i in range(0,pocet_kamenov):
        kamen_a=int(input())
        kamen_b=int(input())
        mapa[kamen_a][kamen_b]=-1

    populacia=vytvor_populaciu(a,b,pocet_pociatocna_generacia)
    milujte_sa_mnozte_sa(populacia,mapa.copy(),a,b)

    print_mapa(mapa,a,b)

    for item in populacia:
        print(tuple(item.dna))