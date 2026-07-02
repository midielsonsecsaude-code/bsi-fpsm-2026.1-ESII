# experimento.py — prove que da para "testar" sem mandar e-mail de verdade
#
# Parte B: a classe FakeEmail abaixo e um e-mail "de mentira".
# Ela respeita o mesmo contrato do Enviador (tem enviar(para, texto)), mas
# em vez de mandar e-mail de verdade so ANOTA quem receberia. Como o servico
# recebe o enviador por construtor (DIP), da para injetar o fake no lugar do
# SMTP e testar sem enviar nada.
from repositorio.assinantes import RepositorioAssinantes
from servico.newsletter import ServicoNewsletter
from enviador.enviador import Enviador


class FakeEmail(Enviador):
    def __init__(self):
        self.enviados = []          # so anota, nao envia nada

    def enviar(self, para, texto):
        self.enviados.append(para)


if __name__ == "__main__":
    repo = RepositorioAssinantes()
    enviador = FakeEmail()                     # de mentira, no lugar do SMTP
    servico = ServicoNewsletter(repo, enviador)  # injeta o fake
    servico.enviar_edicao("Edicao teste")

    print("Quem receberia:", enviador.enviados)
    # esperado: ['ana@exemplo.com', 'bia@exemplo.com'] — sem e-mail de verdade!
