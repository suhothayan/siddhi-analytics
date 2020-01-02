from HttpClient import HttpClient

external_users = set()
external_contributions = 0
external_issues = 0
external_prs = 0
employee_contributions = 0
employee_issues = 0
employee_prs = 0
x_employee_contributions = 0
x_employee_issues = 0
x_employee_prs = 0

employees = ['suhothayan', 'mohanvive', 'niveathika', 'RAVEENSR', 'ramindu90', 'sayshika', 'lasanthaS',
             'harsha89', 'RukshiW', 'miyurud', 'ashensw', 'nirmal070125', 'dnwick', 'sajithshn', 'keizer619',
             'praminda', 'nadundesilva', 'tishan89', 'niruhan', 'pcnfernando', 'vithu30', 'dilini-muthumala',
             'hemikak', 'AnuGayan', 'kalaiyarasiganeshalingam', 'grainier', 'gimantha', 'CharukaK', "suganyasuven",
             'dependabot-preview[bot]', 'Methma', 'senthuran16', 'sahandilshan', 'BuddhiWathsala', 'dunithd',
             'ramith', 'PrabodDunuwila', 'dushaniw', 'pamodaaw', 'Meruja', 'gomathyk', 'shafanaS', 'erangatl',
             'chaminda', 'madurangasiriwardena']

x_employees = ['rajeev3001', 'lasanthafdo', 'ayash', 'minudika', 'Yasara123', 'ChariniNana', 'Anoukh', 'thiliA',
               'ChathurikaA', 'slgobinath', 'gokul', 'ksdperera', 'this', 'NisalaNiroshana', 'manoramahp', 'sacjaya',
               'lgobinath']


def analyse(http_client, repo, type="all"):
    """
    Input
     repo: Repo Name
     type: 'all' or 'new' or 'old' (less than 2018-01-01)
    """

    global external_contributions
    global external_issues
    global external_prs
    global employee_contributions
    global employee_issues
    global employee_prs
    global x_employee_contributions
    global x_employee_issues
    global x_employee_prs

    data = http_client.get_issues(1, repo, type)
    total_count = int(data['total_count'])
    print(f"Repo:{repo} total_count:{total_count}")
    pages = int(abs(total_count / 100) + 1)
    for page in range(1, pages + 1):
        if page != 1:
            data = http_client.get_issues(page, repo, type)
        try:
            items = data['items']
            for item in items:
                name = item['user']['login']
                if name in employees:
                    employee_contributions += 1
                    if 'pull_request' in item:
                        employee_prs += 1
                    else:
                        employee_issues += 1
                elif name in x_employees:
                    x_employee_contributions += 1
                    if 'pull_request' in item:
                        x_employee_prs += 1
                    else:
                        x_employee_issues += 1
                else:
                    external_users.add(name)
                    external_contributions += 1
                    if 'pull_request' in item:
                        external_prs += 1
                    else:
                        external_issues += 1
        except:
            print(f"Items not found for repo:{repo} on page:{page} on data: {data}")
            break


if __name__ == "__main__":
    user_name = input("GitHub Username\n")
    password = input("GitHub Token\n")
    http_client = HttpClient(user_name, password)
    repos = http_client.get_repos()
    for repo in repos:
        if repo != 'siddhi':
            analyse(http_client, repo)
        else:
            analyse(http_client, repo, "old")
            analyse(http_client, repo, "new")

    print(f"External Contributors: {external_users}")
    print(
        f"Employees: {len(employees)} Contributions:{employee_contributions} Issues:{employee_issues} PRs:{employee_prs} ")
    print(
        f"X-Employees: {len(x_employees)} Contributions:{x_employee_contributions} Issues:{x_employee_issues} PRs:{x_employee_prs} ")
    print(
        f"External Contributors: {len(external_users)} Contributions:{external_contributions} Issues:{external_issues} PRs:{external_prs} ")
