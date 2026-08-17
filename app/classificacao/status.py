def calcular_status_pedido(valor_total: float, pago: bool) -> str:
    if valor_total <= 0: 
        return "Invalido"

    if not pago:
        return "Pendente"
    return "Confirmado"

# invalido 
# pendente
# confirmado