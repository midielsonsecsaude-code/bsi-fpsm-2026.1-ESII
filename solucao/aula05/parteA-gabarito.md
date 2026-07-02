# Gabarito de referência — Atividade 5, Parte A (Questionário)

**Aula 5 — LSP, ISP e DIP · Injeção de dependência · Fakes**
**Valor:** 0,7 ponto · **13 questões** (4 blocos)

> **Uso deste documento.** Chave de respostas de referência, publicada **após o prazo**
> de entrega. As respostas objetivas são de correção direta (alternativa correta).
> Nas questões de justificar, a "resposta-modelo" é um teto de referência: aceite
> qualquer redação do aluno que, com as próprias palavras, expresse a mesma ideia —
> não exija as mesmas palavras. Correção é crítica; leia as observações de ambiguidade
> ao final de cada questão quando houver.

---

## BLOCO 1 — O problema: testar é difícil assim

### Q1 — objetiva
**Correta:** *"Porque cria o servidor de e-mail e o repositório por dentro — testá-lo mandaria e-mail de verdade."*

**Por quê.** Na imagem, o `__init__` faz `self.repo = RepositorioAssinantes()` e
`self.enviador = ServidorSMTP()` — o serviço **instancia as dependências dentro de si**.
Como o `ServidorSMTP` é o e-mail "de verdade", rodar um teste chamaria `enviar_edicao`
e dispararia envio real; não há como colocar uma peça de mentira no lugar. As demais
alternativas são falsas: número de linhas, `for`/`while` e ausência de banco não têm
relação com a dificuldade de testar.

### Q2 — justificar (1–2 frases)
**Resposta-modelo.** No lugar do servidor de e-mail real, queremos colocar um
**objeto "de mentira" (fake/dublê)** que tenha o mesmo método `enviar(...)` mas
**só anote** para quem enviaria, sem mandar e-mail de verdade. Assim o teste roda
rápido, sem efeito colateral, e podemos **verificar** o que o serviço faria.

*Aceitar como corretas:* respostas que mencionem "fake", "mock", "dublê",
"objeto falso", "simulador" ou "um enviador que só finge/registra" **desde que**
apareça a razão: **não mandar e-mail real / poder conferir o resultado**.
*Não aceitar:* "colocar outro servidor SMTP", "usar o banco de dados", ou respostas
que não digam por quê.

---

## BLOCO 2 — LSP: a subclasse honra o contrato

### Q3 — objetiva
**Correta:** *"que uma subclasse deve poder substituir a classe-mãe sem alterar o comportamento esperado."*

**Por quê.** É a definição do Princípio da Substituição de Liskov: onde se espera a
mãe, deve ser possível usar a filha sem surpresas de comportamento. As outras confundem
LSP com "toda classe deve herdar" (falso), com o ISP ("interfaces pequenas") e com o
DIP ("receber por construtor").

### Q4 — objetiva
**Correta:** *"Porque ao mudar a largura ele muda também a altura — e quem usa um Retângulo não espera isso."*

**Por quê.** A imagem mostra `set_largura(10)`: no Retângulo(5,3) só a largura muda
(alt continua 3, `area = 30`, ok); no Quadrado(5,5) a altura **muda sozinha** para 10,
e `area()` dá 100 quando quem usava um Retângulo esperava 10×5 = 50. A subclasse
**quebra a promessa** do método herdado — isso viola o LSP. A alternativa "não é um
retângulo na vida real" é a armadilha clássica: o LSP é sobre **comportamento do
contrato no código**, não sobre a intuição do mundo real; "falta `area()`" e "Python
não permite herança" são factualmente falsas.

### Q5 — objetiva
**Correta:** *"a filha exija MAIS, entregue MENOS, ou lance um erro novo que a mãe não lançava."*

**Por quê.** Essas três coisas quebram a substituibilidade (pré-condição mais forte,
pós-condição mais fraca, exceção nova) — logo, **NÃO** podem acontecer se a filha
respeita o LSP. As demais (ter o mesmo método, ser usada no lugar da mãe, herdar da
mãe) são justamente o que se **espera** de uma subclasse bem-comportada.

---

## BLOCO 3 — ISP: não dependa de métodos que não usa

### Q6 — objetiva
**Correta:** *"Ela exige métodos demais (anexar, agendar, formatar HTML) que nem todo enviador usa."*

**Por quê.** A imagem mostra a interface `Enviador(ABC)` marcada como "GORDA", com
quatro métodos abstratos: `enviar`, `anexar_arquivo`, `agendar`, `formatar_html`.
O ISP diz que ninguém deve ser **obrigado** a depender de métodos que não usa; uma
interface tão grande força implementações a cumprir coisas que não fazem sentido para
elas. "Poucos métodos" é o oposto do problema; "não herda de `ABC`" é falso (ela herda);
"arquivo errado" não tem a ver com o ISP.

### Q7 — objetiva
**Correta:** *"Lança `NotImplementedError` — é forçado a 'fingir' que faz algo que não faz."*

**Por quê.** No código do `EnviadorSMS`, apenas `enviar` faz algo real (`print`);
`anexar_arquivo`, `agendar` e `formatar_html` fazem `raise NotImplementedError`
(comentados como "SMS nao anexa!", "nem agenda!", "nem formata HTML!"). Ou seja, a
interface gorda **obrigou** o SMS a implementar métodos que não fazem sentido para ele.
As outras alternativas (retorna 0, manda SMS, chama SMTP) não correspondem ao código.

### Q8 — justificar (1–2 frases)
**Resposta-modelo.** O ISP propõe **quebrar a interface gorda em interfaces menores e
específicas** (por exemplo, uma só para `enviar`, outra para `anexar`, outra para
`agendar`…), de modo que cada classe implemente **só o que realmente usa** — o SMS
implementaria apenas o "enviar" e não seria forçado a `NotImplementedError`.

