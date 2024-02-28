from datetime import datetime
import time
import sys
import os

AUTO_GIT_WAIT_TIME = 30

def git_commit_push(repo_path, commit_message) -> None:

    sys.stdout.write("----------------------------------------------\n")
    sys.stdout.write(f"system INFO:\t start git process.\n\n")

    try:

        os.chdir(repo_path)
        os.system("git add .")
        os.system(f'git commit -m "{commit_message}"')
        os.system("git push origin main")
        
        sys.stdout.write("\n\nsystem OK:\t git commit and push successful!\n")
        sys.stdout.write("----------------------------------------------\n\n\n\n")

    except Exception as e:

        sys.stdout.write(f"system DETAIL:\t {e}\n")
        sys.stdout.write("----------------------------------------------\n\n\n\n")

    else:

        return

def main() -> None:

    git_repo_path = os.getcwd()

    times = 1

    while (True):

        current_time = datetime.now()
        commit_message = current_time.strftime("%Y/%m/%d %H:%M")

        sys.stdout.write("----------------------------------------------\n")
        sys.stdout.write(f"system INFO:\t auto git times is: {times}\n")
        sys.stdout.write(f"system INFO:\t now times is: {commit_message}\n")

        git_commit_push(git_repo_path, commit_message)

        time.sleep(AUTO_GIT_WAIT_TIME)

        times += 1

    # return

main()