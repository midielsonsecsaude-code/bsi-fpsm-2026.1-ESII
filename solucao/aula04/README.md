# Solução — Aula 4 (Parte B): OCP na Bilheteria CineForma

Solução de referência, correta e rodável, da Parte B da Aula 4.

## O que foi aplicado (OCP)
- **Uma classe por tipo de ingresso** (`modelos/ingresso.py`): `Inteira`, `Meia`,
  `VIP` — cada uma sabe calcular o seu próprio `preco()`. A base `Ingresso` é o
  contrato.
- **Bilheteria polimórfica** (`servico/bilheteria.py`): `total()` soma
  `i.preco()` de cada ingresso. **Sem `if/elif` por tipo** e sem o cálculo
  duplicado da v1.0 (que aparecia em `vender` e em `total`).
- **Tipo novo `Cortesia` (preço 0,00)** adicionado só criando uma classe nova
  que respeita o contrato e registrando-a na venda do `main.py` —
  **sem tocar** em `Inteira`, `Meia`, `VIP` nem em `total()`.

## Como rodar
```bash
cd solucao/aula04
python3 main.py
```

## Saída esperada
```
Inteira: R$20.00
Meia: R$10.00
VIP: R$35.00
Cortesia: R$0.00
Total: R$65.00
```
O total bate com a versão original (`aula04/main.py` → `R$65.00`), pois a
`Cortesia` soma 0,00.
