# Diagnóstico de referência — Aula 1 (Sistema de Empréstimo de Equipamentos)

> Solução de referência da atividade de **diagnóstico** (divulgada após o prazo). A tarefa pedia **ler o
> sistema + a documentação** e **listar as divergências / a dívida técnica** — comparando o que os `docs/`
> descrevem com o que o `emprestimos.py` realmente faz. Abaixo, cada ponto vem com a **evidência no código**.
> A sua lista não precisa ser idêntica: o que conta é **identificar os problemas certos** e **explicá-los
> referidos ao código**.

O próprio `docs/projeto.md` já registra parte disso na **tabela de dívida técnica** (DT01–DT07) e nas
**decisões de projeto** (DP01–DP05) — um bom diagnóstico confirma cada item **no código** e acrescenta o que
observar.

| # | Problema (dívida técnica) | Evidência em `emprestimos.py` | Consequência |
|---|---|---|---|
| 1 | **Ausência de camadas** — tela + regra + dados no mesmo arquivo (DT01/DP01) | a classe `Sistema` (regra), o `def main()` com `input()/print()` (tela) e as listas globais (dados) convivem no mesmo `.py` | nada é separável nem reutilizável; qualquer mudança mexe em tudo |
| 2 | **Variáveis globais acessadas direto pela classe** (DT02) | `equipamentos` e `emprestimos_registrados` são globais; `registrar`/`devolver` fazem `for e in equipamentos` / `... emprestimos_registrados` diretamente | alto acoplamento ao estado global; impossível ter duas instâncias, difícil de testar |
| 3 | **Notificação misturada com a regra de negócio** (DT03/DP03) | `print("[EMAIL] ...")` aparece **dentro** de `registrar`, `devolver` **e** `listar_atrasados` (3 lugares) | não dá para trocar o canal de aviso (e-mail→SMS) sem mexer na regra; baixa coesão |
| 4 | **Cálculo de multa duplicado** (DT04) | o bloco `if tipo == "notebook" ... elif "projetor" ... elif "cabo"` aparece **igual** em `devolver` e em `listar_atrasados` | mudar uma tarifa num lugar e esquecer o outro gera bug silencioso (fere o DRY) |
| 5 | **Multa com `if/elif` por tipo** (DT06/DP05 — fere OCP) | o mesmo `if/elif` por tipo de equipamento decide a multa | adicionar um tipo novo (ex.: `"tablet"`) exige **editar** os métodos existentes — não é fechado para modificação |
| 6 | **Dados sem tipagem — dicionários soltos** (DT07/DP02) | equipamentos e empréstimos são `dict` (`e["disponivel"]`, `emprestimo["tipo"]`) em vez de classes de domínio | sem validação; um erro de digitação numa chave (`"tpio"`) não é avisado |
| 7 | **Zero testes automatizados** (DT05/DP04) | não há arquivo de teste; o `docs/projeto.md §7` admite "testes não implementados na v1.0" | qualquer mudança é feita **sem rede de segurança** — risco alto de regressão |

## Observações de coerência docs × código (bônus)
- O **diagrama de classes** (`docs/projeto.md §3`) mostra só a classe `Sistema` acessando as variáveis
  globais — e **não** representa o menu (`main`) nem separa camadas. Isso é **coerente** com o código (a
  fragilidade está documentada), não uma contradição — mas evidencia que a estrutura real não tem desenho de
  arquitetura de verdade.
- `docs` diz que a notificação é "via `print()` — não envia e-mail real" (DP03): confere com o código, que
  só imprime `[EMAIL] ...`.
- **Qualidade externa × interna:** o sistema **funciona** (empresta, devolve, calcula multa) — a qualidade
  **externa** está ok; todos os problemas acima são de qualidade **interna** (estrutura), que o usuário não vê
  mas que torna o sistema caro de manter. É esse o ponto do diagnóstico.

> **Como isso conecta com o curso:** cada item acima vira tema de uma aula seguinte — camadas (Aula 2), SRP
> (Aula 3), OCP (Aula 4), DIP/testabilidade (Aulas 5 e 7), duplicação/refactoring (Aula 10).
