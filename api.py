import requests
import json


def lister_parties(idul):
    """
    (Qu'est-ce que fait ma fonction?)
    (Quels sont les paramètres en entrée de ma fonction) idul
    (Quelle est la sortie et/ou le retour de ma fonction)
    """
    url_lister = 'https://python.gel.ulaval.ca/quoridor/api/lister/'
    donnees = requests.get(url_lister, params={'idul': idul})
    if donnees.status_code == 200:
        donnees = donnees.text
        json_x = json.loads(donnees)
        json_y = json.dumps(json_x, indent=2)
        print(json_y)  
    else:
        print("Le GET sur '{}' a produit le code d'erreur {}".format(
            url_lister, donnees.status_code)
        )

