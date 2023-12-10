import os
import re

files = os.listdir()
for file in files:
	if not file.endswith('.py'):
		search = re.search(r'Ep[\s]?\d{1}', file)
		if search:
			start = search.start()
		else:
			start = 0
		os.rename(file, file[start:])

