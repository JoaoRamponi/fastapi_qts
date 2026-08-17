from app.classificacao.status import calcular_status_pedido

def test_retorna_invalido_quando_valor_zero():
    assert calcular_status_pedido(0, True) == "Invalido"

def test_retrona_invalido_quando_valor_negativo():
    assert calcular_status_pedido(-10, False) == "Invalido"

def test_retorna_pendente_quando_nao_foi_pago():
    assert calcular_status_pedido(120, False) == "Pendente"

def test_retorna_pedente_quando_pago_e_valor_valido():
    assert calcular_status_pedido(120, True) == "Confirmado"