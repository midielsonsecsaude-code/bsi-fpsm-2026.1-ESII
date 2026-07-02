# academia.py — SOLUÇÃO da Aula 3 (SRP aplicado).
# Esta camada agora só faz a TELA (interface): lê o que o usuário digita e mostra
# o resultado. A REGRA foi para servico.AcademiaService, os DADOS para
# modelo.Aluno/AlunoRepo e a NOTIFICAÇÃO para notificador.Notificador.
# O comportamento observável é o MESMO da v1.0.

from servico import AcademiaService


class TelaAcademia:
    """Responsabilidade única: interface com o usuário (menu, input, prints)."""

    def __init__(self, servico=None):
        self.servico = servico or AcademiaService()

    def matricular(self):
        nome = input("Nome do aluno: ")
        print("Planos: 1-Mensal  2-Trimestral  3-Anual")
        plano = input("Plano: ")
        try:
            aluno, _valor = self.servico.matricular(nome, plano)
        except ValueError as e:
            print(str(e))            # "Plano inválido."
            return
        print(f"Aluno {aluno.id} matriculado.")

    def check_in(self):
        nome = input("Nome do aluno: ")
        try:
            aluno = self.servico.check_in(nome)
        except LookupError as e:
            print(str(e))            # "Aluno não encontrado."
            return
        print(f"Check-in de {nome} registrado. Total: {aluno.checkins}.")

    def listar(self):
        print("--- Alunos ---")
        for aluno, valor in self.servico.listar():
            print(f"{aluno.id}- {aluno.nome}  (R${valor:.2f}/mês, {aluno.checkins} check-ins)")


def main():
    tela = TelaAcademia()
    while True:
        print("\n1-Matricular  2-Check-in  3-Listar  0-Sair")
        op = input("Opção: ")
        if op == "1":   tela.matricular()
        elif op == "2": tela.check_in()
        elif op == "3": tela.listar()
        elif op == "0": break


if __name__ == "__main__":
    main()
