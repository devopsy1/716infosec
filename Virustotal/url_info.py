import requests

url = 'https://www.virustotal.com/api/v3/urls/30a7c3645e4b009a32c854b830656166c71c00e08e2e7a74264026747bb67a72'
params = {'key': '74e64c842978dc210fc9c2c1b47230afbdf113a822938bdd591d2a3a3c236f0c'}

response = requests.get(url, params=params)

print(response.json())