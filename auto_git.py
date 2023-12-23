import os
from datetime import datetime

def git_auto_commit_push(repo_path, commit_message):

    print(f"system INFO:\t start git process.")

    try:

        os.chdir(repo_path)

        os.system('git add .')

        os.system(f'git commit -m "{commit_message}"')

        os.system('git push origin main')

        print("\nsystem OK:\t git commit and push successful!")

    except Exception as e:

        print(f"system DETAIL:\t {e}")

# git_repo_path = input("Enter the path to your Git repository: ")
git_repo_path = "D:\Code\GitHub\zongzongchu0408@gmail.com\Python_NUCT_WAL_auto_connect"

# commit_message = input("Enter the commit message: ")
current_time = datetime.now()
commit_message = formatted_time = current_time.strftime("%Y/%m/%d %H:%M")

git_auto_commit_push(git_repo_path, commit_message)