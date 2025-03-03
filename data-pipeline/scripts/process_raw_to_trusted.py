from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ProcessRawToTrusted").getOrCreate()

# Exemplo: lendo um csv na camada RAW
df = spark.read.options(header=True, inferSchema=True, delimiter=",").csv("/app/data/raw/data_original.csv", header=True, inferSchema=True)
df.printSchema()
# Realizar transformações simples: Remoção de nulos por exemplo
df_trusted = df.dropna()

# Salvar os dados na camada TRUSTED
df_trusted.write.mode("overwrite").csv("/app/data/trusted/data_trusted.csv", header=True)

spark.stop()