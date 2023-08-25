import databricks.koalas as ks

def read_parquet_from_dbfs(path):
    """
    Returns:
    - DataFrame Koalas.
    """
    return ks.read_parquet(path)

def write_parquet_to_dbfs(df, path):
    """
    Escreve um DataFrame Koalas como arquivo Parquet no DBFS.
    """
    df.to_parquet(path)

def mount_azure_blob(container_name, storage_account_name, mount_point, sas_token):
    """
    Monta um blob do Azure no DBFS.
    """
    dbutils.fs.mount(
        source=f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net/",
        mount_point=mount_point,
        extra_configs={"<conf-key>":sas_token}
    )
