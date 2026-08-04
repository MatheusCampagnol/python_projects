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
