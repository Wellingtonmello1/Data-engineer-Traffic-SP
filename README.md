# Data-engineer-Traffic-SP
Meu primeiro projeto independente de Engenharia de dados pegando dados publicos do GOVERNO

AWS Traffic Data Lake – End-to-End Data Engineering Project
Este projeto demonstra um Data Lake completo na AWS, usando:

Amazon S3 (Bronze → Silver → Gold)
AWS Glue (ETL, Crawlers, Jobs)
Lake Formation (Governança e Segurança)
Athena (SQL Analytics)
Parquet + Particionamento
IAM (permissões granulares)

S3 (Bronze - JSON cru)
         ↓
AWS Glue ETL (PySpark)
         ↓
S3 (Silver - Parquet Curado)
         ↓
AWS Glue Crawler
         ↓
Athena (Catálogo)
         ↓
Governança Lake Formation
         ↓
S3 (Gold - Agregado)
