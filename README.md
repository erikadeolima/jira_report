# Jira Report Automation

Projeto para extração e análise de issues do Jira, gerando relatórios completos em CSV e Excel, pronto para análise de produtividade, tempo de desenvolvimento, story points e muito mais.

## Funcionalidades

- Busca todas as issues do Jira usando JQL customizável.
- Extrai campos relevantes: código, título, tipo, status, responsável, reporter, story points, datas, número de commits, etc.
- Calcula tempo de desenvolvimento e salva o relatório em CSV e Excel.
- Pronto para análises estatísticas com pandas.

## Pré-requisitos

- Python 3.8+
- Acesso à API do Jira (usuário, token e URL)
- Permissão para leitura das issues no Jira

## Instalação

1. Clone o repositório e acesse a pasta do projeto:

   ```bash
   cd /caminho/para/seu/projeto
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

   O arquivo `requirements.txt` deve conter:

   ```
   requests
   pandas
   openpyxl
   ```

## Configuração

Edite o arquivo `config.py` com suas credenciais do Jira:

```python
JIRA_URL = "https://suaempresa.atlassian.net"
JIRA_USER = "seu_email@dominio.com"
JIRA_TOKEN = "seu_token_api"
```

## Como usar

1. Execute o script principal:

   ```bash
   python -m jira_report_automation.main
   ```

   ou, se estiver na raiz do projeto:

   ```bash
   python -m jira_report.main
   ```

2. O script irá:

   - Buscar todas as issues do Jira conforme a JQL definida no código.
   - Processar e calcular os campos necessários.
   - Salvar os resultados em:
     - `/Users/erikalima/Documents/all_tasks_developed_by_erika_lima.csv`
     - `/Users/erikalima/Documents/all_tasks_developed_by_erika_lima.xlsx`

3. O DataFrame será exibido no terminal ao final da execução.

## Customização

- Para alterar o filtro das issues, edite a variável `jql` no arquivo `main.py`:

  ```python
  jql = "assignee = currentUser() AND issuetype in standardIssueTypes() ORDER BY created DESC"
  ```

- Para mudar o caminho de saída dos arquivos, edite o caminho nos métodos de exportação do `ReportGenerator`.

## Dicas

- Se aparecer erro `ModuleNotFoundError: No module named 'openpyxl'`, instale com:
  ```bash
  pip install openpyxl
  ```
- Sempre ative o ambiente virtual antes de rodar o script.

## Exemplo de saída

O relatório gerado terá colunas como:

- BEES CODE
- Title
- Issue Type
- Number of commits
- Start Date
- Final Date
- Time to Develop (days)
- Story Points
- Status
- Assignee
- Reporter
- Development Commits

---

Se quiser realizar análises estatísticas (média, moda, etc.), basta carregar o CSV gerado com pandas e aplicar os métodos desejados.
