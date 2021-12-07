from django.http import response
from django.shortcuts import render
import json
import requests

def index(request):
    url = "https://ddragon.leagueoflegends.com/cdn/11.21.1/data/en_US/champion.json"
    response = requests.get(url)
    json_data = response.content
    datas = json.loads(json_data)
    champions = list()
    champion = dict()
    for data in datas['data']:
        champion['name'] = data
        imageUrl = f"http://ddragon.leagueoflegends.com/cdn/11.23.1/img/champion/{data}.png"
        champion['image'] = imageUrl
        champions.append(champion.copy())
    
    context = {'champions' : champions}

    return render(request, 'OP_GG2/index.html', context)
    




