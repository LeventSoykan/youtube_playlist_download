import os
import re

files = os.listdir()
for file in files:
  if not file.endswith('.py'):
    search = re.search(r'\d+',file)
    res = search.group()
    while len(res) < 3:
      res = '0' + res
    end = search.end()
    new_filename = res + file[end:]
    os.rename(file, new_filename)

