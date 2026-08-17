import pytest
from app.credito.credito import classificar_credito
@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        (0, 1000, True, "renda invalida"),
        (0, -300, True, "renda invalida"),
        (1000, -900, False, "score invalido"),
        (1500, 9000, False, "score invalido"),
        (5000, 900, True, "reprovado"),
        (7000, 299, False, "reprovado"),
        (1000, 599, False, "aprovado padrao"),
        (3050, 929, False, "aprovado premium")
    ],
)

@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        (0, 0, True, "renda invalida"),
        (0.01, -1, False, "score invalido"),
        (0.01, 399, False, "reprovado"),
        (0.01, 699, False, "aprovado padrao"),
        (0.01, 999, False, "aprovado premium")
    ],
)

def test_credito_classificar_caixa_preta(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado
