import requests


url = 'https://akabab.github.io/superhero-api/api/all.json'

r = requests.get(url)

heroes = {'Hulk': 0,
          'Captain America': 0,
          'Thanos': 0}

for item in r.json():
    for hero in heroes:
        if hero == item['name']:
            heroes.update({item['name']: item['powerstats']['intelligence']})

hero_intelligence = max(heroes.items(), key=lambda x: x[1])

print(hero_intelligence)