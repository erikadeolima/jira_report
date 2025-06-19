from .issue import Issue
from typing import List
import pandas as pd

class ReportGenerator:
    def __init__(self, issues: List[Issue]):
        self.issues = issues

    def gerar_relatorio(self):
        data = []
        for issue in self.issues:
            data.append([
                issue.key,
                issue.summary,
                issue.issue_type,
                issue.num_commits,
                issue.data_inicio,
                issue.data_final,
                issue.dias_desenvolvimento,
                issue.story_points,
                issue.status,
                issue.assignee,
                issue.reporter,
                issue.development_commits
            ])
        df = pd.DataFrame(data, columns=[
            'BEES CODE', 'Title', 'Issue Type', 'Number of commits',
            'Start Date', 'Final Date', 'Time to Develop (days)', 'Story Points',
            'Status', 'Assignee', 'Reporter', 'Development Commits'
        ])
        df = df.fillna('')
        df.to_csv('/Users/erikalima/Documents/all_tasks_developed_by_erika_lima.csv', index=False)
        df.to_excel('/Users/erikalima/Documents/all_tasks_developed_by_erika_lima.xlsx', index=False)
        print("Dados salvos em all_tasks_developed_by_erika_lima.csv e .xlsx")
        print(df) 