from app.entregas.bonificacao import calcular_bonus_entrega

def test_entregador_com_mais_de_vinte_entregas_recebe_bonus():
    resultado = calcular_bonus_entrega(total_entregas=25)

    assert resultado == 50.0

def test_entregador_com_menos_de_vinte_entregas_nao_recebe():
    resultado = calcular_bonus_entrega(total_entregas=10)
    
    assert resultado == 0.0

def test_entregador_ouro_com_mais_de_cinquenta_entregas_recebe_bonus_maior():
    resultado = calcular_bonus_entrega(total_entregas=55)

    assert resultado == 120.0