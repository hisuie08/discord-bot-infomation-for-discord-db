import base64
import json
import os

import requests

PATH = os.path.dirname(os.path.abspath(__file__))


def load_git_token():
    with open(PATH + "/token.txt") as t:
        return t.read()


GITHUB_TOKEN = load_git_token()


def getter(org: str, repo: str, branch="main") -> json:
    # デフォルトブランチ名master時代のリポジトリは注意
    url = f"http://api.github.com/repos/{org}/{repo}/contents/bot.json"
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}'
    }
    params = {"ref": branch}
    res = requests.get(url, headers=headers, params=params)
    res.raise_for_status()
    rawBotData = str(res.json()["content"]).replace("\n", "")
    jsonBotData = json.loads(base64.b64decode(rawBotData).decode("utf-8"))
    return jsonBotData
