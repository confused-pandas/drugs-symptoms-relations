from manager.omim_text import OmimTextManager

class Main:

    def __init__(self, clignical_sign):
        self.clignical_sign = clignical_sign

    if __name__== '__main__':
        manager = OmimTextManager("Normocephaly")
        manager.extractDataFromCs()