import pytest
from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
    "valor_base, plano, dias_atrazo, valor_esperado",
    [
        (0.0, "BASICO", 2, -1.0),
        (1.0, "BASICO", -2, -1.0),

        (1.0, "", 0, -2.0),

        (100.0, "BASICO", 0, 100.0),
        (200.0, "PREMIUM", 0, 180.0),
        (400.0, "EMPRESARIAL", 0, 320.0),

        (50.0, "BASICO", 2, 55.5),
        (100.0, "BASICO", 40, 165.0),

        (10.0, "BASICO", 0, 10.0),
        (10.0, "BASICO", 1, 15.05),
        (10.0, "BASICO", 30, 16.5),
        (10.0, "BASICO", 31, 38.1),

        (-25.0, "BASICO", 0, -1.0)

    ],
)

def test_cobranca_classificar_caixa_preta(
    valor_base, plano, dias_atrazo, valor_esperado
):
    assert processar_cobranca(valor_base, plano, dias_atrazo) == valor_esperado


import time

from app.faturamento.cobranca import processar_cobranca

def test_tempo_execucao_cobranca_nao_funcional():
    inicio = time.perf_counter()
    resultado = processar_cobranca(500.0, "BASICO", 0)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert resultado > 0.0
    assert tempo_decorrido < 0.1