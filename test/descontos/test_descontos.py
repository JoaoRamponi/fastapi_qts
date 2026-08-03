from app.desconto.descontos import calcular_desconto

def test_valor_zero():
    resultado = calcular_desconto(0, True)
    assert resultado == 0

def test_valor_negativo():
    resultado = calcular_desconto(-10, False)
    assert resultado == 0

def test_cliente_vip():
    resultado = calcular_desconto(100, True)
    assert resultado == 80

def test_cliente_nao_vip():
    resultado = calcular_desconto(100, False)
    assert resultado == 90

def test_valor_pequeno_vip():
    resultado = calcular_desconto(0.01, True)
    assert round(resultado, 3) == 0.008

def test_valor_pequeno_nao_vip():
    resultado = calcular_desconto(0.01, False)
    assert round(resultado, 3) == 0.009

def test_valor_alto_vip():
    resultado = calcular_desconto(200, True)
    assert resultado == 160

def test_valor_alto_nao_vip():
    resultado = calcular_desconto(200, False)
    assert resultado == 180
