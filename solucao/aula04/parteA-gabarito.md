# Aula 4 — Parte A (Questionário sobre OCP) — GABARITO DE REFERÊNCIA

> **Gabarito para publicação APÓS o prazo de entrega.**
> Chave de correção da **Parte A** (0,7 ponto). Referência para o professor/monitor e para
> os alunos conferirem depois de entregar. Baseado no código da **Bilheteria CineForma**
> (`aula04/servico/bilheteria.py`, `aula04/main.py`) e na hierarquia com OCP
> (`aula04/template/modelos/ingresso.py`, `aula04/template/servico/bilheteria.py`).
>
> **Total: 13 questões** — 9 objetivas (marcar) e 4 de justificar (Q3, Q7, Q11, Q13).
> Nas justificativas, aceite qualquer redação que expresse a ideia-chave descrita abaixo;
> não exija as palavras exatas.

---

## BLOCO 1 — O problema: decidir por tipo com `if/elif`

### Q1. O que há de frágil no cálculo com `if/elif`? *(marcar)*
**Resposta correta:** "O preço de cada tipo está escrito dentro do `if/elif`, e cada tipo novo obriga a mexer aqui."

**Justificativa:** No `vender`/`total` da v1.0, os preços (`20.0`, `10.0`, `35.0`) estão embutidos nos ramos do `if/elif`. Acrescentar um tipo (ex.: Cortesia) exige **editar essa função que já funcionava** — exatamente o que o OCP quer evitar. As demais são falsas: `if/elif` nem sempre é a melhor solução; o problema não é lentidão nem falta de banco de dados.

### Q2. Qual é o risco de o cálculo aparecer em dois lugares? *(marcar)*
**Resposta correta:** "Se um preço mudar, é preciso lembrar de corrigir nos dois lugares — esquecer um gera um bug silencioso."

**Justificativa:** O preço de cada tipo está repetido em `vender` **e** em `total` (linhas 9–14 e 25–30 de `bilheteria.py`). Se, por exemplo, a "vip" passar de 35 para 40 e o programador só corrigir um dos dois, o sistema fica inconsistente sem erro visível. É a violação do **DRY** (ver Q12). As outras opções (segurança, memória, cobrança em dobro) são falsas.

### Q3. *(justificar)* O que seria preciso fazer para acrescentar a **Cortesia** no código com `if/elif`?
**Resposta-modelo:** Seria preciso **editar as duas funções** (`vender` e `total`), acrescentando em cada uma um novo ramo `elif tipo == "cortesia": ...` com o preço da cortesia (0,00). Ou seja, é obrigatório **mexer em código já pronto e testado**, em mais de um lugar, correndo o risco de esquecer um deles.

**Aceitar como correto se o aluno mencionar, no mínimo:** que precisa **alterar o código existente** e/ou que precisa mexer em **dois lugares** (`vender` e `total`). Pontuar melhor quem cita os dois pontos.

---

## BLOCO 2 — A regra: OCP

### Q4. O que o OCP diz? *(marcar)*
**Resposta correta:** "aberto para extensão e fechado para modificação."

**Justificativa:** É a definição literal do Open/Closed Principle: pode-se **estender** (acrescentar comportamento, em geral uma classe nova) sem **modificar** o código existente. A primeira opção inverte os termos (erro clássico); as duas últimas são caricaturas.

### Q5. Ligar cada metade do OCP à sua descrição. *(associação)*
**Resposta correta:**
- Aberto para **extensão** → **(b)** poder acrescentar comportamento novo (em geral, uma classe nova)
- Fechado para **modificação** → **(a)** não editar o código que já está pronto e testado

**Justificativa:** "Extensão" = adicionar o novo (classe `Cortesia`); "modificação" = mexer no que já existe (o que se quer evitar). São pares diretos, sem ambiguidade.

### Q6. Por que "fechado para modificação" é uma boa ideia? *(marcar)*
**Resposta correta:** "mexer no código que já funciona é justamente o que mais introduz bugs."

**Justificativa:** Todo código já testado carrega risco de regressão quando alterado; deixá-lo intocado e estender por fora preserva o que funciona. As outras opções (rodar mais rápido, ser proibido editar, ninguém entender) são falsas.

### Q7. *(justificar)* Por que adicionar uma classe nova é mais seguro do que editar uma função testada?
**Resposta-modelo:** Porque a função que já funcionava **continua intacta** — não há como quebrá-la nem introduzir regressão nela. A classe nova é código isolado, que só acrescenta comportamento; se ela tiver bug, o problema fica contido nela, sem afetar o resto que já estava testado.

**Aceitar como correto se o aluno mencionar:** que **editar pode quebrar/introduzir bug** no que já funciona, enquanto **adicionar não mexe** no código existente (mantém o testado intacto / risco isolado).

---

## BLOCO 3 — A solução: polimorfismo (cada tipo, uma classe)

### Q8. Qual é o papel da classe base `Ingresso`? *(marcar)*
**Resposta correta:** "Ser o contrato: define que todo ingresso sabe responder `preco()` — cada tipo preenche do seu jeito."

