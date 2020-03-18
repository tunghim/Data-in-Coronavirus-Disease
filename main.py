import os
import requests

with open('raw api.txt') as f:
  urlList = f.readlines()

i = 1
for url in urlList:
    url = url.rstrip('\n')
    print(url)
    response = requests.get(url)
    with open(os.path.join("output", "file_" + str(i) + '.csv'), 'wb') as f:
        f.write(response.content)
    i = i + 1
