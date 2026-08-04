# 🚀 Plano de 8 Semanas: Dados e Automação com Python

## 📅 Semana 1 - Terça: A Base do Pandas e Arquivos

**Objetivo:** Ler diferentes formatos de arquivo, lidar com delimitadores fora do padrão e converter dados de um formato para outro.

### 📁 Arquivos Necessários
- `vendas_atuais.csv` (Delimitador padrão: vírgula)
- `clientes_legado.xlsx` (Arquivo Excel)
- `logs_acesso.txt` (Delimitador: pipe `|`)

### 🛠️ Tarefas
- [ ] **Passo 1:** Importe a biblioteca `pandas` (caso dê erro no passo 3, instale o motor do Excel rodando `pip install openpyxl` no terminal).
- [ ] **Passo 2:** Carregue o arquivo `vendas_atuais.csv` em uma variável chamada `df_vendas`.
- [ ] **Passo 3:** Carregue o arquivo `clientes_legado.xlsx` em uma variável chamada `df_clientes`.
- [ ] **Passo 4:** Carregue o arquivo `logs_acesso.txt` em uma variável chamada `df_logs`. Configure o parâmetro `sep` corretamente para ler o pipe (`|`).
- [ ] **Passo 5:** Imprima as 5 primeiras linhas do `df_logs` (usando o método `.head()`) para verificar se as colunas foram separadas corretamente.
- [ ] **Passo 6:** Exporte o DataFrame `df_clientes` (que era um Excel) como um novo arquivo chamado `clientes_formatado.csv`. Lembre-se de passar o parâmetro `index=False` para não exportar os números das linhas.

---

## 📅 Semana 1 - Quinta: Filtros e Fatiamento

**Objetivo:** Navegar pelos DataFrames, selecionar colunas específicas e aplicar filtros condicionais (equivalente ao `WHERE` do SQL).

### 🛠️ Tarefas
- [ ] **Passo 1:** A partir do `df_vendas`, crie um novo DataFrame chamado `vendas_notebooks` filtrando apenas as linhas onde a coluna `produto` é exatamente igual a "Notebook".
- [ ] **Passo 2:** Calcule e imprima a soma total da coluna `quantidade` dentro desse novo DataFrame `vendas_notebooks`.
- [ ] **Passo 3:** A partir do `df_clientes`, selecione e exiba apenas um "recorte" contendo as colunas `NOME_COMPLETO` e `ESTADO`.
- [ ] **Passo 4:** Usando o `df_logs`, filtre apenas os acessos que duraram mais de 300 segundos (`tempo_sessao_segundos > 300`) **E** que visitaram a página `/checkout`. *(Dica: no Pandas, o operador "E" é o símbolo `&`, e cada condição precisa estar entre parênteses)*.
- [ ] **Passo 5:** Exporte esse último DataFrame de logs filtrados para um novo arquivo chamado `checkouts_longos.csv`.


# 🚀 Plano de 8 Semanas: Dados e Automação com Python

## 📅 Semana 2 - Terça: Limpeza Pesada (O Pão de Cada Dia)

**Objetivo:** Tratar valores nulos, remover duplicatas e padronizar textos inconsistentes (essencial para bases legadas).

### 📁 Arquivos Necessários
- `clientes_legado.xlsx` (Base caótica de clientes)

### 🛠️ Tarefas
- [ ] **Passo 1:** Carregue o arquivo `clientes_legado.xlsx` em um DataFrame chamado `df_clientes`.
- [ ] **Passo 2 (Tratamento de Texto):** Padronize a coluna `NOME_COMPLETO`. Remova os espaços em branco excedentes nas pontas (usando `.str.strip()`) e deixe o formato de capitalização padrão, com a primeira letra de cada palavra maiúscula (usando `.str.title()`).
- [ ] **Passo 3 (Valores Nulos):** Verifique quantas linhas possuem valores nulos (`NaN`) na coluna `ESTADO` ou `PONTOS_FIDELIDADE` usando `.isnull().sum()`.
- [ ] **Passo 4:** Preencha os valores nulos da coluna `ESTADO` com o texto `"DESCONHECIDO"` (usando `.fillna()`) e preencha os nulos da coluna `PONTOS_FIDELIDADE` com o valor `0`.
- [ ] **Passo 5:** Exporte essa base limpa para um novo arquivo chamado `clientes_higienizados.csv`.

---

## 📅 Semana 2 - Quinta: Domínio do Tempo e Tipos

**Objetivo:** Converter colunas de texto em datas reais e extrair informações temporais para análises.

### 📁 Arquivos Necessários
- `vendas_atuais.csv` (Vendas com datas em formato de texto)
- `logs_acesso.txt` (Logs com carimbo de data/hora)

### 🛠️ Tarefas
- [ ] **Passo 1:** Carregue o arquivo `vendas_atuais.csv` em um DataFrame.
- [ ] **Passo 2:** Converta a coluna `data` de texto para o tipo datetime real do Pandas usando a função `pd.to_datetime()`.
- [ ] **Passo 3:** Crie uma nova coluna chamada `mes_venda` no seu DataFrame, extraindo apenas o número do mês da coluna de data (dica: `.dt.month`).
- [ ] **Passo 4:** Crie outra coluna chamada `dia_da_semana`, extraindo o dia da semana correspondente (dica: `.dt.day_name()`).
- [ ] **Passo 5:** Carregue o arquivo `logs_acesso.txt` (com o separador `|`) e converta a coluna `data_acesso` para datetime também. Filtre apenas os acessos que aconteceram em uma data específica ou após um dia base para testar a manipulação temporal.