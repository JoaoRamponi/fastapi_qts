VALOR_BONUS_OURO = 120.0
VALOR_BONUS_PADRAO = 50.0
LIMITE_MINIMO_OURO = 50
LIMITE_MINIMO_PADRAO = 20

def calcular_bonus_entregador(total_entregas: int) -> float:
    """Calcule a bonificacao financeira de acordo com a quantidade de entregas."""
    if total_entregas < 0 :
        return 0
    
    if total_entregas >= LIMITE_MINIMO_OURO:
        return VALOR_BONUS_OURO
    
    if total_entregas >= LIMITE_MINIMO_PADRAO:
        return VALOR_BONUS_PADRAO
    
    return 0.0


