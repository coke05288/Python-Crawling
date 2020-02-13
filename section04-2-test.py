import json
import requests

url = "https://jsonplaceholder.typicode.com/posts"

s = requests.Session()
r = s.get(url, stream=True)

if r.encoding is None:
    r.encoding = 'UTF-8'

for line in r.json():
    # print(type(line))

    for k, v in line.items():
        print("Key : {} \nValue : {}".format(k, v))
    print()
    print()

s.close()