import os
from datetime import datetime

# File to be committed
file_path = 'commit_file.txt'

# Create or update the file with the current timestamp
with open(file_path, 'a') as file:
    file.write(f'Commit on {datetime.now()}\n')

# Git commands to add, commit, and push the changes
os.system('git add commit_file.txt')
os.system('git commit -m "Auto commit"')
os.system('git push')
