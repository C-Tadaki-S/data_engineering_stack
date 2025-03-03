from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

spark = SparkSession.builder.appName("ProcessoTrustedToAnalytic").getOrCreate()

# Exemplo: leitura dos dados Trusted
df_trusted = spark.read.csv("/app/data/trusted/data_trusted.csv", header=True, inferSchema=True)

# Exemplo de transformação: calcular a média de uma coluna

df_analytic = df_trusted.groupBy("categoria").agg(avg(col("valor")).alias("media_valor"))

# Salvar os dados na camada ANALYTIC
df_analytic.write.mode("overwrite").csv("/app/data/analytic/data_analytic.csv", header=True)

spark.stop()