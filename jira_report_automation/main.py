from .jira_client import JiraClient
from .report_generator import ReportGenerator

if __name__ == "__main__":
    client = JiraClient()
    # JQL para buscar todas as issues atribuídas ao usuário atual e de tipos padrão
    jql = "assignee = currentUser() AND issuetype in standardIssueTypes() ORDER BY created DESC"
    issues = client.buscar_issues(jql)
    generator = ReportGenerator(issues)
    generator.gerar_relatorio() 