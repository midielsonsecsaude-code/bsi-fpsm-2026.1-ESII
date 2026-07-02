from modelos.pedido import Pedido


class PedidoRepo:
    """Camada de persistência: guarda e busca pedidos (em memória)."""

    def __init__(self) -> None:
        self._pedidos: list[Pedido] = []

    def salvar(self, pedido: Pedido) -> None:
        # guarda o pedido na lista (sem duplicar)
        if pedido not in self._pedidos:
            self._pedidos.append(pedido)

    def buscar(self, pedido_id: int):
        # devolve o pedido com esse id (ou None se não achar)
        for pedido in self._pedidos:
            if pedido.id == pedido_id:
                return pedido
        return None

    def listar(self) -> list:
        # devolve todos os pedidos guardados
        return self._pedidos

    def proximo_id(self) -> int:
        # próximo id: quantidade atual + 1 (igual ao monolito)
        return len(self._pedidos) + 1
