from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def drop_null_columns(df: DataFrame) -> DataFrame:
    """Drop columns with all null values."""
    return df.dropna(how='all', subset=df.columns)

def drop_null_rows(df: DataFrame, columns: list) -> DataFrame:
    """Drop rows with null values in specific columns."""
    return df.dropna(subset=columns)

def rename_columns(df: DataFrame, rename_mapping: dict) -> DataFrame:
    """Rename columns based on a provided mapping."""
    for old_name, new_name in rename_mapping.items():
        df = df.withColumnRenamed(old_name, new_name)
    return df

def select_columns(df: DataFrame, columns: list) -> DataFrame:
    """Select a subset of columns."""
    return df.select(*columns)

def add_calculated_column(df: DataFrame, new_column_name: str, expression: str) -> DataFrame:
    """Add a new column based on an expression."""
    return df.withColumn(new_column_name, expr(expression))

def sort_dataframe(df: DataFrame, columns: list, ascending: bool = True) -> DataFrame:
    """Sort the DataFrame based on one or more columns."""
    return df.sort(*columns, ascending=ascending)


