# Análise — as 3 responsabilidades da classe `Academia` (v1.0)

**Parte 2 da atividade (0,3):** respostas com base no `academia.py` da pasta da aula.

---

## 1. Quais são as 3 responsabilidades grudadas na classe `Academia`?

> A classe faz **regra de negócio** (calcula o valor do plano e conta os
> check-ins), **tela** (mostra o menu, lê o que o usuário digita com `input()` e
> imprime as confirmações) e **notificação** (monta e "envia" o aviso de
> WhatsApp ao aluno). As três coisas ficam misturadas dentro dos mesmos métodos.

## 2. Aponte, no código, **uma linha** de cada responsabilidade
(linhas do `aula03/academia.py` original)

- **Regra de negócio** (cálculo / contagem): linha **21** — `if plano == "1": valor = 100.0` (e a contagem em `aluno["checkins"] += 1`, linha 53)
- **Tela** (interface com o usuário): linha **16** — `nome = input("Nome do aluno: ")`
- **Notificação** (aviso ao aluno): linha **36** — `print(f"[WhatsApp para {nome}] Bem-vindo(a) à FitPará! Mensalidade: R${valor:.2f}.")`

## 3. Como o SRP separa essas responsabilidades?
Em qual componente cada responsabilidade passa a morar:

> - A **notificação** vai para a classe **`Notificador`** (`notificador.py`): só
>   ela sabe montar/enviar o aviso, sempre no formato `[WhatsApp para ...] ...`.
> - A **regra de negócio** vai para **`AcademiaService`** (`servico.py`):
>   calcula o valor do plano (RN01) e conta o check-in (RN02), sem `input()` nem
>   `print()` de tela. Os **dados** deixam de ser dicionário solto e viram a
>   dataclass **`Aluno`**, guardada pelo **`AlunoRepo`** (`modelo.py`).
> - A **tela** fica na **`TelaAcademia`** (`academia.py`): só o menu, os
>   `input()` e os `print()` de confirmação; ela **usa** o serviço, que **usa**
>   o repositório e o notificador.

## 4. Por que ficou melhor? Cite **um** RNF

> **RNF03 — Manutenibilidade.** Trocar o texto ou o canal do aviso
> (WhatsApp → SMS → e-mail) agora se faz só dentro do `Notificador`, sem tocar
> na regra (`AcademiaService`) nem na tela (`academia.py`). Na v1.0 o `print` do
> aviso estava grudado no meio da regra e da tela, então qualquer mudança no
> canal obrigava a mexer nos métodos de negócio.
>
> (Também melhora o **RNF04 — Testabilidade**: `valor_do_plano("1")` e
> `AcademiaService.matricular` podem ser testados sem depender do `input()`,
> injetando um notificador de mentira.)
