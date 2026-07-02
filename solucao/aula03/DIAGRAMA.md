# Diagrama de classes — Academia FitPará (depois do SRP)

**Parte 1 da atividade (0,3):** diagrama de classes em **Mermaid** com a
decomposição em componentes. O GitHub renderiza Mermaid sozinho ao abrir o
arquivo no site.

```mermaid
classDiagram
    %% ===== EXEMPLO JÁ RESOLVIDO — os dados do aluno (dataclass) =====
    class Aluno {
        -id: int
        -nome: str
        -plano: str
        -checkins: int
    }

    %% ===== Componentes do SRP =====
    class AlunoRepo {
        -alunos: list
        -_proximo_id: int
        +proximo_id() int
        +salvar(nome, plano) Aluno
        +buscar_por_nome(nome) Aluno
        +listar() list
    }

    class Notificador {
        +enviar(destinatario, mensagem)
    }

    class AcademiaService {
        -repo: AlunoRepo
        -notificador: Notificador
        +matricular(nome, plano) Aluno
        +check_in(nome) Aluno
        +listar() list
    }

    class TelaAcademia {
        -servico: AcademiaService
        +matricular()
        +check_in()
        +listar()
    }

    %% Ligações (quem usa quem)
    AlunoRepo o-- Aluno : guarda
    AcademiaService ..> Aluno : cria
    AcademiaService --> AlunoRepo : usa
    AcademiaService --> Notificador : usa
    TelaAcademia --> AcademiaService : usa
```

**O que cada classe guarda/faz:**
- `Aluno` — os dados de um aluno (`id`, `nome`, `plano`, `checkins`). É uma **dataclass**.
- `AlunoRepo` — guarda e busca os alunos (salvar, buscar por nome, listar, próximo id).
- `Notificador` — envia o aviso ao aluno, sempre no formato `[WhatsApp para ...] ...`.
- `AcademiaService` — as **regras**: matricular (calcular o valor do plano — RN01), fazer check-in (RN02).
- `TelaAcademia` — a **tela** (menu, `input()`, `print()` de confirmação); usa o serviço.
