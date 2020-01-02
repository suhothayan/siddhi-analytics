import requests
from requests.auth import HTTPBasicAuth


class HttpClient:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def get_issues(self, page, repo, type="all"):
        """
        Input
         repo: Repo Name
         type: 'all' or 'new' or 'old' (less than 2018-01-01)
        """
        if type == "all":
            URL = f"https://api.github.com/search/issues?page={page}&per_page=100&q=repo:siddhi-io/{repo}"
        elif type == "new":
            URL = f"https://api.github.com/search/issues?page={page}&per_page=100&q=repo:siddhi-io/{repo}+created:%3C2018-01-01"
        else:
            URL = f"https://api.github.com/search/issues?page={page}&per_page=100&q=repo:siddhi-io/{repo}+created:%3E%3D2018-01-01"

        r = requests.get(url=URL, auth=HTTPBasicAuth(self.user_name, self.password))
        return r.json()

    def get_repos(self):
        URL = "https://api.github.com/users/siddhi-io/repos"
        r = requests.get(url=URL, auth=HTTPBasicAuth(self.user_name, self.password))
        data = r.json()
        repos = list()
        for repo in data:
            repos.append(repo['name'])
        print(f"Repos: {repos}")
        return repos
