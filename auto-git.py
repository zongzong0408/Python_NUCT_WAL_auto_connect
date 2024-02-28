from datetime import datetime
import time
import sys
import os

def git_commit_push(repo_path, commit_message) -> None:

    sys.stdout.write(f"\n\n\nsystem INFO:\t start git process.\n")

    try:

        os.chdir(repo_path)
        os.system("git add .")
        os.system(f"git commit -m '{commit_message}'")
        os.system("git push origin main")
        
        sys.stdout.write("\nsystem OK:\t git commit and push successful!")

    except Exception as e:

        sys.stdout.write(f"system DETAIL:\t {e}")

    else:

        return

def main() -> None:

    while (True):

        git_repo_path   = os.getcwd()

        current_time    = datetime.now()
        commit_message  = current_time.strftime("%Y/%m/%d %H:%M")

        git_commit_push(git_repo_path, commit_message)

        time.sleep(5)

    # return

main()