from App.diagrama_sequencia import DiagramaSequencia
from App.mensagens import AdicionarMensagem, MensagemAssincrona, MensagemSincrona, MensagemResposta
from App.lifeline import Lifeline
from App.fragments import Fragments

if __name__ == '__main__':
    lifeline1 = Lifeline('Lifeline1')
    lifeline2 = Lifeline('Lifeline2')
    mensagem_sincrona = AdicionarMensagem('Mensagem Sincrona', 0.9, 'Source', 'Terget')
    mensagem_assincrona = AdicionarMensagem('Mensagem Assincrona', 0.5, 'Lifeline1', 'Lifeline2')
    resposta = AdicionarMensagem('Resposta', 0.3, 'Lifeline 2', 'Lifeline 1')
    fragment = Fragments('Fragmento Opcional', True, 'Nome do diagrama')

    diagrama = DiagramaSequencia('Nome do diagrama', 'condicao', lifeline1.arrayLifeline, mensagem_sincrona.arrayMensagem, fragment.arrayFragments)