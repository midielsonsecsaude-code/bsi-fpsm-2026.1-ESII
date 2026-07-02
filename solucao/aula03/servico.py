# servico.py — a REGRA DE NEGÓCIO, separada da tela e da notificação.
# Aqui não há input() nem print() de tela: só o cálculo do plano (RN01), a
# contagem de check-in (RN02) e o disparo do aviso via Notificador.
# Por isso a regra pode ser testada sem depender do teclado nem do "envio".

from modelo import AlunoRepo
from notificador import Notificador

# RN01 — o valor da mensalidade depende do plano.
PLANOS = {"1": 100.0, "2": 90.0, "3": 80.0}


def valor_do_plano(plano):
    """RN01: devolve a mensalidade do plano, ou None se o plano for inválido."""
    return PLANOS.get(plano)


class AcademiaService:
    """As regras: matricular (calcular o valor do plano) e fazer check-in.
    Usa o AlunoRepo para guardar os dados e o Notificador para avisar."""

    def __init__(self, repo=None, notificador=None):
        self.repo = repo or AlunoRepo()
        self.notificador = notificador or Notificador()

    def matricular(self, nome, plano):
        """RF01: matricula um aluno. Devolve (aluno, valor).
        Levanta ValueError se o plano for inválido (RN01)."""
        valor = valor_do_plano(plano)
        if valor is None:
            raise ValueError("Plano inválido.")
        aluno = self.repo.salvar(nome, plano)
        # NOTIFICAÇÃO: a MESMA mensagem de boas-vindas da v1.0.
        self.notificador.enviar(
            nome, f"Bem-vindo(a) à FitPará! Mensalidade: R${valor:.2f}."
        )
        return aluno, valor

    def check_in(self, nome):
        """RF02/RN02: registra o check-in de um aluno já matriculado.
        Devolve o Aluno. Levanta LookupError se não estiver matriculado."""
        aluno = self.repo.buscar_por_nome(nome)
        if aluno is None:
            raise LookupError("Aluno não encontrado.")
        aluno.checkins += 1
        # NOTIFICAÇÃO: a MESMA mensagem de check-in da v1.0.
        self.notificador.enviar(nome, "Check-in confirmado! Bom treino.")
        return aluno

    def listar(self):
        """RF04: devolve a lista de (aluno, valor) para a tela exibir."""
        return [(a, valor_do_plano(a.plano)) for a in self.repo.listar()]
