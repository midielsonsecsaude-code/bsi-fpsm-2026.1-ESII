# main.py — ponto de entrada (solução da Parte B — OCP)
from modelos.ingresso import Inteira, Meia, VIP, Cortesia
from servico.bilheteria import total


if __name__ == "__main__":
    # Cortesia() foi incluída na venda SEM alterar total() nem as classes antigas.
    venda = [Inteira(), Meia(), VIP(), Cortesia()]
    for i in venda:
        print(f"{i.__class__.__name__}: R${i.preco():.2f}")
    print(f"Total: R${total(venda):.2f}")   # continua R$65.00 (Cortesia soma 0)