*Aceitar como corretas:* "separar/dividir/quebrar em interfaces menores",
"várias interfaces pequenas", "cada classe implementa só o que precisa".
*Não aceitar:* "adicionar mais métodos", "apagar o SMS", "usar herança múltipla" sem
a ideia de separar responsabilidades, ou respostas que só reafirmam o problema sem
apontar a separação.

---

## BLOCO 4 — DIP: dependa de abstrações (e poder testar)

### Q9 — objetiva
**Correta:** *"O serviço (alto nível) depende direto dos detalhes (e-mail, repositório), em vez de uma abstração."*

**Por quê.** O diagrama mostra `ServicoNewsletter (alto nível)` com setas "cria e
depende de" apontando direto para `ServidorSMTP` e `RepositorioAssinantes` (os
detalhes/baixo nível). O DIP diz que o alto nível **não** deve depender direto dos
detalhes, e sim de uma **abstração**. As demais (métodos demais, faltam testes, código
duplicado) não são o que a figura mostra.

### Q10 — objetiva
**Correta:** *"Ele recebe o repositório e o enviador por construtor, em vez de criá-los por dentro."*

**Por quê.** Na imagem "com DIP", o `__init__(self, repo, enviador)` **recebe de fora**
(`self.repo = repo`, `self.enviador = enviador`) — não há mais `= RepositorioAssinantes()`
nem `= ServidorSMTP()` dentro. Isso é a **injeção de dependência**. As outras (criar
mais objetos por dentro, ganhar `if/elif`, virar função solta) contrariam a figura.

### Q11 — objetiva
**Correta:** *"Verificar para quem a edição iria, sem mandar e-mail de verdade."*

**Por quê.** O `FakeEmail` tem uma lista `self.enviados` e, em `enviar`, faz
`self.enviados.append(para)` ("só anota, não manda"). Depois do `enviar_edicao("teste")`,
`print(enviador.enviados)` mostra `['ana@exemplo.com', 'bia@exemplo.com']` — dá para
**conferir os destinatários sem envio real**. "Mais rápido" até é efeito colateral, mas
não é o que o fake **permite** verificar; acessar banco real e trocar o repositório por
SQL não têm relação.

### Q12 — associação
**Correta:**

- **( b ) LSP** — a subclasse honra o contrato da classe-mãe
- **( c ) ISP** — interfaces pequenas, sem métodos que não se usa
- **( a ) DIP** — depender de uma abstração, não dos detalhes

**Por quê.** LSP = substituibilidade/contrato (b); ISP = interfaces enxutas (c);
DIP = depender de abstração, não de detalhe (a). Correção "tudo ou nada" por letra:
o par certo é LSP→b, ISP→c, DIP→a.

### Q13 — justificar (2–3 frases)
**Resposta-modelo.** Aplicar o DIP faz o serviço **receber** o repositório e o enviador
por construtor, em vez de criá-los por dentro. Como quem entrega essas peças é o código
de fora, **no teste eu posso entregar um `FakeEmail`** (que só anota, não manda) no lugar
do `ServidorSMTP`. Assim o `enviar_edicao` roda de verdade, mas **sem disparar e-mail
real**, e ainda dá para conferir na lista `enviados` para quem a edição iria.

*Elementos esperados (aceitar se aparecerem, em qualquer redação):*
1. o serviço **recebe** as dependências por fora (não cria dentro);
2. por isso é possível **trocar/injetar** o enviador real por um **fake**;
3. resultado: testar **sem mandar e-mail de verdade** (e/ou poder verificar o envio).
*Correção sugerida:* uma justificativa que traga (1)+(2)+(3) é resposta cheia;
com (2)+(3) já demonstra o entendimento central. Não aceitar respostas que só repitam
"é mais fácil testar" sem explicar o mecanismo (receber → trocar por fake).

---

## Observações de ambiguidade e notas de correção

1. **Divergência imagem × código-fonte do repositório (não afeta a resposta).**
   A imagem da Q1 (`q-servico_v1.png`) mostra o `enviar_edicao` percorrendo os
   assinantes e chamando `self.enviador.enviar(a.email, texto)` **sem** o filtro
   `if a.pode_receber()`. O arquivo real `servico/newsletter.py` do repositório **tem**
   esse filtro. O enunciado avisa que "tudo o que você precisa está aqui dentro" (nas
   imagens), então a correção deve se basear **na imagem**. Essa diferença **não muda**
   a alternativa correta da Q1 (o problema é criar as dependências por dentro).

2. **Q2 — abertura de vocabulário.** O aluno pode nomear a peça de várias formas
   (fake, mock, dublê, stub, "objeto falso", "simulador"). Todas valem **desde que** a
   justificativa contenha a razão: não mandar e-mail real / poder verificar o resultado.
   O termo técnico usado na aula é **fake**; não penalizar quem escrever "mock/dublê".

3. **Q11 — distrator "mandar e-mail mais rápido".** É verdade que o fake é mais rápido,
   mas isso **não** é o que ele "permite verificar". A resposta correta é a que fala em
   **conferir os destinatários sem envio real**. Se algum aluno argumentar velocidade,
   trata-se de erro de foco: a alternativa marcada precisa ser a de verificação sem envio.

4. **Q12 — forma de marcação.** O enunciado pede "escreva a letra no parêntese".
   Considerar corretas também respostas que "liguem" LSP–b, ISP–c, DIP–a por setas,
   desde que o pareamento esteja certo.

5. **Questões objetivas restantes (Q3, Q4, Q5, Q6, Q7, Q9, Q10).** Sem ambiguidade;
   há uma única alternativa correta em cada, conforme acima.
