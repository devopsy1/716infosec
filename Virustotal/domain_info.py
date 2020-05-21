import requests

headers = {'x-apikey': '74e64c842978dc210fc9c2c1b47230afbdf113a822938bdd591d2a3a3c236f0c'}

response = requests.get('https://www.virustotal.com/api/v3/domains/www.secure.bankofamerica.com-login-sign-in-signonv2screen.go.suzukihaiphong.com.vn', headers=headers)

print(response.json())