# Soluções de referência

Esta pasta reúne as **soluções de referência e gabaritos** das atividades e provas — **divulgados
somente APÓS o prazo de entrega** de cada bloco. Use-as para **conferir e estudar**; a sua resposta não
precisa ser idêntica (as questões discursivas admitem redações diferentes) — o que vale é o **conceito
certo, referido ao código**.

## O que já está disponível

### NAP 1 — encerrada (tudo publicado)
| Aula | Conteúdo | Solução aqui |
|------|----------|--------------|
| 1 | Diagnóstico do sistema legado | `aula01/diagnostico.md` |
| 2 | Camadas / ADR / UML | `aula02/parteA-gabarito.md` + código em camadas (`aula02/`) |
| 3 | SRP (assíncrona) | `aula03/` — código separado por responsabilidade + `ANALISE.md` + `DIAGRAMA.md` |
| 4 | OCP | `aula04/parteA-gabarito.md` + código com Strategy/OCP (`aula04/`) |
| 5 | LSP, ISP, DIP | `aula05/parteA-gabarito.md` + código com DIP + fake (`aula05/`) |
| 6 | **Prova Escrita 1** | `aula06/prova-nap1-gabarito.md` |

### NAP 2 — parcial
| Aula | Conteúdo | Solução aqui |
|------|----------|--------------|
| 7 | Testes e cobertura | `aula07/parteA-gabarito.md` (**só a Parte A**) |
| 8 | TDD | `aula08/parteA-gabarito.md` (**só a Parte A**) |

> As **Partes B da NAP 2** e as **Aulas 9 e 10** (e a Prova 2) serão publicadas **após os respectivos
> prazos de entrega**.

## Como rodar as soluções de código (Parte B)
```bash
cd solucao/aula04      # (ou aula02, aula03, aula05)
python3 main.py        # aula03: python3 academia.py
```
Cada solução foi verificada rodando e comparando o comportamento com o sistema original da aula.
