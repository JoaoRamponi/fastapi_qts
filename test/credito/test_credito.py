import pytest
from app.credito.credito import classificar_credito
@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        (0, 1000, True, "renda invalida"),
        (0, -300, True, "renda invalida"),
        (1000, -300, False, "score invalido"),
        (150, 3000, False, "score invalido"),
        (500, 900, True, "reprovado"),
        (700, 299, False, "reprovado"),
        (1000, 599, False, "aprovado padrao"),
        (3050, 929, False, "aprovado premium")
    ],
)

def test_credito_classificar_caixa_preta(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado
