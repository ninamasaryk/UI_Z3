import numpy as np
from chromozom import *

def print_mapa(mapa,a,b):
    for i in range(b+2):
        print(mapa[i]);


def je_uviaznuty(a,b,rozmer_a,rozmer_b):
    if(a>1) and (b>1) and (a<rozmer_a+1) and (b<rozmer_b-1):
        return True
    return False

def oramuj(mapa,a,b):
    for i in range(a+2):
        for j in range(b+2):
            if (i==0) or (j==0) or (i==a+1) or (j==b+1):
                mapa[i][j]='x'
def vytvor_populaciu(a,b,pocet):
    populacia=[]
    for i in range(pocet):

        prvok = Chromozom(tuple(np.random.permutation(a+b)))
        print(tuple(prvok.dna))
        populacia.append(prvok)

    return populacia