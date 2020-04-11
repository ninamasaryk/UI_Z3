from pomocne_funkcie import *

def hrab(a,b,mapa,rozmer_a,rozmer_b):
	if(a>=0 and b>=0 and a<rozmer_a and b<rozmer_b and mapa[a][b]==0):
		return True
	return False


def pohrabkaj(postupnost,mapa_povodna,a,b):
	print(postupnost)
	deepcopy1d2d = lambda lVals: [x if not isinstance(x, list) else x[:] for x in lVals]
	mapa=deepcopy1d2d(mapa_povodna)
	pohoda=True
	uviaznuty=False
	for i in postupnost:
		num=postupnost.index(i)+1
		print(i)
		akt_a=1;
		akt_b=1;
		zvisle_b=[0,1,-1,0]
		zvisle_a=[1,0,0,-1]
		vodorovne_b=[1,0,0,-1]
		vodorovne_a=[0,1,-1,0]

		if (i<a):
			akt_a = i+1
			if (mapa[akt_a][akt_b] == 0):
				mapa[akt_a][akt_b] = num

				while (0 < akt_a) and (akt_a <= a) and (0 < akt_b) and (akt_b <= b) and not(uviaznuty):
					result=False
					j=0
					while(j<4):
						print("j ",j,"A: ", akt_a + int(vodorovne_a[j]), " B: ", akt_b + int(vodorovne_b[j]))
						result = hrab(akt_a + int(vodorovne_a[j]), akt_b + int(vodorovne_b[j]), mapa, a+2, b+2)
						if (result):
							akt_a += int(vodorovne_a[j])
							akt_b += int(vodorovne_b[j])
							mapa[akt_a][akt_b] = num
							print_mapa(mapa, a, b)
							print("--------------------")
							j = 4
						j+=1
					if not (result):
						uviazol = je_uviaznuty(akt_a, akt_b, a, b)
						if (uviazol):
							uviaznuty = True
						break






		else:
			akt_b = i - a+1
			if(mapa[akt_a][akt_b]==0):
				mapa[akt_a][akt_b]=num
				while (0 < akt_a) and (akt_a <= a ) and (0 < akt_b) and (akt_b <= b ) and not(uviaznuty):

					result = False
					j = 0
					while (j < 4):
						print("j: ",j,"A: ",akt_a+int(zvisle_a[j])," B: ",akt_b+int(zvisle_b[j]))
						result = hrab(akt_a + int(zvisle_a[j]), akt_b + int(zvisle_b[j]), mapa, a+2, b+2)
						if (result):
							akt_a += int(zvisle_a[j])
							akt_b += int(zvisle_b[j])
							mapa[akt_a][akt_b] = num
							print_mapa(mapa, a, b)
							print("--------------------")
							j = 4
						j += 1
					if not (result):
						uviazol=je_uviaznuty(akt_a,akt_b,a,b)
						if (uviazol):
							uviaznuty=True
						break


		print_mapa(mapa,a,b)
	return

def milujte_sa_mnozte_sa(populacia,mapa,a,b):
	for item in populacia:
		pohrabkaj(item.dna,mapa.copy(),a,b)








