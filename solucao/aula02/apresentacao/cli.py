# Camada de apresentação: SÓ entrada e saída. (PRONTA — não precisa mexer)
CARDAPIO = [("X-Burguer", 18.0), ("Refrigerante", 6.0), ("Batata frita", 12.0)]


def menu(service) -> None:
    while True:
        print("\n1-Novo  2-Adicionar item  3-Fechar  4-Listar  0-Sair")
        op = input("Opção: ")
        if op == "1":
            pedido = service.criar_pedido(input("Cliente: "))
            print(f"Pedido {pedido.id} criado.")
        elif op == "2":
            pid = int(input("ID do pedido: "))
            for i, (nome, preco) in enumerate(CARDAPIO, 1):
                print(f"{i}- {nome} (R${preco:.2f})")
            nome, preco = CARDAPIO[int(input("Item: ")) - 1]
            service.adicionar_item(pid, nome, preco, int(input("Qtd: ")))
            print("Item adicionado.")
        elif op == "3":
            total = service.fechar_pedido(int(input("ID do pedido: ")))
            print(f"Total: R${total:.2f}")
        elif op == "4":
            for p in service.repo.listar():
                estado = "fechado" if p.fechado else "aberto"
                print(f"#{p.id} {p.cliente} — {estado} — R${p.total():.2f}")
        elif op == "0":
            break
