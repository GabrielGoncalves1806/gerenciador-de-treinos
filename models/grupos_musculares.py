import json 

def get_grupos():
    with open("data/grupos_musculares.json","r") as grupos:
        return json.load(grupos)