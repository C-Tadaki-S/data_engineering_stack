from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ProcessRawToTrusted").getOrCreate()

# Exemplo: lendo um csv na camada RAW
df = spark.read.csv("/app/data/raw/data_original.csv", header=True, inferSchema=True)

# Realizar transformações simples: Remoção de nulos por exemplo
df_trusted = df.dropna()

# Salvar os dados na camada TRUSTED
df_trusted.write.mode("overwrite").csv("/app/data/trusted/data_trusted.csv", header=True)

spark.stop()