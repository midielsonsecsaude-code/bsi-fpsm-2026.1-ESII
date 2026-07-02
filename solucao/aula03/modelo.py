# modelo.py — os DADOS do aluno, agora tipados (dataclass), e o repositório.
# Na v1.0 cada aluno era um dicionário solto ({"id":..., "nome":...}); aqui vira
# um Aluno com campos nomeados, e o AlunoRepo cuida de guardar/buscar.

from dataclasses import dataclass, field


@dataclass
class Aluno:
    """Os dados de um aluno (substitui o dicionário solto da v1.0)."""
    id: int
    nome: str
    plano: str
    checkins: int = 0


@dataclass
class AlunoRepo:
    """Guarda e busca os alunos. UMA responsabilidade: armazenamento."""
    alunos: list = field(default_factory=list)
    _proximo_id: int = 1

    def proximo_id(self):
        return self._proximo_id

    def salvar(self, nome, plano):
        """Cria e armazena um novo Aluno; devolve o Aluno criado."""
        aluno = Aluno(id=self._proximo_id, nome=nome, plano=plano)
        self.alunos.append(aluno)
        self._proximo_id += 1
        return aluno

    def buscar_por_nome(self, nome):
        """Devolve o Aluno com esse nome, ou None se não existir."""
        for a in self.alunos:
            if a.nome == nome:
                return a
        return None

    def listar(self):
        """Devolve todos os alunos armazenados."""
        return self.alunos
