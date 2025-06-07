
# 📚 Books to Scrape - Web Scraper

Projeto de web scraping desenvolvido em Python para extrair dados do site [Books to Scrape](http://books.toscrape.com), um site de demonstração para práticas de scraping. O script coleta informações sobre livros e exporta os dados para um arquivo CSV.

---

## 📌 Objetivo

O objetivo do projeto é automatizar a coleta de dados de livros disponíveis no site, extraindo informações como:

- Título
- Preço
- Número de estrelas (avaliação)
- Estoque
- Gênero (categoria)
- Descrição

---

## 🧠 Tecnologias e Bibliotecas Utilizadas

- `Python 3`
- `requests`
- `BeautifulSoup (bs4)`
- `pandas`
- `concurrent.futures` (ThreadPoolExecutor e ProcessPoolExecutor)

---

## 📁 Estrutura do Projeto

```
desafio/
│
├── main.py        # Arquivo principal que orquestra a coleta e exportação dos dados
├── scraping/
    └── pages.py                 # Lê e processa cada página do site
    └── book_info.py             # Extrai informações detalhadas de cada livro
    └── utils.py                 # Dicionário de conversão de estrelas
└── data/
    └── books.csv            # Arquivo gerado com os dados coletados
```

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/books-scraper.git
cd books-scraper
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate       # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o script principal

```bash
python main.py
```

Após a execução, o arquivo `books.csv` será salvo na pasta `data/`.

---

## 🧠 Como Funciona

- `main.py` gera URLs das 50 páginas do site e processa cada uma em paralelo com `ProcessPoolExecutor`.
- `readPage()` em `pages.py` busca e analisa todos os livros da página usando `ThreadPoolExecutor` para acelerar o scraping individual dos livros.
- `fetchBookData()` em `book_info.py` extrai os dados básicos do livro, e chama `readBookInfo()` para pegar o gênero e a descrição acessando a página individual do livro.
- `utils.py` contém um dicionário auxiliar para converter avaliações por estrelas (texto) em números.

---

## 📊 Exemplo de Dados Coletados

| Titles              | Prices | Stars | Gender  | Stock     | Descriptions              |
|---------------------|--------|-------|---------|-----------|----------------------------|
| A Light in the Attic | 51.77  | 3     | Poetry  | In stock  | It's hard to imagine...    |
| Tipping the Velvet   | 53.74  | 1     | Fiction | In stock  | Tipping the Velvet is...   |

---

## ⏱️ Desempenho

- A coleta foi otimizada com `concurrent.futures` para paralelizar:
  - o scraping de páginas (`multiprocessamento`)
  - o scraping de livros dentro da página (`multithread`)
- Há um `sleep` aleatório entre 1-3 segundos nas requisições de detalhes para evitar bloqueios pelo servidor.

---

## 🛡️ Boas Práticas

- User-Agent personalizado nas requisições
- Tratamento de exceções com `try/except`
- Códigos organizados por responsabilidade (modularização)
- Evita scraping agressivo (uso de delays aleatórios)

---

## 📌 Licença

Este projeto é apenas para fins educacionais. O site alvo é público e voltado para testes de scraping. Nenhuma informação real ou privada está sendo coletada.

---

## ✍️ Autor

Desenvolvido por Matheus Amorim  
💼 GitHub: [https://github.com/MatheusAmorimm](https://github.com/MatheusAmorimm)

---
