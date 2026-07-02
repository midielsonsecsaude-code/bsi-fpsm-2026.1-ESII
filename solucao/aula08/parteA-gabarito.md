# Gabarito — Atividade 8, Parte A: Questionário sobre TDD

> **Chave de respostas de referência — publicação após o prazo.**
> Documento de correção da **Parte A** (questionário, 1,0 ponto) da Aula 8 (TDD: ciclo Red→Green→Refactor).
> São **10 questões**: **8 objetivas** (Q1–Q4, Q6–Q9) e **2 de justificativa** (Q5, Q10).
> As justificativas (Q5, Q10) têm **resposta-modelo**: aceite qualquer redação do aluno que expresse a mesma ideia, com suas próprias palavras. Não exija as palavras exatas.

Referência de comportamento do `validar(senha)` (arquivo final, já refatorado):

```python
validar("Abcdef12")  == []                                   # aprovada
validar("Ab1")       == ["precisa de pelo menos 8 caracteres"]
validar("Abcdefgh")  == ["precisa de um número"]
validar("abcdefg1")  == ["precisa de uma letra maiúscula"]
validar("abc")       == ["precisa de pelo menos 8 caracteres",
                         "precisa de um número",
                         "precisa de uma letra maiúscula"]
```

`[]` (lista vazia) = senha aprovada. A lista devolvida traz **os problemas** encontrados.

---

### Q1. O que é TDD? — Objetiva

**Resposta correta: "Escrever o teste primeiro e depois o código que faz ele passar."**

Por quê: TDD (Test-Driven Development / Desenvolvimento Guiado por Testes) é justamente **inverter a ordem**: o teste vem antes do código de produção. As outras opções descrevem "testar no fim (ou nunca)", uma ferramenta mágica que conserta bugs sozinha, e testar só quando o cliente reclama — nenhuma é TDD.

---

### Q2. RED com a função ainda inexistente — Objetiva

**Resposta correta: "a função `validar` ainda não existe — e esse é o RED esperado do TDD (o teste falha porque o código nem foi escrito)."**

Por quê: a imagem mostra `ImportError: cannot import name 'validar' from 'senha'`. O teste foi escrito **antes** da função; ao rodar, ele falha porque não há o que importar. Esse é o passo **RED** — a falha é esperada e intencional, não um defeito do teste nem do `pytest`.

---

### Q3. Ordem do ciclo — Objetiva

**Resposta correta: "Red → Green → Refactor."**

Por quê: primeiro o teste falha (**RED**), depois você escreve o mínimo para ele passar (**GREEN**), e só então melhora a forma do código sem quebrar os testes (**REFACTOR**). As demais ordens embaralham os passos.

---

### Q4. O MÍNIMO no passo GREEN — Objetiva

**Resposta correta: "adicionar a regra que verifica se a senha tem um número."**

Por quê: no GREEN o "mínimo" é o **mínimo que faz o novo teste passar SEM quebrar os que já passavam**. Trocar o `return` por `return ["precisa de um número"]` (resposta fixa) faria o teste do número passar, mas **quebraria** `test_senha_boa_nao_tem_problemas` (a senha boa deixaria de devolver `[]`) — por isso está errado. Apagar a regra do tamanho quebraria o teste da senha curta e não tem relação com o número. "Não dá para fazer" é falso.

> Observação para o corretor: a alternativa da "resposta fixa" é a pegadinha do **fake it**; aqui ela não serve porque já existe um segundo teste (a senha boa) que a barra. É exatamente o contraste que a Q5 explora.

---

### Q5. Por que um único teste não garante correção? — Justificativa

**Resposta-modelo:** Com **só um teste**, o código pode "colar na resposta" daquele caso específico — aqui `return 60` passa só porque o único teste espera 60, mas a função **não soma nada**. Para forçar a soma de verdade, faltaria **pelo menos mais um teste com outros números / outro total esperado** (ex.: `total([1, 2]) == 3`): com dois casos que dão resultados diferentes, devolver um valor fixo não passa mais, e o código é obrigado a somar.

Aceitar quando o aluno disser, com suas palavras: (a) que um só teste é fácil de enganar / o código pode "chutar" a resposta certa; **e** (b) que outro(s) teste(s) com valores diferentes forçariam o código a somar de fato. Se citar só (a) sem indicar a saída (mais testes / casos variados), considerar **parcial**.

---

### Q6. Trocar `if`s por tabela + `for` — Objetiva

**Resposta correta: "um refactor: muda a FORMA do código, não o comportamento — e os testes provam que nada quebrou."**

