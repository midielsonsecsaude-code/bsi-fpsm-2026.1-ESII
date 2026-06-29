# senha.py — validador de senha (construído por TDD na Aula 8)
#
# validar(senha) devolve uma LISTA com os problemas da senha.
# Lista vazia ([]) = senha aprovada.
#
# As 3 regras nasceram de testes (RED -> GREEN). Depois veio o REFACTOR:
# o padrão "if not <condição>: adiciona <mensagem>" se repetia 3 vezes,
# então juntamos tudo numa TABELA de regras + um for. O comportamento é o
# mesmo (os testes continuam passando) — só ficou mais limpo. De quebra,
# adicionar uma regra nova agora é só mais uma linha na tabela.
def validar(senha):
    regras = [
        (len(senha) >= 8,                 "precisa de pelo menos 8 caracteres"),
        (any(c.isdigit() for c in senha), "precisa de um número"),
        (any(c.isupper() for c in senha), "precisa de uma letra maiúscula"),
    ]
    problemas = []
    for ok, mensagem in regras:
        if not ok:
            problemas.append(mensagem)
    return problemas
