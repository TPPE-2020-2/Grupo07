
class Fragments():
    arrayFragments = []
    def __init__(self, nome="", condicao_guarda=True, representedBy = ""):
        try:
            if not representedBy:
                raise Exception('EmptyOptionalFragment')
            
            fragmento_opcional = {
                'nome': nome,
                'condicao_guarda': condicao_guarda,
                'representedBy': representedBy
            }
            if condicao_guarda:
                self.arrayFragments.append(fragmento_opcional)
            else:
                pass

        except Exception as error:
            print('Fragmento Opcional', error)

    def addFragment(self, fragmento_opcional):
        self.arrayFragments.append(fragmento_opcional) 
