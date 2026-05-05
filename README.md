# 📊 Job Market Scraper

Coleta automatizada de vagas de emprego de 10 áreas do mercado brasileiro,
com limpeza dos dados e exportação para Power BI.

---

## 💡 Motivação

O mercado de trabalho brasileiro é amplo e diversificado, mas é difícil 
ter uma visão clara de quais áreas têm mais oportunidades, quais empresas 
mais contratam e como as vagas se distribuem por região.

Este projeto automatiza a coleta de vagas de 10 áreas diferentes, 
transforma os dados brutos em informação estruturada e gera insumo 
para análise e visualização no Power BI.

---

## 🎯 Objetivos

- Coletar vagas de 10 áreas diferentes do mercado brasileiro
- Extrair informações como cargo, empresa, cidade, skills e nível
- Limpar e estruturar os dados com pandas
- Exportar para CSV/Excel pronto para análise no Power BI

---

## 🛠️ Tecnologias

| Ferramenta | Uso |
|---|---|
| Python 3.13 | Linguagem principal |
| requests | Requisições HTTP |
| BeautifulSoup4 | Extração de dados HTML |
| pandas | Transformação dos dados |
| openpyxl | Exportação para Excel |

---

## 📁 Estrutura do Projeto

job-market-scraper/
│
├── data/
│   ├── raw/          # Dados brutos coletados
│   └── processed/    # Dados limpos e estruturados
│
├── src/
│   ├── scraper.py    # Coleta os dados
│   ├── cleaner.py    # Limpa e transforma
│   └── exporter.py   # Exporta para CSV/Excel
│
├── notebooks/        # Análises exploratórias
├── docs/             # Documentação adicional
├── .gitignore
├── requirements.txt
└── README.md

---

## ▶️ Como Executar

### Pré-requisitos
- Python 3.10 ou superior
- Git

### Passo a passo

```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/job-market-scraper.git

# Entre na pasta
cd job-market-scraper

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o scraper
python src/scraper.py
```

---

## 📦 Resultados Esperados

Ao executar o projeto, serão gerados:

- `data/raw/` — dados brutos em JSON ou HTML
- `data/processed/vagas.csv` — dados limpos em CSV
- `data/processed/vagas.xlsx` — dados prontos para Power BI

---

## 🔮 Próximos Passos

- [x] Expandir coleta para múltiplas áreas
- [x] Separar cidade e estado em colunas distintas
- [ ] Adicionar mais fontes de vagas
- [ ] Criar dashboard no Power BI
- [ ] Agendar execução automática com schedule
- [ ] Análise de frequência de skills por cargo

---

## 👤 Autor

**Leandro Bispo**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/leandrorbispo/)
[![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/LeandroBispo90)