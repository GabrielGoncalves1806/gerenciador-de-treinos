import json

def get_muscle_sprite(grupo_muscular):
    try:
        with open("data/sprites.json","r") as data:
            sprites = json.load(data)
            return sprites[grupo_muscular.lower()]
    except:
        return 'spite não encontrada'
