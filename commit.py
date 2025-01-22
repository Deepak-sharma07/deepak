import os
from datetime import datetime
import subprocess

def make_commits(num_commits: int):
    for i in range(num_commits):
        # Get the current date and time for each commit
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Append some text to the file
        with open('data.txt', 'a') as file:
            file.write(f'Commit {i + 1} on {current_date}\n')
        
        # Add the file to the staging area
        subprocess.run(['git', 'add', 'data.txt'], check=True)
        
        # Commit with a unique message for each commit
        subprocess.run(['git', 'commit', '--date', current_date, '-m', f'Commit {i + 1} on {current_date}'], check=True)

    # Push all commits after loop
    subprocess.run(['git', 'push'], check=True)

# Call the function with the desired number of commits
make_commits(100)
