from app.desconto.descontos import calcular_desconto


def test_valor_zero():
    resultado = calcular_desconto(0, True)
    assert resultado == 0


def test_valor_negativo():
    resultado = calcular_desconto(-10, False)
    assert resultado == 0


