import requests

auth = ('key', 'p4Pt8hUyi9Jkm21YnjtM4fjAqe0qyLUpk6Q7GC0QCZth5sDEjbsZtjpHLhM5zhjE')

response = requests.get('https://api.greynoise.io/v2/noise/multi/quick?ips=71.6.135.131,71.6.135.132', auth=auth)

print(response.json())