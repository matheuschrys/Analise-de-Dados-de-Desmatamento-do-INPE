"""Utilitários para análise de dados de desmatamento do PRODES/INPE."""

from .analysis import (
    DEFAULT_MUNICIPIOS_PATH,
    DEFAULT_PRODES_PATH,
    carregar_dados,
    calcular_desmatamento_por_bioma,
    calcular_area_total_por_bioma,
    calcular_percentual_desmatado_por_bioma,
    calcular_ranking_estados,
)

__all__ = [
    "DEFAULT_MUNICIPIOS_PATH",
    "DEFAULT_PRODES_PATH",
    "carregar_dados",
    "calcular_desmatamento_por_bioma",
    "calcular_area_total_por_bioma",
    "calcular_percentual_desmatado_por_bioma",
    "calcular_ranking_estados",
]
