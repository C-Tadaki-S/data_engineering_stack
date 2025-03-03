# Data Pipeline Challenge: Docker, Airflow, Spark & PySpark

Este repositório apresenta um ambiente containerizado para um pipeline de dados com três camadas – **Raw**, **Trusted** e **Analytic** – utilizando Docker, Apache Airflow, Apache Spark e PySpark. O projeto foi desenvolvido para demonstrar a integração dessas tecnologias em um fluxo de ETL (Extract, Transform, Load) básico.

## Visão Geral

- **Raw:** Camada onde os dados brutos são armazenados.
- **Trusted:** Camada que contém os dados limpos e validados (transformações simples, como remoção de valores nulos).
- **Analytic:** Camada onde os dados são agregados e preparados para análises (ex.: cálculo de médias por categoria).

## Arquitetura e Componentes

O ambiente é composto por diversos containers orquestrados com Docker Compose:

- **Airflow:** Gerencia e agenda o pipeline por meio de um DAG (definido em `dags/pipeline_dados.py`), executando tarefas de ingestão e processamento dos dados.
- **Spark Cluster:** Composto por um Spark Master e um ou mais Spark Workers, responsáveis por executar os jobs em PySpark.
- **PySpark Job Container:** Container customizado (configurado via `spark/Dockerfile`) para rodar scripts de transformação de dados.

O fluxo do pipeline é executado da seguinte forma:
1. **Ingestão:** Os dados brutos são copiados para a camada *Raw*.
2. **Processamento Trusted:** Um job em PySpark lê os dados brutos, realiza a limpeza e os grava na camada *Trusted*.
3. **Processamento Analytic:** Outro job em PySpark agrega os dados limpos para gerar a camada *Analytic*.

## Estrutura do Projeto

