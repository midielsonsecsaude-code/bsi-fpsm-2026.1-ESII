# Gabarito de referência — Atividade 2, Parte A (Questionário)

> **Chave de respostas oficial.** Divulgada **após o prazo** de entrega no SIGAA.
> Refere-se ao arquivo `aula02/atividade/at02-parteA.md` (15 questões, 0,7 ponto).
> As justificativas abaixo são **respostas-modelo**: aceite qualquer redação do aluno
> que expresse a mesma ideia, ancorada no código/documentos da Aula 2.
>
> Fontes de apoio: `bsi-fpsm-2026.1-ESII/aula02/pedidos.py`,
> `docs/requisitos.md`, `docs/projeto.md`, `docs/visao.md` e o `template/` em camadas.

---

## BLOCO 1 — Arquitetura e camadas

### Q1 (marcar) — O total é calculado em dois lugares do `pedidos.py`. Que problema é esse?
**Resposta correta:** **A mesma regra de negócio está duplicada — se a regra mudar, há dois lugares para corrigir.**
**Justificativa:** o total aparece em `fechar_pedido` (`total += item["preco"]*item["qtd"]`, linhas 48–50) e em `listar_pedidos` (`sum(i["preco"]*i["qtd"] ...)`, linha 57); mudar a RN01 obrigaria a corrigir os dois trechos.

### Q2 (associação) — Ligue cada camada à sua responsabilidade
**Resposta correta:**
- Apresentação → **(c)** a tela: menu, ler o que o usuário digita, mostrar o resultado
- Serviço → **(b)** as regras de negócio (criar pedido, fechar, validar)
- Repositório → **(a)** guardar e buscar os pedidos (os dados)
- Domínio (`modelos`) → **(d)** as entidades do problema: `Pedido` e `Item`

**Justificativa:** é exatamente a divisão do `template/` — `apresentacao/cli.py` (tela), `servico/pedido_service.py` (regras), `repositorio/pedido_repo.py` (dados) e `modelos/pedido.py` + `modelos/item.py` (entidades).

### Q3 (marcar) — A regra de dependência em camadas diz que:
**Resposta correta:** **cada camada chama a de baixo, nunca a de cima (apresentação → serviço → repositório → domínio).**
**Justificativa:** a dependência é de cima para baixo; o domínio não conhece a tela (no `template`, o `cli.py` chama o `service`, e não o contrário).

### Q4 (justificar) — Em qual arquivo e método passa a morar o total, e por que é melhor que na tela?
**Resposta-modelo:** o cálculo passa a morar no **método `total()` da classe `Pedido`**, no arquivo **`modelos/pedido.py`** (que soma o `subtotal()` de cada `Item`). É melhor porque a regra fica em **um único lugar** (sem duplicação) e **junto dos dados** que ela usa; a tela só pede `pedido.total()`, então a regra pode ser reaproveitada e testada sem depender do `input()`.
**Aceitar também:** menção a que `Item.total()`/`subtotal()` calcula preço×qtd e `Pedido.total()` soma tudo. O essencial é citar **`modelos/pedido.py`** e o **método `total()`**.

---

## BLOCO 2 — Requisitos não funcionais (RNF) e ADR

### Q5 (associação) — Ligue cada RNF à sua definição
**Resposta correta:**
- RNF03 — Manutenibilidade → **(b)** adicionar uma nova saída (ex.: um relatório) não deve exigir mexer em todo o sistema
- RNF04 — Testabilidade → **(c)** a regra (ex.: o total) deve poder ser testada sem depender do `input()` do usuário
- RNF05 — Extensibilidade → **(a)** trocar a forma de guardar os dados (lista → arquivo → banco) não deve impactar as regras

**Justificativa:** é a redação literal de `docs/requisitos.md`, seção 2 (RNF03, RNF04, RNF05).

### Q6 (marcar) — Por que o código não atende o RNF04 (testabilidade)?
**Resposta correta:** **Porque a regra do total está dentro de uma função que chama `input()` — não dá para testá-la sem simular o usuário digitando.**
**Justificativa:** em `fechar_pedido` o `input("ID do pedido: ")` e o cálculo do total estão na mesma função; para testar o total seria preciso simular a digitação (o que a observação do analista no RNF04 confirma).

### Q7 (completar) — Complete a Decisão do ADR com as 4 camadas na ordem da regra de dependência
**Resposta correta:**
> Adotar arquitetura em **camadas** , com dependência de cima para baixo:
> `apresentacao/  →  servico/  →  repositorio/  →  modelos/` (domínio)

**Justificativa:** é a ordem da regra de dependência e a estrutura de pastas do `template/`. Aceitar "domínio" como sinônimo de `modelos/` na última posição.

