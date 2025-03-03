Segue um exemplo de **README.md** que descreve o resultado final do projeto, destacando a arquitetura, o fluxo dos dados e como interagir com o ambiente, sem reproduzir cada passo de configuração:

---

```markdown
# Data Pipeline Challenge: Docker, Airflow, Spark & PySpark

Este repositório apresenta um ambiente containerizado para um pipeline de dados com três camadas – **Raw**, **Trusted** e **Analytic** – utilizando Docker, Apache Airflow, Apache Spark e PySpark. O projeto foi desenvolvido para demonstrar a integração dessas tecnologias em um fluxo de ETL (Extract, Transform, Load).

## Visão Geral

- **Raw:** Camada onde os dados brutos são armazenados.
- **Trusted:** Camada que contém os dados limpos e validados (transformações simples, como remoção de valores nulos).
- **Analytic:** Camada onde os dados são agregados e preparados para análises (ex.: cálculo de médias por categoria).

## Arquitetura e Componentes

O ambiente é composto por diversos containers orquestrados com Docker Compose:

- **Airflow:** Gerencia e agenda o pipeline por meio de um DAG (definido em `dags/pipeline_dados.py`), executando tarefas de ingestão e processamento.
- **Spark Cluster:** Composto por um Spark Master e um ou mais Spark Workers, responsáveis por executar os jobs em PySpark.
- **PySpark Job Container:** Container customizado (configurado via `spark/Dockerfile`) para rodar scripts de transformação de dados.

O fluxo do pipeline é executado da seguinte forma:
1. **Ingestão:** Os dados brutos são copiados para a camada *Raw*.
2. **Processamento Trusted:** Um job em PySpark lê os dados brutos, realiza a limpeza e os grava na camada *Trusted*.
3. **Processamento Analytic:** Outro job em PySpark agrega os dados limpos para gerar a camada *Analytic*.

## Estrutura do Projeto

```
data-pipeline/
├── airflow/          # Configurações e logs do Airflow
├── dags/             # Definição do DAG do Airflow
├── spark/            # Dockerfile e configurações para o ambiente Spark/PySpark
├── scripts/          # Scripts em PySpark para processamento (ETL)
└── data/
    ├── raw           # Dados brutos (Raw)
    ├── trusted       # Dados processados e limpos (Trusted)
    └── analytic      # Dados prontos para análise (Analytic)
```

## Como Utilizar

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/data-pipeline.git
   cd data-pipeline
   ```

2. **Garantir que Docker e Docker Compose estejam instalados.**

3. **Iniciar o ambiente:**
   ```bash
   docker-compose up -d
   ```

4. **Acessar o Airflow:**
   Abra o navegador e acesse [http://localhost:8080](http://localhost:8080). Localize o DAG `pipeline_de_dados`, ative-o e execute-o para disparar o pipeline.

5. **Verificar os resultados:**
   - Confira a pasta `data/raw` para os dados brutos.
   - Confira a pasta `data/trusted` para os dados limpos.
   - Confira a pasta `data/analytic` para os dados agregados prontos para análise.

## Personalizações e Próximos Passos

- **Airflow DAG:** Personalize o fluxo de trabalho ajustando o DAG em `dags/pipeline_de_dados.py`.
- **PySpark Scripts:** Amplie ou ajuste as transformações nos scripts dentro da pasta `scripts/`.
- **Docker e Ambiente Spark:** Modifique as configurações do Docker Compose e do Dockerfile em `spark/` conforme suas necessidades.

## Suporte

Caso ocorram dúvidas ou problemas, consulte os logs dos containers:
```bash
docker-compose logs -f airflow
```

## Licença

Este projeto é distribuído sob a licença [MIT](LICENSE).
```

---

Este modelo de README resume o resultado final do pipeline, destacando sua arquitetura, o fluxo dos dados e os principais componentes, sem detalhar o passo a passo da configuração. Basta ajustar as URLs, nomes de usuário e detalhes específicos conforme necessário para o seu projeto.
