from pyspark.sql import DataFrame
from pyspark.sql.functions import avg, sum, max, min, count, lit

def count_by_column(df: DataFrame, column_name: str) -> DataFrame:
    """Count occurrences by a specific column."""
    return df.groupBy(column_name).agg(count(lit(1)).alias("count"))

def average_by_column(df: DataFrame, group_column: str, agg_column: str) -> DataFrame:
    """Calculate average of a column grouped by another column."""
    return df.groupBy(group_column).agg(avg(agg_column).alias(f"avg_{agg_column}"))

def sum_by_column(df: DataFrame, group_column: str, agg_column: str) -> DataFrame:
    """Calculate sum of a column grouped by another column."""
    return df.groupBy(group_column).agg(sum(agg_column).alias(f"sum_{agg_column}"))

def max_min_by_column(df: DataFrame, group_column: str, agg_column: str) -> DataFrame:
    """Find max and min values of a column grouped by another column."""
    return df.groupBy(group_column).agg(max(agg_column).alias(f"max_{agg_column}"), min(agg_column).alias(f"min_{agg_column}"))

def percentage_distribution(df: DataFrame, column_name: str) -> DataFrame:
    """Calculate percentage distribution of values in a column."""
    total_count = df.count()
    return (df.groupBy(column_name)
            .agg(count(lit(1)).alias("count"))
            .withColumn("percentage", (col("count") / total_count) * 100))



