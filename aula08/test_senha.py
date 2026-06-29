# test_senha.py — testes do validador de senha
#
# Esta aula foi construída por TDD: cada teste abaixo veio ANTES do código.
# Cada teste é uma função que começa com test_ e confere o código com assert.
# Rode todos com:  pytest
from senha import validar


def test_senha_boa_nao_tem_problemas():
    # uma senha que cumpre todas as regras devolve lista vazia
    assert validar("Abcdef12") == []


def test_senha_curta_avisa():
    assert validar("Ab1") == ["precisa de pelo menos 8 caracteres"]


def test_senha_sem_numero_avisa():
    assert validar("Abcdefgh") == ["precisa de um número"]


def test_senha_sem_maiuscula_avisa():
    assert validar("abcdefg1") == ["precisa de uma letra maiúscula"]


# ------------------------------------------------------------------
# TODO (Parte B): adicione UMA regra nova pelo ciclo do TDD (RED → GREEN).
#
#   1. RED  — escreva PRIMEIRO o teste abaixo e rode pytest (deve FALHAR):
#
#          def test_senha_sem_minuscula_avisa():
#              assert validar("ABCDEFG1") == ["precisa de uma letra minúscula"]
#
#   2. GREEN — agora adicione UMA LINHA na tabela 'regras' do senha.py
#             (foi para isso que a gente refatorou!):
#
#          (any(c.islower() for c in senha), "precisa de uma letra minúscula"),
#
#   3. Rode pytest de novo: devem aparecer 5 passed.
# ------------------------------------------------------------------
