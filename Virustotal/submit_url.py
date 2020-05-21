import requests

response = requests.post('https://www.virustotal.com/api/v3/urls', auth=('X-Apikey', '74e64c842978dc210fc9c2c1b47230afbdf113a822938bdd591d2a3a3c236f0c'), params=('url', 'www.secure.bankofamerica.com-login-sign-in-signonv2screen.go.suzukihaiphong.com.vn'))

print(response.json())