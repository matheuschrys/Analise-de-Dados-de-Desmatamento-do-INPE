"""Ponto de entrada simples para gerar as tabelas consolidadas da análise."""

from .analysis import (
    calcular_area_total_por_bioma,
    calcular_desmatamento_por_bioma,
    calcular_percentual_desmatado_por_bioma,
    calcular_ranking_estados,
    carregar_dados,
)


def main() -> None:
    df = carregar_dados()
    print("Dados integrados:", df.shape)
    print("\nDesmatamento por bioma:")
    print(calcular_desmatamento_por_bioma(df).head())
    print("\nÁrea total por bioma:")
    print(calcular_area_total_por_bioma(df).head())
    print("\nPercentual desmatado por bioma:")
    print(calcular_percentual_desmatado_por_bioma(df).head())
    print("\nRanking de estados:")
    print(calcular_ranking_estados(df).head())


if __name__ == "__main__":
    main()
