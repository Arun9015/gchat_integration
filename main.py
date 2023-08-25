import os
from github import Github
import requests

g = Github(os.environ["GITHUB_TOKEN"])
repo = g.get_repo(os.environ['REPO_NAME'])
event = os.environ['EVENT']
# GitHub token with appropriate permissions
# GITHUB_TOKEN = "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"

# Google Chat webhook URL
GCHAT_WEBHOOK_URL = "https://chat.googleapis.com/v1/spaces/AAAAJWnA1jA/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=pfdOLCmNOvrazVV-IkSORjSpmfOs9Kpay03eCZD5xww"

def main():
    pr_number = int(os.environ['PR_NUMBER'])
    pr = repo.get_pull(pr_number)


    message = f"New Pull Request:\nTitle: {pr.title}\nURL: {pr.html_url}"
    payload = {
        "text" : message
    }
    # response = requests.post(GCHAT_WEBHOOK_URL, json=payload)
    # print(response)
    print("workflow is working")
    print(event)

if __name__ == "__main__":
    main()
