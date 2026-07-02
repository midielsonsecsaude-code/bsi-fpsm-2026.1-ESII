# acaiteria.py — sistema de pedidos de uma açaiteria de delivery (Aula 9)
#
# Este arquivo reúne os QUATRO padrões de projeto da aula, aplicados a UM
# sistema só, que foi crescendo passo a passo na apostila:
#
#   • Strategy  -> o cálculo da ENTREGA (moto, bicicleta, retirada)
#   • Factory   -> criar_entrega(nome): traduz um texto na estratégia certa
#   • Observer  -> os AVISOS quando o pedido é confirmado (cliente, cozinha, vendas)
#   • Facade    -> a classe Acaiteria: uma porta única que monta e usa tudo
#
# Tudo é texto no terminal (print) — sem banco, sem internet — para focar no
# desenho do código, não na tecnologia.


# ----------------------------------------------------------------------
# STRATEGY — cada forma de entrega é uma classe que sabe calcular o seu preço
# ----------------------------------------------------------------------
class Entrega:
    """Strategy (a abstrata). Toda forma de entrega promete um método preco()."""
    def preco(self, distancia_km):
        raise NotImplementedError("cada entrega concreta calcula o seu preço")


class EntregaMoto(Entrega):
    def preco(self, distancia_km):
        return 5.0 + 2.0 * distancia_km        # taxa fixa + por km


class EntregaBicicleta(Entrega):
    def preco(self, distancia_km):
        return 3.0 + 1.0 * distancia_km        # mais barata que a moto


class Retirada(Entrega):
    def preco(self, distancia_km):
        return 0.0                             # o cliente busca na loja: de graça


# ----------------------------------------------------------------------
# FACTORY — um lugar só que traduz um nome (texto) na estratégia de entrega
# ----------------------------------------------------------------------
def criar_entrega(nome):
    """Simple Factory: recebe um texto e devolve a estratégia de Entrega certa.

    Quem chama pede "moto" sem precisar conhecer a classe EntregaMoto.
    Se o nome não existir, avisa na hora com um erro claro.
    """
    opcoes = {
        "moto": EntregaMoto,
        "bici": EntregaBicicleta,
        "retirada": Retirada,
        "drone": EntregaDrone,
    }
    if nome not in opcoes:
        raise ValueError(f"forma de entrega desconhecida: {nome!r}")
    return opcoes[nome]()      # cria e devolve o objeto da classe escolhida


# ----------------------------------------------------------------------
# OBSERVER — vários avisos disparados quando o pedido é confirmado
# ----------------------------------------------------------------------
class Observador:
    """Observer (o abstrato). Todo observador reage a um evento com atualizar()."""
    def atualizar(self, evento):
        raise NotImplementedError("cada observador reage do seu jeito")


class AvisaCliente(Observador):
    def atualizar(self, evento):
        print(f"[SMS]     Oi {evento['cliente']}, seu açaí saiu! "
              f"Total R$ {evento['total']:.2f}")


class PainelCozinha(Observador):
    def atualizar(self, evento):
        print(f"[COZINHA] Preparar pedido de {evento['cliente']}")


class RegistroVendas(Observador):
    def atualizar(self, evento):
        print(f"[VENDAS]  +R$ {evento['total']:.2f} registrado")


# ----------------------------------------------------------------------
# FACADE — a Acaiteria: uma porta única que esconde a montagem das peças
# ----------------------------------------------------------------------
class Acaiteria:
    """Facade + composition root.

    Aqui (e só aqui) as peças concretas são criadas e ligadas: a lista de
    observadores começa montada. Quem usa a Acaiteria chama UMA operação
    simples — finalizar() — sem conhecer Strategy, Factory nem Observer.
    """
    def __init__(self):
        # composition root: o lugar onde as dependências concretas nascem
        self._observadores = [AvisaCliente(), PainelCozinha(), RegistroVendas()]

    def inscrever(self, observador):
        """Registra um novo aviso sem mexer no resto do sistema (Observer)."""
        self._observadores.append(observador)

    def _notificar(self, evento):
        for obs in self._observadores:
            obs.atualizar(evento)

    def finalizar(self, cliente, itens, metodo_entrega, distancia_km):
        """itens: lista com o preço de cada coisa do pedido (ex.: [12.0, 4.0])."""
        subtotal = sum(itens)
        entrega = criar_entrega(metodo_entrega)        # Factory -> Strategy
        total = subtotal + entrega.preco(distancia_km)
        evento = {"cliente": cliente, "total": total}
        self._notificar(evento)                        # Observer
        return total


# Rodar "python acaiteria.py" mostra o sistema funcionando de ponta a ponta.
if __name__ == "__main__":
    loja = Acaiteria()
    print("Pedido da Ana (2 itens, moto, 3 km):")
    total = loja.finalizar("Ana", [12.0, 4.0], "moto", distancia_km=3)
    print(f"=> total cobrado: R$ {total:.2f}")
