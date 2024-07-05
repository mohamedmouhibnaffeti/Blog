import schedule
import time
import subprocess
from datetime import datetime

# Function to add, commit, and push changes
def git_commit_push():
    try:
        # Add all changes
        subprocess.run(["git", "add", "."], check=True)

        # Commit changes with a timestamp message
        commit_message = f"Fixed issue"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push changes to the remote repository
        subprocess.run(["git", "push", "-u", "-f", "origin", "master"], check=True)

        print(f"Changes committed and pushed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Schedule the job every minute
schedule.every(5).seconds.do(git_commit_push)

print("Starting the scheduler...")
while True:
    schedule.run_pending()
