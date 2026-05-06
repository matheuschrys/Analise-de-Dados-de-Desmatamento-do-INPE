"""Funções de carga, transformação e agregação dos dados PRODES/INPE."""

from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_RAW_DIR = PROJECT_ROOT / "data" / "raw"
DEFAULT_PRODES_PATH = DATA_RAW_DIR / "br_inpe_prodes_municipio_bioma.csv"
DEFAULT_MUNICIPIOS_PATH = DATA_RAW_DIR / "br_bd_diretorios_brasil_municipio.csv"

COLUNAS_MUNICIPIOS = [
    "id_municipio",
    "nome",
    "nome_mesorregiao",
    "nome_regiao_metropolitana",
    "sigla_uf",
    "nome_uf",
    "nome_regiao",
    "amazonia_legal",
]


def carregar_dados(
    caminho_prodes: str | Path = DEFAULT_PRODES_PATH,
    caminho_municipios: str | Path = DEFAULT_MUNICIPIOS_PATH,
) -> pd.DataFrame:
    """Carrega as bases CSV e retorna um DataFrame integrado por município."""
    df_prodes = pd.read_csv(caminho_prodes)
    df_municipios = pd.read_csv(caminho_municipios, usecols=COLUNAS_MUNICIPIOS)

    return df_prodes.merge(df_municipios, how="inner", on="id_municipio")


def calcular_desmatamento_por_bioma(df: pd.DataFrame) -> pd.DataFrame:
    """Soma a área desmatada por ano e bioma, incluindo valor em milhões de km²."""
    resultado = _agrupar_por_ano_bioma(df, "desmatado")
    resultado["desmatado_milhoes"] = _em_milhoes(resultado["desmatado"])
    return resultado


def calcular_area_total_por_bioma(df: pd.DataFrame) -> pd.DataFrame:
    """Soma a área total monitorada por ano e bioma, incluindo valor em milhões de km²."""
    resultado = _agrupar_por_ano_bioma(df, "area_total")
    resultado["area_total_milhoes"] = _em_milhoes(resultado["area_total"])
    return resultado


def calcular_percentual_desmatado_por_bioma(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula o percentual de área desmatada em relação à área total por ano e bioma."""
    resultado = (
        df.groupby(["ano", "bioma"], as_index=False)[["desmatado", "area_total"]]
        .sum()
        .sort_values(["bioma", "ano"])
    )
    resultado["porcentagem_desmatada"] = (
        resultado["desmatado"] / resultado["area_total"] * 100
    )
    return resultado


def calcular_ranking_estados(df: pd.DataFrame) -> pd.DataFrame:
    """Gera ranking de estados por valores absolutos e relativos de desmatamento."""
    resultado = df.groupby("sigla_uf", as_index=False)[["desmatado", "area_total"]].sum()
    resultado["desmatado_milhoes"] = _em_milhoes(resultado["desmatado"])
    resultado["area_total_milhoes"] = _em_milhoes(resultado["area_total"])
    resultado["porcentagem_desmatada"] = (
        resultado["desmatado"] / resultado["area_total"] * 100
    )
    return resultado.sort_values("desmatado", ascending=False)


def _agrupar_por_ano_bioma(df: pd.DataFrame, coluna_valor: str) -> pd.DataFrame:
    return (
        df.groupby(["ano", "bioma"], as_index=False)[coluna_valor]
        .sum()
        .sort_values(["bioma", "ano"])
    )


def _em_milhoes(serie: pd.Series) -> pd.Series:
    return (serie / 1_000_000).round(2)
