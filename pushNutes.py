import os
from datetime import datetime

commitMessage = datetime.today().strftime('Date: %Y-%m-%d || Time: %H:%M:%S')


os.chdir('C:/Users/midhdesk1/Desktop/Send Nutes')
os.system('git add .')
os.system(f'git commit -m "{commitMessage}"')
os.system('git push origin main')

input(print("Pushed the code to GitHub"))