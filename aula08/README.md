# Aula 8 — TDD (Test-Driven Development)

Sistema de hoje: um **validador de senha** 🔒. A **teoria** completa está nos slides e a **atividade** está no **SIGAA**.

TDD é escrever o **teste primeiro** e só depois o código que faz ele passar. O ciclo é **RED → GREEN → REFACTOR**: o teste falha (vermelho), você escreve o mínimo para passar (verde), depois melhora o código sem quebrar os testes.

## O que tem aqui
```
aula08/
├── senha.py          ← a função validar() construída por TDD (3 regras, depois refatorada)
└── test_senha.py     ← 4 testes (a senha boa + uma por regra) + um # TODO (a sua tarefa, Parte B)
```

A função `validar(senha)` devolve uma **lista com os problemas** da senha. Lista vazia (`[]`) = senha aprovada. **Cada regra nasceu de um teste** — foi assim que a aula construiu o arquivo.

## Como rodar os testes
No terminal do Codespaces (o `pytest` já vem instalado):
```bash
cd aula08
pytest
```
Você verá **`4 passed`**. Depois de completar a Parte B (a regra da letra minúscula), verá **`5 passed`**.

## A tarefa (resumo)
Adicione **uma regra nova** (senha precisa de letra **minúscula**) usando o ciclo do TDD: escreva o **teste primeiro** (ele falha — RED), depois adicione a regra em `senha.py` (passa — GREEN). O passo a passo está na **Parte B** (SIGAA).