### Q8 (marcar) — Um ADR serve para registrar:
**Resposta correta:** **a decisão de arquitetura, o contexto que a motivou e suas consequências (o "porquê").**
**Justificativa:** é a definição de ADR (Nygard); em `docs/projeto.md` a "decisão pendente" de arquitetura é o que vai para o ADR.

### Q9 (justificar) — Uma desvantagem de dividir o sistema em camadas
**Resposta-modelo:** aumenta a **complexidade inicial / o número de arquivos** — uma operação simples passa por várias camadas (tela → serviço → repositório → domínio), então há mais código para escrever e mais indireção para entender do que num arquivo só.
**Aceitar também:** mais lento de programar no começo; para uma mudança pequena às vezes é preciso tocar em várias camadas; curva de aprendizado maior. Qualquer desvantagem real e coerente vale.

---

## BLOCO 3 — UML: lendo o diagrama de classes

### Q10 (marcar) — Na classe `Pedido`, `- itens`; o sinal `-` (menos) significa que o atributo é:
**Resposta correta:** **privado (de uso interno da classe).**
**Justificativa:** em UML, `-` denota visibilidade **privada** (`+` seria público, `#` protegido); não tem relação com número negativo.

### Q11 (marcar) — A multiplicidade `1 → *` entre `Pedido` e `Item` quer dizer:
**Resposta correta:** **um pedido pode ter vários itens (e cada item está num pedido).**
**Justificativa:** `*` = muitos; um `Pedido` agrega vários `Item` (no código, `itens: list[Item]`), enquanto o `1` do lado do pedido indica um pedido por conjunto de itens.

### Q12 (justificar) — Complete a leitura da classe `Pedido`
**Resposta-modelo:** "Isto é um **Pedido**; ele **tem** um **cliente e uma lista de itens** e **sabe** **calcular o próprio total** (método `total()`)."
**Aceitar também:** "tem" = cliente/itens (atributos); "sabe" = calcular o total / fechar o pedido (comportamento). O essencial é separar **dados (tem)** de **comportamento (sabe)**.

---

## BLOCO 4 — Princípios de projeto

### Q13 (marcar) — A tela recalcula o total lendo `i["preco"]` e `i["qtd"]` direto. Isso é exemplo de:
**Resposta correta:** **acoplamento alto — a tela depende dos detalhes internos de como o pedido é formado.**
**Justificativa:** em `listar_pedidos` a tela conhece a estrutura interna dos itens (chaves `preco`/`qtd`); se essa estrutura mudar, a tela quebra — o oposto de ocultamento de informação.

### Q14 (marcar) — A tela recebe o total sem saber como é calculado. Isso é exemplo de:
**Resposta correta:** **ocultamento de informação — a tela usa o serviço sem conhecer os detalhes internos.**
**Justificativa:** no `template`, o `cli.py` chama `service.fechar_pedido(...)` / `p.total()` e só recebe o número; o "como" fica escondido dentro do serviço/domínio.

### Q15 (justificar) — Escolha um princípio (coesão / acoplamento / ocultamento) e mostre, citando um arquivo, onde a versão em camadas fica melhor
**Resposta-modelo (qualquer um dos três serve; exige citar um arquivo):**
- **Coesão:** `modelos/pedido.py` — a classe `Pedido` cuida só do pedido e do seu `total()`; cada arquivo tem uma responsabilidade única, ao contrário do `pedidos.py`, que junta tela + regras + dados.
- **Acoplamento:** `apresentacao/cli.py` — a tela só conhece o `service` (chama `service.fechar_pedido(...)`) e não mexe nas chaves internas dos itens; no `pedidos.py`, a tela lia `i["preco"]`/`i["qtd"]` direto (acoplamento alto).
- **Ocultamento de informação:** `servico/pedido_service.py` (ou `modelos/pedido.py`) — quem chama recebe o total pronto e não sabe como ele é somado; o detalhe fica escondido dentro do serviço/domínio.

**Critério:** exige **(1)** nomear corretamente o princípio escolhido e **(2)** citar **um arquivo** da estrutura em camadas coerente com o princípio.

---

## Observações sobre ambiguidade

- **Q9, Q12, Q15** são abertas: aceite qualquer redação correta equivalente às respostas-modelo (ver "Aceitar também").
- **Q7:** aceitar tanto `modelos/` quanto a palavra "domínio" na 4ª posição — são o mesmo item nesta atividade.
- **Q15:** as três escolhas de princípio são igualmente válidas; corrigir pelo par (princípio nomeado + arquivo citado), não por qual princípio o aluno preferiu.
- As **objetivas (Q1, Q3, Q6, Q8, Q10, Q11, Q13, Q14)** têm resposta única e sem ambiguidade — cada distrator é claramente falso à luz do código/`requisitos.md`.
