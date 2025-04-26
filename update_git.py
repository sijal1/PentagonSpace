import os
import subprocess

REPO_PATH = r"D:\pentagonspace"

os.chdir(REPO_PATH)

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Daily update"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("Git repository updated successfully!")
except subprocess.CalledProcessError as e:
    print("Error running Git commands:", e)
