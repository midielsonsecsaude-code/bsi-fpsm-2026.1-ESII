# Aula 7 — Parte A (Questionário) — GABARITO DE REFERÊNCIA

> **Chave de respostas.** Publicada **após o encerramento do prazo** de entrega.
> Uso: correção e conferência. **10 questões** — 8 objetivas (marcar uma) e 2 de justificativa.
> Valor total da Parte A: **1,0 ponto** (todas as questões respondidas corretamente).
>
> Base de correção: material da Aula 7 (`aula07/placar.py`, `partida.py`, `test_placar.py`, `README.md`)
> e a teoria da aula (teste de unidade, `assert`, AAA, pirâmide de testes, cobertura, dublês —
> stub/spy/fake/mock — e DIP para injetar o dublê).

---

## Objetivas — resposta rápida

| Q | Resposta correta |
|---|---|
| Q1 | Uma função que confere se o código faz o esperado, usando `assert`. |
| Q2 | Falha e avisa, porque o que vem depois dele é falso (2+2 não é 5). |
| Q3 | `"empate"`. |
| Q4 | Arrange → Act → Assert. |
| Q6 | A `Partida` receber o narrador pelo construtor (injeção de dependência — DIP). |
| Q7 | Entra no lugar de uma peça real para o teste não disparar o efeito de verdade. |
| Q8 | Cobertura mostra quanto do código os testes exercitam — mas alta cobertura não garante testes bons. |
| Q9 | Testes de unidade (muitos, rápidos, isolados). |

Justificativas: **Q5** e **Q10** (respostas-modelo abaixo).

---

## Correção comentada

### Q1 — O que é um teste automático?
**Correta:** *"Uma função que confere se o código faz o esperado, usando `assert`."*

**Por quê:** é exatamente o que os arquivos mostram. Em `test_placar.py`, cada teste é uma
função `test_...` que usa `assert` para conferir o esperado
(`assert resultado(2, 1) == "vitória"`). O comentário do próprio arquivo diz: *"Cada teste é
uma função que começa com `test_` e confere o código com `assert`."*
As demais são distratores: teste não conserta código sozinho, não é relatório à mão, nem teste de digitação.

---

### Q2 — `assert 2 + 2 == 5`
**Correta:** *"Falha e avisa, porque o que vem depois dele é falso (2+2 não é 5)."*

**Por quê:** `assert` só passa quando a condição é **verdadeira**. `2 + 2` é `4`, então
`2 + 2 == 5` é falso e o `assert` **falha** (levanta `AssertionError`) — é assim que um teste
avisa que algo está errado. `assert` **não** passa sempre (senão não serviria para testar).

---

### Q3 — `resultado(1, 1)`
**Correta:** *"`empate`."*

**Por quê:** em `placar.py`, com `gols_casa = 1` e `gols_fora = 1`: não é `1 > 1` (falha o `if`),
não é `1 < 1` (falha o `elif`), então cai no `return "empate"`. Gols iguais **não** dão erro —
é justamente o caso de empate (e é o teste que o aluno escreve na Parte B).

---

### Q4 — Estrutura AAA (linhas A, B, C)
**Correta:** *"Arrange (prepara) → Act (age) → Assert (confere)."*

**Por quê:** na imagem,
- **A** `casa, fora = 2, 1` → **Arrange**: prepara os dados de entrada.
- **B** `r = resultado(casa, fora)` → **Act**: executa a ação/função sob teste.
- **C** `assert r == "vitória"` → **Assert**: confere o resultado.

Essa é a ordem canônica do padrão AAA. As demais opções embaralham a ordem.

---

### Q5 — (Justificativa) Por que o teste não narra um gol de verdade?
**Tipo:** resposta aberta. Aceitar qualquer redação com suas palavras que contenha a ideia central.

**Resposta-modelo (curta):**
> Porque no teste a `Partida` recebe o `FakeNarrador` no lugar do `Narrador` real. O `FakeNarrador`
> não imprime "GOOOL" (não faz `print`) — o método `gol()` dele apenas **anota** o time numa lista
> (`gols_narrados.append(time)`). Assim o teste verifica o comportamento sem disparar o efeito real
> de narrar ao vivo.

**Pontos que valem (basta a ideia principal):**
- O dublê **substitui** o narrador de verdade no teste (via construtor).
- O dublê **não executa o efeito real** (não faz o `print`/não narra).
- Ele só **guarda/anota** o que foi chamado, para o teste conferir depois.

**Não exigir** que o aluno classifique o dublê pelo nome técnico — ver a nota de ambiguidade abaixo.

> ⚠️ **Nota de correção importante (para o professor):** o objeto da imagem se chama
> `FakeNarrador`, mas o teste **inspeciona o que ele registrou** (`assert fake.gols_narrados == ["Brasil"]`).
> Um dublê que **anota/registra as chamadas para o teste verificar depois** é, pela teoria da Aula 7,
> um **spy**, não um "fake" no sentido estrito (um *fake* seria uma implementação alternativa
> funcional, ex.: um repositório em memória). Aqui o **nome** da classe é "Fake" por didática, mas o
> **papel** que ela cumpre no teste é de **spy**. **Q5 não pede essa classificação** (só pede por que
> não narra), então isso não afeta a correção de Q5 — mas fica o registro para não induzir o aluno ao
> erro de chamar esse comportamento de "fake" caso a distinção apareça em prova/discussão.

