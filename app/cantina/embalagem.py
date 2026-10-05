def calcular_taxa_embalagem(levar_viagem: bool, quantidade_itens: int) -> float:
    """Calcule a taxa de embalagem caso o cliente deseja levar o pedido"""
    if not levar_viagem or quantidade_itens <= 0:
        return 0.0

    taxa_fixa = 2.0
    adicional_por_item = quantidade_itens * 0.50

    return round(taxa_fixa + adicional_por_item, 2)