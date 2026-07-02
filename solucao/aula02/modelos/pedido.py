from dataclasses import dataclass, field

from modelos.item import Item


@dataclass
class Pedido:
    """Entidade de domínio: um pedido e suas regras próprias."""
    id: int
    cliente: str
    itens: list[Item] = field(default_factory=list)
    fechado: bool = False

    def adicionar(self, item: Item) -> None:
        # acrescenta o item à lista de itens do pedido
        self.itens.append(item)

    def total(self) -> float:
        # soma o subtotal() de cada item
        return sum(item.subtotal() for item in self.itens)