**Justificativa:** Em `modelos/ingresso.py`, `Ingresso` declara `preco()` como o **contrato** que toda subclasse cumpre; cada tipo (`Inteira`, `Meia`, `VIP`) implementa `preco()` à sua maneira. A base **não** guarda os preços num só lugar (opção 1), nem mostra menu, nem substitui banco.

### Q9. Por que o `total` não precisa mais de `if/elif`? *(marcar)*
**Resposta correta:** "Porque cada ingresso é um objeto que responde `preco()` do seu jeito — o serviço chama sem saber o tipo concreto."

**Justificativa:** `total(venda)` é `sum(i.preco() for i in venda)`: o serviço chama `preco()` em cada objeto sem perguntar o tipo. Isso é **polimorfismo** — quem decide o valor é o próprio objeto. As outras opções (Python adivinha, preços iguais, `if/elif` escondido no `sum`) são falsas.

### Q10. O que significa `(Ingresso)` em `class Inteira(Ingresso):`? *(marcar)*
**Resposta correta:** "`Inteira` é um `Ingresso` (herda dele) e cumpre o mesmo contrato."

**Justificativa:** Os parênteses indicam **herança**: `Inteira` é subclasse de `Ingresso` e, por isso, também sabe responder `preco()`. Não é o contrário, não apaga a base e não é comentário.

---

## BLOCO 4 — Consequências e limites

### Q11. *(justificar)* Ao adicionar a `Cortesia`, o que **não** precisou ser modificado? Por que isso é o que o OCP promete?
**Resposta-modelo:** Não foi preciso modificar o **serviço** (`total()`), nem as classes já existentes (`Ingresso`, `Inteira`, `Meia`, `VIP`), nem quem já usava a hierarquia — bastou **acrescentar** a classe `Cortesia(Ingresso)`. Isso é exatamente o OCP: o sistema ficou **aberto para extensão** (nova classe) e **fechado para modificação** (nada do que já funcionava foi tocado).

**Aceitar como correto se o aluno citar:** que o `total()` / o serviço (e/ou as outras classes) **não foi alterado**, e amarrar isso à ideia de estender sem modificar.

### Q12. Como se chama o princípio de o preço de cada tipo morar num lugar só, acabando com a duplicação? *(marcar)*
**Resposta correta:** "DRY (*Don't Repeat Yourself* — 'não se repita')."

**Justificativa:** Concentrar cada preço numa única classe elimina a duplicação que existia entre `vender` e `total` (ver Q2) — é a definição de **DRY**. YAGNI, KISS e SOLID são outros conceitos (SOLID é o conjunto de que o próprio OCP faz parte, mas não é o nome da regra "não repita").

### Q13. *(justificar)* Descreva uma situação em que aplicar OCP (criar hierarquia de tipos) seria **exagero**.
**Resposta-modelo:** Quando há **poucos tipos e eles são estáveis** (não vão mudar nem crescer) — por exemplo, só existem "inteira" e "meia" e não se prevê nenhum tipo novo. Nesse caso, criar uma classe por tipo adiciona complexidade (mais arquivos/classes) sem ganho real; um `if/elif` simples resolve. Também vale para protótipos/scripts descartáveis, onde a flexibilidade não compensa o custo.

**Aceitar como correto qualquer situação plausível em que a extensão futura é improvável**, por exemplo: sistema pequeno/estável, protótipo descartável, número fixo de casos que nunca muda, prazo curto. **Rejeitar** respostas que apenas repitam "OCP é ruim" sem descrever uma situação concreta.

---

## Grade de correção sugerida (13 questões — 0,7 ponto)

- **Objetivas (Q1, Q2, Q4, Q5, Q6, Q8, Q9, Q10, Q12):** certo/errado pela alternativa.
- **Justificar (Q3, Q7, Q11, Q13):** aceitar redação livre que contenha a **ideia-chave** listada
  em cada questão; não exigir termos técnicos exatos (a turma escreve "com suas palavras").

## Observações / pontos de atenção do corretor

- **Q5 (associação):** confira que o aluno **não inverteu** as letras. É o erro mais provável.
- **Q4:** a alternativa errada mais atrativa é a que **inverte** ("aberto para modificação e fechado
  para extensão"); ela costuma pegar quem decorou a frase pela metade.
- **Q3 vs Q11:** são complementares (o "antes" com `if/elif` e o "depois" com classes). Se o aluno
  acertar a lógica numa e errar na outra, corrija cada uma pelo seu próprio critério.
- **Q13:** por ser aberta, há várias respostas defensáveis; o critério é **descrever uma situação
  concreta** de baixa probabilidade de extensão, não a "resposta certa" única.

## Ambiguidades sinalizadas

Nenhuma questão objetiva é ambígua: em todas há uma única alternativa correta ancorada no código
ou na definição do OCP. A única questão com múltiplas respostas legitimamente defensáveis é a
**Q13** (aberta por natureza) — qualquer situação plausível de tipos estáveis/poucos/descartáveis
deve ser aceita, conforme o critério acima.
