#Objective: Automate old log cleanup safely. The team wants to automatically identify logs older than 
# a configurable number of days, 
# archive them into a .tar.gz, and remove the originals only after successful archiving.


# 

from pathlib import Path
import os
from datetime import datetime
import tarfile

log_dir = Path('/home/yuvaraj/log-lab')

files_to_archive = []

curr_time = datetime.now()
#Opening archieve
with tarfile.open("files_to_archieve_latest.tar.gz", "w:gz") as tar: 

    for file in log_dir.rglob("*.log"):    
        mod_time = datetime.fromtimestamp(file.stat().st_mtime)        
        updated_log = curr_time - mod_time
        log_days = updated_log.days
        print(log_days)
        if log_days >= 20:
            tar.add(file)
            files_to_archive.append(file)

with tarfile.open("files_to_archieve_latest.tar.gz", "r:gz") as tar:
    file_names = tar.getnames()
    print(file_names)    

# expected = [str(file) for file in files_to_archive]

expected = [str(file).lstrip("/") for file in files_to_archive]

# expected = []

# for file in files_to_archive:
#     expected.append(str(file))

print(expected)

if expected == file_names:
    for file in files_to_archive:
        file.unlink()