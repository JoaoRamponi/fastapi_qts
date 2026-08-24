import pytest

from app.envio.frete import calcular_frete_expresso


@pytest.mark.parametrize(
    "peso_kg, distancia_km, valor_esperado",
    [
        (0, 50, 0.0),
        (2, 0, 0.0),
        (-1, 20, 0.0),
        (2, 10, 20.0),  # 10 (base) + 2 * 2.5 (5) + 10 * 0.5 (5) = 20.0
        (4, 120, 95.0),  # 10 (base) + 10 (peso) + 60 (dist) + 15 (taxa) = 95.0
    ],
)
def test_calcular_frete_expresso_funcional(
    peso_kg, distancia_km, valor_esperado
):
    assert (
        calcular_frete_expresso(peso_kg, distancia_km) == valor_esperado
    )

import time

from app.envio.frete import calcular_frete_expresso


def test_tempo_execucao_frete_nao_funcional():
    inicio = time.perf_counter()
    resultado = calcular_frete_expresso(2, 50)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert resultado > 0.0
    # Garante que executa em menos de 80 milissegundos
    assert tempo_decorrido < 0.08
    