---

### Q6 — O que tornou possível trocar o `Narrador` real pelo dublê?
**Correta:** *"A `Partida` receber o narrador pelo construtor (a injeção de dependência — o DIP da Aula 5)."*

**Por quê:** em `partida.py`, `def __init__(self, narrador)` recebe o narrador **de fora** e guarda
em `self.narrador`. Como a `Partida` não cria o narrador por conta própria, o teste pode **injetar**
qualquer objeto que tenha `gol(time)` — inclusive o dublê. É a **injeção de dependência** (DIP,
Aula 5) que torna a peça substituível/testável. O `pytest`, o número de arquivos e a cobertura
não têm relação com essa substituição.

---

### Q7 — Para que serve um dublê (test double)?
**Correta:** *"Entrar no lugar de uma peça real (e-mail, banco, narrador) para o teste não disparar
o efeito de verdade."*

**Por quê:** um dublê ocupa o lugar de uma dependência real (que teria efeito colateral — mandar
e-mail, gravar no banco, narrar ao vivo) para que o teste rode **rápido, isolado e sem efeito real**.
É exatamente o papel do `FakeNarrador` frente ao `Narrador` (que faria `print`). Deixar o código
"bonito", substituir o `pytest` ou "medir cobertura" não são funções de um dublê.

---

### Q8 — Sobre cobertura de testes
**Correta:** *"Cobertura mostra quanto do código os testes exercitam — mas alta cobertura não garante
testes bons."*

**Por quê:** cobertura mede **quanto** do código foi executado pelos testes; não mede a **qualidade**
das verificações. Dá para ter 100% de cobertura com `assert` fracos e ainda ter bugs — por isso
**100% não garante ausência de bugs**. Cobertura também não é "número de testes que falharam", e
**menos** cobertura não é melhor.

---

### Q9 — Base da pirâmide de testes
**Correta:** *"Testes de unidade (muitos, rápidos, isolados)."*

**Por quê:** na pirâmide, a **base larga** são os **testes de unidade** — muitos, rápidos e isolados
(como os de `resultado()`). Acima vêm menos testes de integração e, no topo, poucos testes de ponta
a ponta (e2e). Testes manuais não formam a base da pirâmide automatizada.

---

### Q10 — (Justificativa) Por que testes automáticos deixam mudar o código com menos medo?
**Tipo:** resposta aberta. Aceitar qualquer redação com suas palavras que contenha a ideia central.

**Resposta-modelo (curta):**
> Porque, ao mexer no código, é só rodar os testes de novo: se algo que funcionava quebrou, um teste
> **falha na hora** e aponta onde. Essa "rede de segurança" (regressão) dá confiança para alterar,
> refatorar ou acrescentar coisas sabendo que você seria avisado se estragasse algo.

**Pontos que valem (basta a ideia principal):**
- Os testes avisam **automaticamente/na hora** se uma mudança quebrou algo (regressão).
- Funcionam como **rede de segurança**: mais confiança para refatorar/alterar.
- Evitam ter de **reconferir tudo à mão** a cada mudança.

---

## Resumo do gabarito (só as objetivas)
**Q1** função com `assert` · **Q2** falha (2+2≠5) · **Q3** empate · **Q4** Arrange→Act→Assert ·
**Q6** injeção pelo construtor (DIP) · **Q7** substitui peça real (sem efeito) ·
**Q8** cobertura = quanto exercita, não garante qualidade · **Q9** testes de unidade.
**Q5** e **Q10** são justificativas — corrigir pela **ideia central** (modelos acima).

## Ambiguidades sinalizadas
1. **Q5 — nome "Fake" × papel de "spy" (a mais relevante).** A classe chama-se `FakeNarrador`,
   mas o teste verifica o que ela **registrou** (`fake.gols_narrados == ["Brasil"]`): esse é o
   comportamento de **spy** (anota as chamadas para o teste conferir), não de um *fake* estrito.
   A **pergunta de Q5 não cobra** essa classificação, então não altera a nota; mas o professor deve
   ter cuidado ao comentar, para não reforçar "anota → fake". Se a distinção stub/spy/fake/mock for
   cobrada em outro item/prova, a resposta certa para "dublê que anota o que foi chamado" é **spy**.
2. **Q5 e Q10 são abertas.** Não há alternativa única; correção por presença da **ideia central**.
   Sugestão: crédito cheio com ≥1 dos pontos listados, expresso com as próprias palavras.
3. **Nenhuma inconsistência** encontrada nas objetivas: cada uma tem exatamente **uma** alternativa
   correta, ancorada no material (`placar.py`, `partida.py`, `test_placar.py`, imagens das questões).
