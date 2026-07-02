# template — esqueleto em camadas (para você completar)

Este é o **código com que você vai trabalhar**. A estrutura em camadas já está montada;
o que falta são as implementações, marcadas com `# TODO`.

**Sua tarefa:** complete os `# TODO` movendo a lógica que hoje está no `../pedidos.py`
para a camada certa. Quando terminar, rode e deve funcionar igual ao monolito:

```bash
cd template
python main.py
```

Camadas: `apresentacao/` (tela) · `servico/` (regras) · `repositorio/` (dados) · `modelos/` (entidades).
A `main.py` e a `apresentacao/cli.py` já vêm prontas — foque em **modelos**, **repositorio** e **servico**.

**Como saber se acertou:** rode `python main.py` e compare com o `../pedidos.py` original —
mesmo menu e mesmo total (ex.: 1 X-Burguer + 1 Refrigerante = R$24.00). Se o comportamento
bate, você completou certo.
