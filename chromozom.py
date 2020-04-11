class Chromozom:
    dna=None
    fitnes=None



    def __init__(self, dna_vstup):
        self.dna=dna_vstup


    def __lt__(self, other):
        return self.fitnes > other.fitnes