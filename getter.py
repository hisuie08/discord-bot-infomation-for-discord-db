import requests
import base64
import os
PATH = os.path.dirname(os.path.abspath(__file__))


def load_git_token():
    with open(PATH + "/token.txt") as t:
        return t.read()


GITHUB_TOKEN = load_git_token()


def getter(org, repo, branch):
    branch = "main"  # デフォルトブランチ名master時代のリポジトリは注意
    url = f"http://api.github.com/repos/{org}/{repo}/content/bot.json "
    res = requests.get(url, headers={
                       'Authorization': f'token {GITHUB_TOKEN}'}, params={"ref": branch})
    res.raise_for_status()
    base64Data = res.json()["content"]
    print(base64Data)
    return


getter()
