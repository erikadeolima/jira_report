class Issue:
    def __init__(self, key: str, summary: str, status: str, assignee: str, data_inicio=None, data_final=None, num_commits=0, dias_desenvolvimento=0, story_points=0, issue_type="", reporter="", development_commits=0):
        self.key = key
        self.summary = summary
        self.status = status
        self.assignee = assignee
        self.data_inicio = data_inicio
        self.data_final = data_final
        self.num_commits = num_commits
        self.dias_desenvolvimento = dias_desenvolvimento
        self.story_points = story_points
        self.issue_type = issue_type
        self.reporter = reporter
        self.development_commits = development_commits 