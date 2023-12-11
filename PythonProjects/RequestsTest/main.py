import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
               json={
     "name": "Baby John",
     "photo": "https://dolnikov.ru/pokemons/albums/039.png"
},
headers={'Content-Type': 'application/json', 'trainer_token': '1a497fc6525c26e3b3ac4b11742b75be'}, timeout=5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.json} ')

response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
               json={
     "pokemon_id" : "21383",
     "name": "Baby Tom",
     "photo": "https://dolnikov.ru/pokemons/albums/039.png"
},
headers={'Content-Type': 'application/json', 'trainer_token': '1a497fc6525c26e3b3ac4b11742b75be'}, timeout=5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.json} ')

response = requests.post(url='https://api.pokemonbattle.me:9104//trainers/add_pokeball',
              json={
    "pokemon_id" : "21383",
},
headers={'Content-Type': 'application/json', 'trainer_token': '1a497fc6525c26e3b3ac4b11742b75be'}, timeout=5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.json} ')
