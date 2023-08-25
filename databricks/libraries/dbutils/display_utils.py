from IPython.display import display, HTML

def display_spark_df(df, num_rows=10):
    """
    - df: DataFrame Spark.
    - num_rows: Número de linhas a serem exibidas.
    """
    display(df.limit(num_rows).toPandas())

def display_html(html_content):
    """
    Parameters:
    - html_content: String contendo o conteúdo HTML.
    """
    display(HTML(html_content))

def display_chart(chart):
    """
    Exibe um gráfico (por exemplo, um gráfico matplotlib ou plotly).
    - chart: Objeto de gráfico.
    """
    display(chart)
