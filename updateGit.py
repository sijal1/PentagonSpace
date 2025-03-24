import os
import subprocess

# Set your project directory
repo_path = r"D:\pentagonspace"

# Change to the repository directory
os.chdir(repo_path)

# Run Git commands
try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Daily update"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("✅ Git repository updated successfully!")
except subprocess.CalledProcessError as e:
    print("❌ Error running Git commands:", e)
