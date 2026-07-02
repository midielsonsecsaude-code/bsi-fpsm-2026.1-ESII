from modelos.item import Item
from modelos.pedido import Pedido


class PedidoService:
    """Camada de serviço: as regras de negócio. Recebe o repositório (injeção)."""

    def __init__(self, repo) -> None:
        self.repo = repo

    def criar_pedido(self, cliente: str) -> Pedido:
        # cria um Pedido com o próximo id e salva no repositório
        pedido = Pedido(id=self.repo.proximo_id(), cliente=cliente)
        self.repo.salvar(pedido)
        return pedido

    def adicionar_item(self, pedido_id: int, nome: str, preco: float, qtd: int) -> None:
        # busca o pedido; se inválido ou fechado, é erro de negócio
        pedido = self.repo.buscar(pedido_id)
        if pedido is None or pedido.fechado:
            raise ValueError("Pedido inválido ou já fechado")
        pedido.adicionar(Item(nome=nome, preco=preco, qtd=qtd))

    def fechar_pedido(self, pedido_id: int) -> float:
        # busca o pedido, marca como fechado e devolve o total
        pedido = self.repo.buscar(pedido_id)
        if pedido is None:
            raise ValueError("Pedido inválido")
        pedido.fechado = True
        return pedido.total()
