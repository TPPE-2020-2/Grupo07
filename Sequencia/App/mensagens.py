import os.path
import sys

###### mover metodo ou atributo #######

class Mensagem():

    def __init__(self, name='', prob=0.0, source='', target=''):
        self.name = name
        self.prob = prob
        self.source = source
        self.target = target


class AdicionarMensagem(Mensagem):
    arrayMensagem = []

    def __init__(self, name='', prob=0.0, source='', target=''):
        mensagem = {
            'name': name,
            'prob': prob,
            'source': source,
            'target': target,
            'tipo': 'inicial'
        }

        self.arrayMensagem.append(mensagem)


class MensagemSincrona:
    def __init__(self, name="", prob=0.0, source="", target=""):
        try:
            if not name or not prob or not source or not target:
                raise Exception('MessageFormatException')
        except Exception as error:
            print('Falta um atributo', error)

        finally:

            mensagem = {
                'name': name,
                'prob': prob,
                'source': source,
                'target': target,
                'tipo': 'Sincrona'
            }

            self.mensagem = mensagem





class MensagemAssincrona:
    def __init__(self, name="", prob=0.0, source="", target=""):
        try:
            if not name or not prob or not source or not target:
                raise Exception('MessageFormatException')

        except Exception as error:
            print('Falta um atributo', error)

        finally:

            mensagem = {
                'name': name,
                'prob': prob,
                'source': source,
                'target': target,
                'tipo': 'Assincrona'
            }

            self.mensagem = mensagem


class MensagemResposta:
    def __init__(self, name="", prob=0.0, source="", target=""):
        try:
            if not name or not prob or not source or not target:
                raise Exception('MessageFormatException')

        except Exception as error:
            print('Falta um atributo', error)

        finally:

            mensagem = {
                'name': name,
                'prob': prob,
                'source': source,
                'target': target,
                'tipo': 'Resposta'
            }

            self.mensagem = mensagem


if __name__ == "__main__" and __package__ is None:
    from os import sys, path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    # def get_name_fals(self):
    #     return 'Mensagem 1'

    # def get_name(self):
    #     return self.name

    # def set_name(self, name):
    #     self.name = name

    # def get_prob(self):
    #     return self.prob

    # def set_prob(self, prob):
    #     self.prob = prob

    # def get_source(self):
    #     return self.source

    # def set_source(self, source):
    #     self.source = source

    # def get_target(self):
    #     return self.target

    # def set_target(self, target):
    #     self.target = target

#     def CadastrarMensagem(self):

#         # ARRUMAR A EXCEPTION PARA QUE VERIFIQUE SE ESTA FALTANDO PARAMETRO
#         # if not self.nome or not self.prob or not self.source or not self.target:
#         #     raise Exception('MessageFormatException')
#         #else:
#         if os.path.exists("msg.txt"):
#             msg_arq = open("msg.txt", 'r')
#             msg_lista = msg_arq.readlines()
#             msg_arq.close()

#             try:
#                 msg_lista.insert(len(msg_lista)-1, "< Message name = " + str(self.name) + " " + " prob = " + str(self.prob) + " source = " + str(self.source) + " target = " + str(self.target) + " " + "/>" + '\n')

#                 if not self.name or not self.prob or not self.source or not self.target:
#                     raise Exception('MessageFormatException')

#             except:
#                 sys.exit('MessageFormatException')

#             msg_arq = open("msg.txt", 'w')
#             msg_lista = "".join(msg_lista)
#             msg_arq.write(msg_lista)
#             msg_arq.close()


#         else:
#             msg_arq = open("msg.txt", 'w+')
#             msg_lista.append("< Message >" + '\n')
#             msg_lista.append(+" < Message  name = " + " " + str(self.name) + " "+" prob = " + " " + str(self.prob) + " " + " source = " + " " + str(self.source) + " " + "target = " + " " + str(self.target) +  "/>" + '\n')
#             msg_lista.append("</ Message >" + '\n')
#             msg_arq.writelines(msg_lista)


#         return


# #mensagem1 = Mensagem(None,0.9,"teste2","teste3")
# #mensagem1.CadastrarMensagem()
# mensagem2 = Mensagem("Sincrona", 0.5, "Lifeline1", "Lifeline2")
# mensagem2.CadastrarMensagem()