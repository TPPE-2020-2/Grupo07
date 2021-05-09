import os.path
import sys


class Lifeline(): 
    arrayLifeline = []
    def __init__(self, nomeLifeline =""):

        lifeline = {

            'nomeLifeline': nomeLifeline
        }

        self.lifeline = lifeline
        
        self.arrayLifeline.append(nomeLifeline)
        

          

    #falsificacao
    def get_name_fals(self):
      return 'Lifeline fals'

if __name__ == "__main__" and __package__ is None:
    from os import sys, path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))