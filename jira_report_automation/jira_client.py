import requests
from .config import JIRA_URL, JIRA_USER, JIRA_TOKEN
from .issue import Issue
from datetime import datetime

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"

class JiraClient:
    def __init__(self):
        self.base_url = JIRA_URL
        self.auth = (JIRA_USER, JIRA_TOKEN)
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def buscar_issues(self, jql: str):
        url = f"{self.base_url}/rest/api/3/search"
        issues = []
        start_at = 0
        max_results = 50
        total = None
        while True:
            params = {
                "jql": jql,
                "startAt": start_at,
                "maxResults": max_results,
                "fields": "summary,status,assignee,customfield_10022,issuetype,reporter,development"
            }
            response = requests.get(url, headers=self.headers, params=params, auth=self.auth)
            if response.status_code != 200:
                print(f"Erro ao buscar issues: {response.status_code}")
                print(response.text)
                break
            data = response.json()
            if total is None:
                total = data["total"]
                print(f"Total de issues encontradas: {total}")
            for idx, issue in enumerate(data["issues"], start=1+start_at):
                key = issue.get("key", "")
                issue_id = issue.get("id", "")
                fields = issue.get("fields", {})
                summary = fields.get("summary", "")
                status = fields.get("status", {}).get("name", "")
                assignee_field = fields.get("assignee")
                assignee = assignee_field["displayName"] if assignee_field else ""
                reporter_field = fields.get("reporter")
                reporter = reporter_field["displayName"] if reporter_field else ""
                story_points = fields.get("customfield_10022", 0) or 0
                issue_type = fields.get("issuetype", {}).get("name", "")
                # Campo development (API v2), pode não estar presente
                development = fields.get("development", {})
                development_commits = len(development.get("commits", [])) if development and "commits" in development else 0
                print(f"Processando issue {idx}/{total}: {key}")
                # Buscar detalhes de commits (API dev-status)
                num_commits, data_inicio, data_final, dias_desenvolvimento, _ = self.get_issue_commits(issue_id)
                issues.append(Issue(
                    key, summary, status, assignee, data_inicio, data_final, num_commits, dias_desenvolvimento,
                    story_points, issue_type, reporter, development_commits
                ))
            if start_at + max_results >= data["total"]:
                break
            start_at += max_results
        return issues

    def get_issue_commits(self, issue_id):
        url = f"{self.base_url}/rest/dev-status/latest/issue/details?issueId={issue_id}"
        response = requests.get(url, headers=self.headers, auth=self.auth)
        author_emails = set()
        if response.status_code == 200:
            d_myjson = response.json()
            try:
                commits = d_myjson['detail'][-1]['repositories'][0]['commits']
                commits.sort(key=lambda x: x['authorTimestamp'])
                num_commits = len(commits)
                if num_commits > 0:
                    data_inicio = commits[0]['authorTimestamp']
                    data_final = commits[-1]['authorTimestamp']
                    data_inicio_formatada = datetime.strptime(data_inicio, DATE_FORMAT).strftime("%d/%m/%Y")
                    data_final_formatada = datetime.strptime(data_final, DATE_FORMAT).strftime("%d/%m/%Y")
                    datas_commits = set(datetime.strptime(commit['authorTimestamp'], DATE_FORMAT).date() for commit in commits)
                    dias_desenvolvimento = len(datas_commits)
                    for commit in commits:
                        author_email = commit.get('author', {}).get('emailAddress', "")
                        if author_email:
                            author_emails.add(author_email)
                else:
                    data_inicio_formatada = None
                    data_final_formatada = None
                    dias_desenvolvimento = 0
            except (KeyError, IndexError, TypeError):
                num_commits = 0
                data_inicio_formatada = None
                data_final_formatada = None
                dias_desenvolvimento = 0
            return num_commits, data_inicio_formatada, data_final_formatada, dias_desenvolvimento, author_emails
        else:
            print(f"Erro ao buscar commits da issue {issue_id}: {response.status_code}")
            print(response.text)
            return 0, None, None, 0, set() 