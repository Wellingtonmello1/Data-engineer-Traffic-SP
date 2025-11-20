# Data-engineer-Traffic-SP
Meu primeiro projeto independente de Engenharia de dados pegando dados publicos do GOVERNO


aws-traffic-data-lake/
│
├── README.md
│
├── architecture/
│   ├── data-lake-diagram.png
│   └── glue-flow.png
│
├── glue-jobs/
│   ├── bronze-to-silver-traffic.py
│   ├── silver-to-gold-traffic.py
│   └── crawler-setup.md
│
├── athena/
│   ├── bronze_tables.sql
│   ├── silver_tables.sql
│   ├── gold_views.sql
│   └── queries_examples.sql
│
├── lakeformation/
│   ├── permissions-setup.md
│   └── lf-diagram.png
│
├── data-samples/
│   ├── accidents.json
│   ├── traffic_flow.json
│   ├── road_conditions.json
│   └── traffic_cameras.json
│
└── terraform/ (opcional, se quiser mostrar infra como código)
    └── s3-glue-athena.tf
