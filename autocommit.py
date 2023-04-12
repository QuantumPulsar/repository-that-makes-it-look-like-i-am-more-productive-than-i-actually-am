import os
from datetime import datetime

# with open("README.md", "r+") as file:
#     lines = file.readlines()
#     last_line = lines[-1].strip()
#     newday = int(last_line[-2:-1])+1
#     newline = f"# Days of lying about my productivity [{str(newday)}]"
#     lines[-1] = newline
#     file.seek(0)
#     file.writelines(lines)
#     file.close
now = datetime.now()
date_time_str = now.strftime("%D-%M-%Y-%H:%M:%S")
os.system("git add *")
os.system("git commit -m{0}".format(f"{date_time_str}"))