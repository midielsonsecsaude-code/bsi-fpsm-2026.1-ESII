# Solução de referência — Aula 3 (SRP) — Academia FitPará

Versão do sistema **depois de aplicar o SRP**. Cada responsabilidade da classe
`Academia` v1.0 (que fazia tudo) foi separada em um componente próprio.

## Arquivos
| Arquivo | Responsabilidade (SRP) |
|---|---|
| `modelo.py` | **dados** — dataclass `Aluno` + `AlunoRepo` (guardar/buscar) |
| `notificador.py` | **notificação** — `Notificador.enviar()` |
| `servico.py` | **regra de negócio** — `AcademiaService` (RN01/RN02) |
| `academia.py` | **tela** — `TelaAcademia` + `main()` (entrypoint CLI) |
| `ANALISE.md` | análise das 3 responsabilidades |
| `DIAGRAMA.md` | diagrama de classes em Mermaid |

## Como rodar
```bash
cd solucao/aula03
python3 academia.py
```

O comportamento observável é o **mesmo** da v1.0 (`aula03/academia.py`): mesmo
menu, mesmas mensagens de WhatsApp e mesmas confirmações de tela.
