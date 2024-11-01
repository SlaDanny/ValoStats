#encontrar o PUUID
# import requests

# api_key = "RGAPI-d8c05a12-3ccd-4a80-84cc-1a62eae7b636"
# url = "https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/grac 寒/cold"

# headers = {
#     "X-Riot-Token": api_key
# }

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     player_data = response.json()
#     puuid = player_data.get("puuid")
#     print("PUUID do jogador:", puuid)
# else:
#     print(f"Erro na requisição: {response.status_code}")


#obter rank
# import requests

# api_key = "RGAPI-d8c05a12-3ccd-4a80-84cc-1a62eae7b636"
# puuid = "HXF_d_2P_tFYPUxNfCjZdUaCvx0pOLdNOpNFVRJz4-UHVIwk2Ce4RPHtNJsLtYkLWIOuHWTz7rWYcQ"  
# url = f"https://eu.api.riotgames.com/val/ranked/v1/by-act/d1ad9e7a-4e3f-e8c6-eb1b-148162a5acf7/players/{puuid}"

# headers = {
#     "X-Riot-Token": api_key
# }

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     rank_data = response.json()
#     print(rank_data)
# else:
#     print(f"Erro na requisição: {response.status_code}")

# obter os atos
# import requests

# api_key = "sua-api-key"
# # Endpoint de Conteúdo da API do Valorant
# url = "https://eu.api.riotgames.com/val/content/v1/contents"

# # Cabeçalho com a chave de API
# headers = {
#     "X-Riot-Token": api_key
# }

# # Fazendo a requisição
# response = requests.get(url, headers=headers)

# # Verifica se a requisição foi bem-sucedida
# if response.status_code == 200:
#     data = response.json()
#     if "acts" in data:
#         # Itera sobre os atos e imprime o nome e ID
#         for act in data['acts']:
#             print(f"Nome do Ato: {act['name']}, ID do Ato: {act['id']}")
#     else:
#         print("A resposta não contém dados de 'acts'.")
# else:
#     print(f"Erro na requisição: {response.status_code}")


import requests

# Defina a sua chave da API
api_key = "RGAPI-9e6fed6a-6bd4-4477-bbb6-474576faffdc"

# Dados do jogador 
game_name = "grac 寒"  # o nome do jogador
tag_line = "cold"    # a tagline do jogador

# Endpoint para obter o PUUID do jogador
puuid_url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"

# Cabeçalho da requisição
headers = {
    "X-Riot-Token": api_key
}

# Fazer a requisição para obter o PUUID
response = requests.get(puuid_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    puuid = data["puuid"]
    print("PUUID:", puuid)

    # Obter o Act ID
    acts_url = "https://europe.api.riotgames.com/val/competitiveness/v1/acts"
    acts_response = requests.get(acts_url, headers=headers)

    if acts_response.status_code == 200:
        acts_data = acts_response.json()
        current_act_id = acts_data[-1]['id']  # Pega o último ato como exemplo
        print("Current Act ID:", current_act_id)

        # Endpoint para obter o rank e outros detalhes do jogador
        rank_url = f"https://europe.api.riotgames.com/val/ranked/v1/leaderboards/by-act/{current_act_id}?puuid={puuid}"
        
        # Fazer a requisição para obter o rank
        rank_response = requests.get(rank_url, headers=headers)

        if rank_response.status_code == 200:
            rank_data = rank_response.json()
            print("Rank Data:", rank_data)
        else:
            print("Erro ao obter o rank:", rank_response.status_code)
    else:
        print("Erro ao obter os atos:", acts_response.status_code)
else:
    print("Erro ao obter o PUUID:", response.status_code)


