import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6d27fc99ea4819c1b1dd88b9c277e2fc'
HEADER = {'Content_Type':'application/json', 'trainer_token':TOKEN}

body_created_pokemon = {
    "name": "Бульбазавр",
    "photo_id": 5
}

body_rename_pokemon = {
    "pokemon_id": "122759",
    "name": "Maison",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": "122759"
}

'''response_created = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_created_pokemon)'''
'''print(response_created.text)'''

'''message = response_created.json()['message']'''
'''print(message)'''

'''response_rename_pokemon = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename_pokemon)'''
'''print(response_rename_pokemon)'''

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball)