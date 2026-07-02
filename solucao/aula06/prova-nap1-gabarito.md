# Gabarito comentado — Prova Escrita 1 (NAP 1)

> Solução de referência, **divulgada após o encerramento da prova**. As respostas discursivas
> admitem redações diferentes; o que importa é o **conceito certo, referido ao código** de cada questão.

---

## Questão 1 — Qualidade de software e dívida técnica

**a) (0,3)** **Qualidade externa** é o que o **usuário percebe** — o sistema faz o que promete (aqui, o
cliente recebe o preço com o desconto certo), além de desempenho, usabilidade etc. **Qualidade interna** é a
**estrutura do código** que o usuário **não vê** — organização, legibilidade, manutenibilidade. O cliente
percebe a **externa** (o preço certo); o `0.9` fixo no código é um problema **só de qualidade interna**.

**b) (0,4)** Pelo quadrante de Fowler, a dívida é **deliberada** e **prudente**:
- **Deliberada** (não inadvertida): o autor **sabia** que estava tomando um atalho — o bilhete diz que
  "hardcodei… porque a tabela ainda não está no banco". Foi uma escolha consciente.
- **Prudente** (não imprudente): havia uma **razão legítima** (o BD de promoções ainda não existe) e um
  **plano de quitar** ("troco quando o BD existir"). Não foi descuido nem ignorância.

**c) (0,3)** **Manutenibilidade** (aceita-se também *configurabilidade/flexibilidade*): com o `0.9` fixo no
código, mudar a regra de desconto exige **editar o código-fonte e reimplantar**, em vez de alterar uma
configuração/tabela — qualquer ajuste de negócio vira mudança de programa.

---

## Questão 2 — Arquitetura em camadas, princípios de projeto e UML

**a) (0,4)** Dois princípios feridos:
- **Coesão** (baixa): a função é da **tela**, mas acumula a **regra do total** (soma das diárias + taxa de
  5%) — passa a ter mais de uma responsabilidade (exibir **e** calcular), quando deveria só mostrar.
- **Ocultamento de informação** (violado): a tela acessa a **estrutura interna** de `reserva`
  (`reserva['diarias']`, `diaria['valor']`) — conhece como o dado é montado por dentro; se essa estrutura
  mudar, a tela quebra. *(Também é defensável citar **acoplamento** — a tela fica acoplada ao formato do dado.)*

**b) (0,3)** **Regra de dependência:** as dependências apontam **numa só direção** — cada camada conhece
apenas a **camada seguinte, mais interna** (apresentação → serviço → repositório → domínio) e **nunca** o
contrário (as internas não conhecem as externas). O cálculo do total deve sair para a **camada de serviço**
(é regra de negócio).

**c) (0,3)** **(i)** O `-` em `- valor` indica visibilidade **privada** (atributo privado à classe).
**(ii)** A multiplicidade **`1 → *`** diz que **uma** `Reserva` tem **muitas** (zero ou mais) `Diaria` — a
reserva é composta de várias diárias.

---

## Questão 3 — SRP e OCP

**a) (0,3)** `calcular` acumula: **calcular o salário** (por tipo) **e** **mostrar na tela** (`print`) **e**
**gravar em arquivo** (`gravar_em_arquivo`). Três responsabilidades num método só.

**b) (0,4)** Viola o **OCP** porque, para um tipo novo (ex.: `"terceirizado"`), é preciso **abrir e editar**
o `if/elif` — e em **dois** métodos (`calcular` **e** `custo_anual`); o código **não está fechado para
modificação**. Com **polimorfismo**, cada tipo vira uma **classe** com o seu próprio cálculo (ex.: `Clt`,
`Pj`, `Estagio`, cada uma com um método `salario()`); no lugar do `if/elif`, chama-se `funcionario.salario()`.
Um tipo novo (`Terceirizado`) passa a funcionar **só criando uma classe nova** com o seu cálculo — **sem
editar** os métodos existentes.

**c) (0,3)** **DRY** (*Don't Repeat Yourself*): a regra de cada tipo, hoje **repetida** em `calcular` e
`custo_anual`, passa a morar **num único lugar** (a classe daquele tipo), eliminando a duplicação.

---

## Questão 4 — LSP, ISP e DIP

**a) (0,4)** Criar o `ServidorEmail` no construtor viola o **DIP**: a classe de alto nível
(`GeradorRelatorio`) depende **diretamente de uma implementação concreta**, em vez de depender de uma
**abstração** e receber a peça de fora. Fica **difícil de testar** porque toda execução usa o
`ServidorEmail` **real** — não há como trocá-lo por um dublê, então o teste **mandaria e-mail de verdade**
(lento e com efeito colateral). A **injeção de dependência** resolve: o `ServidorEmail` passa a **vir de
fora**, pelo construtor (`__init__(self, email)`) — no uso normal entra o real; no teste, entra um **fake**.

**b) (0,3)** Fere o **ISP (Segregação de Interfaces)** — a interface é "gorda" e força quem a implementa a
depender de métodos que não usa. O `EnviadorSMS` seria **forçado a implementar `anexar` e `agendar`** mesmo
sem saber fazê-los — deixando-os vazios ou lançando `NotImplementedError`, o cheiro clássico de ISP violado.

**c) (0,3)** Viola o **LSP (Substituição de Liskov)**: a subclasse **não pode substituir** a classe-base sem
quebrar o comportamento esperado — ela **recusa** (lança erro) entradas que o `ServidorEmail` original
**aceitava**, então quem espera um `ServidorEmail` não pode confiar em um `ServidorEmailUrgente` no lugar dele.

---

> **Boa prova!** *(gabarito de referência — Aula 6 / NAP 1)*
