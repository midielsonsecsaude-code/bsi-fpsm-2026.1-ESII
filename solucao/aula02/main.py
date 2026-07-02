# Ponto de entrada (composition root): cria e conecta as camadas. (PRONTO)
from apresentacao.cli import menu
from repositorio.pedido_repo import PedidoRepo
from servico.pedido_service import PedidoService


def main() -> None:
    repo = PedidoRepo()
    service = PedidoService(repo)
    menu(service)


if __name__ == "__main__":
    main()
