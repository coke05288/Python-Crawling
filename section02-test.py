import urllib.request as req
import requests

response1 = req.urlopen("http://www.naver.com")
print("response1 : {}".format(response1))
print("response1 Info : {}".format(response1.info()))
print("response1 HTTP : {}".format(response1.getcode()))

print("=============================================================")

response2 = requests.get("http://www.naver.com")
print("response2 : {}".format(response2))
print("response2 : {}".format(response2.headers))
