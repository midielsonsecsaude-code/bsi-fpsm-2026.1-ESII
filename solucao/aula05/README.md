# Solucao — Aula 5 (Parte B): DIP na Forma News

Esta e a **solucao de referencia** da Parte B da Aula 5. O sistema e a
**Forma News** (newsletter que guarda assinantes e envia cada edicao por
e-mail). O DIP ja esta aplicado: o servico **recebe** o repositorio e o
enviador por construtor (injecao) em vez de cria-los dentro de si, e existe
uma interface `Enviador` (ABC). O `experimento.py` prova que da para testar
**sem mandar e-mail de verdade**, usando um `FakeEmail`.

```
solucao/aula05/
├── modelos/assinante.py        ← Assinante, Gratis, Premium
├── repositorio/assinantes.py   ← guarda os assinantes (em memoria)
├── enviador/enviador.py        ← Enviador (abstracao ABC) + ServidorSMTP
├── servico/newsletter.py       ← RECEBE repo e enviador por construtor (DIP)
├── main.py                     ← composition root: monta e injeta as pecas reais
└── experimento.py              ← FakeEmail: testa sem e-mail real
```

## O DIP aqui
- **Antes** (`aula05/servico/newsletter.py`): o servico fazia
  `self.repo = RepositorioAssinantes()` e `self.enviador = ServidorSMTP()`
  dentro do `__init__` — logo, rodar um teste mandaria e-mail de verdade.
- **Depois** (aqui): `ServicoNewsletter(repo, enviador)` — o servico so usa o
  que recebeu. Quem monta as pecas concretas e o `main.py` (composition root).
- **Prova de fogo**: `experimento.py` injeta um `FakeEmail` (mesmo contrato do
  `Enviador`, mas so anota quem receberia) no lugar do `ServidorSMTP`.

## Como rodar
```bash
cd solucao/aula05
python3 main.py         # sistema real: imprime os envios do SMTP
python3 experimento.py  # testa com o fake, sem e-mail de verdade
```

Saida esperada de `main.py`:
```
[SMTP] enviando para ana@exemplo.com: Edicao #42 no ar!
[SMTP] enviando para bia@exemplo.com: Edicao #42 no ar!
```

Saida esperada de `experimento.py`:
```
Quem receberia: ['ana@exemplo.com', 'bia@exemplo.com']
```
