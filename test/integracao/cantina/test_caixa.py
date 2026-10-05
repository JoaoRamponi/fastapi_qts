from app.cantina.caixa import processar_venda

def test_integracao_venda_estudante_combo_para_viagem():
    resultado = processar_venda(
        valor_bruto=50.0,
        quantidade_itens=3,
        tipo_cliente="estudante",
        levar_viagem=True
    )

    assert resultado["sucesso"] is True
    assert resultado["desconto_aplicado"] == 7.50
    assert resultado["taxa_embalagem"] == 3.50
    assert resultado["total_final"] == 46.00