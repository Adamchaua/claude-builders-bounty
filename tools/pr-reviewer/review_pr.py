import sys
import os
import requests
import json

def get_pr_diff(repo, pr_number, token):
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3.diff"
    }
    response = requests.get(url, headers=headers)
    return response.text

def review_diff(diff_text):
    # In a real implementation, this would call an LLM (Claude/GPT)
    # Here we provide a structured template for the AI to fill
    review = "# PR Review Summary\n\n"
    review += "## 🚀 Overview\nBriefly explain what this PR does based on the diff.\n\n"
    review += "## ⚠️ Risks & Security\n- List potential bugs, security flaws, or breaking changes.\n\n"
    review += "## 💡 Suggestions\n- Provide specific code improvements or refactoring ideas.\n\n"
    review += "## ✅ Testing Notes\n- Suggest what the reviewer should test manually.\n"
    return review

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python review_pr.py <owner/repo> <pr_number>")
        sys.exit(1)
    
    repo = sys.argv[1]
    pr_num = sys.argv[2]
    token = os.getenv("GITHUB_TOKEN")
    
    if not token:
        print("Error: GITHUB_TOKEN environment variable is not set.")
        sys.exit(1)
        
    diff = get_pr_diff(repo, pr_num, token)
    print(review_diff(diff))
