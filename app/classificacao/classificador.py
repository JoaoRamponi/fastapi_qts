def  classificador_nota(nota: float) -> str:
    if nota < 0 or nota > 10 :
        return "Nota invalida"
    if nota >= 7:
        return "Aprovado"
    if nota >= 5:
        return "Recuperacao"
    return "Reprovado"