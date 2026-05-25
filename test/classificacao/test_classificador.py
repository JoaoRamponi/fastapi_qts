from app.classificacao.classificador import classificador_nota

def test_nota_invaldia_abaixo_de_zero():
    assert classificador_nota(-1) == "Nota invalida"

def test_nota_aprovado():
    assert classificador_nota(9) == "Aprovado"


