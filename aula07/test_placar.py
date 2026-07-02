# test_placar.py — testes do resultado da partida
#
# Cada teste e uma funcao que comeca com test_ e confere o codigo com assert.
# Rode todos com:  pytest
from placar import resultado


def test_vitoria_quando_a_casa_faz_mais_gols():
    assert resultado(2, 1) == "vitória"


# ------------------------------------------------------------------
# TODO def test_empate_quando_o_placar_e_igual():
assert resultado(1, 1) == "empate"
 