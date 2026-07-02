# servico/newsletter.py — Forma News (com DIP)
#
# Agora o servico RECEBE o repositorio e o enviador por construtor.
# Ele nao cria mais nada por dentro — so usa o que recebeu.
class ServicoNewsletter:
    def __init__(self, repo, enviador):
        self.repo = repo
        self.enviador = enviador

    def enviar_edicao(self, texto):
        for a in self.repo.listar():
            if a.pode_receber():
                self.enviador.enviar(a.email, texto)
