import requests

url = "https://www.ontarioImmigration.gov.on.ca/register_enu/dynamicform/register/start"
url2 = "https://www.ontarioimmigration.gov.on.ca/register_enu/dynamicform/register/launch/JOFW"

haha = requests.get(url2)
print(haha.text)