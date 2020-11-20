import requests


url = 'https://api.zt.kuaishou.com/rest/zt/captcha/sliding/config'
result = requests.post(url)
print(result.text)