Por quê: refatorar é mudar a **estrutura interna** mantendo o **mesmo comportamento**. As três regras continuam sendo as mesmas (tamanho, número, maiúscula) e os testes continuam passando — isso é a definição de refactor. Não é bug (o comportamento não mudou), não é recomeçar do zero, e não é escrever teste novo.

---

### Q7. Um teste ficou vermelho após "limpar" o código — Objetiva

**Resposta correta: "que a rede de testes pegou o erro NA HORA — por isso refatorar com testes é seguro."**

Por quê: a imagem mostra `test_senha_curta_avisa` falhando — `validar("Ab1")` devolveu `[]` em vez de `["precisa de pelo menos 8 caracteres"]`, sinal de que a "limpeza" removeu/alterou uma regra sem querer. O `pytest` apontou a mudança de comportamento **imediatamente**. É essa a proteção que os testes dão. As outras opções ("pytest é chato", "código perfeito", "apagar o teste") ignoram o que o vermelho está avisando.

---

### Q8. Caso-limite: `media` de lista vazia — Objetiva

**Resposta correta: "é um caso-limite: escrever um teste para a lista vazia pega o bug e fica de guarda para ele não voltar (teste de regressão)."**

Por quê: `sum(notas) / len(notas)` divide por `len([]) == 0`, ou seja, quebra (ZeroDivisionError) com lista vazia. Um teste para esse caso-limite **expõe o bug** e depois vira **rede de proteção** (regressão) para que o defeito não volte. "Lista vazia nunca acontece" e "não usar listas" fogem do problema; "deixa o código mais lento" é irrelevante.

---

### Q9. O passo GREEN (escrever o mínimo) — Objetiva

**Resposta correta: "é de propósito: você escreve só o necessário para o teste atual passar; são os próximos testes que forçam o resto."**

Por quê: escrever o mínimo é uma **decisão consciente** do TDD, não trapaça nem preguiça. Cada nova exigência entra como um novo teste, que por sua vez força mais código. Não é "já escrever tudo de uma vez", não é pular teste e não é refatorar (refatorar é o passo seguinte, sem mudar comportamento).

---

### Q10. Por que testes escritos antes deixam mudar/limpar o código com menos medo? — Justificativa

**Resposta-modelo:** Porque os testes funcionam como uma **rede de segurança**: depois de mexer/limpar o código, é só rodar o `pytest`; se tudo continua **verde**, o comportamento foi preservado, e se algo **fica vermelho**, você descobre o estrago **na hora** e sabe exatamente onde. Assim dá para melhorar o código sem o medo de quebrar algo sem perceber.

Aceitar quando o aluno disser, com suas palavras, a ideia de **rede de proteção / retorno rápido**: rodar os testes confirma que nada quebrou (ou avisa na hora se quebrou), então você mexe com confiança. Ligações com a Q7 (o vermelho aparece na hora) são bem-vindas.

---

## Grade sugerida (1,0 ponto no total)

- 10 questões com peso igual: **0,10 ponto cada**.
- **Objetivas (Q1–Q4, Q6–Q9):** certo/errado pela alternativa marcada.
- **Justificativas (Q5, Q10):** 0,10 se a ideia central aparece (mesmo com outras palavras); **0,05 (parcial)** se o aluno toca no problema mas não aponta a saída; 0 se em branco ou sem relação.
- Conforme a Parte A, **entregar esta parte já garante 1,0**; a **Parte B** (repositório) leva ao 1,5 cheio.

## Notas de correção e ambiguidades

- **Nenhuma ambiguidade nas objetivas.** Q1–Q4, Q6–Q9 têm exatamente uma alternativa correta, e todas foram conferidas contra o código-fonte (`senha.py` / `test_senha.py`) e contra as imagens de cada questão.
- **Q4** é a questão mais sutil: a alternativa "resposta fixa" (`return ["precisa de um número"]`) é atraente para quem lembra do *fake it*, mas está **errada** porque quebra o teste da senha boa. Aceite como correta **apenas** "adicionar a regra que verifica se a senha tem um número". Vale conferir se algum aluno justificou espontaneamente por que a resposta fixa não serve — é sinal de entendimento.
- **Q5 e Q10** são abertas: corrija pela **ideia**, não pela redação. Os critérios parciais estão indicados em cada uma.
- **Q7** — a imagem mostra o teste `test_senha_curta_avisa` falhando porque a regra do tamanho foi perdida na "limpeza"; isso reforça a alternativa correta (a rede de testes pegou o erro na hora) e conecta diretamente com a Q10.
