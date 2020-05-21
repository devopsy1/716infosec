import requests

response = requests.get('https://www.virustotal.com/api/v3/files/8739c76e681f900923b900c9df0ef75cf421d39cabb54650c4b9ad19b6a76d85', auth=('X-Apikey', '74e64c842978dc210fc9c2c1b47230afbdf113a822938bdd591d2a3a3c236f0c'))

print(response.json())