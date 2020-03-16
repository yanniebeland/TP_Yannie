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

def initialiser_partie(idul):
    """
    (Qu'est-ce que fait ma fonction?)
    (Quels sont les paramètres en entrée de ma fonction) idul
    (Quelle est la sortie et/ou le retour de ma fonction)
    """
    url_debut = 'https://python.gel.ulaval.ca/quoridor/api/initialiser/'
    try:
        donnees = requests.post(url_debut, data={'idul': idul})
        if donnees.status_code == 200:
            json_donnees = donnees.json()
            return json_donnees['id'], json_donnees['état']
        else:
            print("Le POST sur '{}' a produit le code d'erreur {}".format(
                url_debut, donnees.status_code)
            )
    except RuntimeError as error:
        print(error)

def jouer_coup(id_partie, type_coup, position):
    url_coup = 'https://python.gel.ulaval.ca/quoridor/api/jouer/'
    try:
        response = requests.post(url_coup, data={'id': id_partie, 'type': type_coup, 'pos': position})
        if response.status_code == 200:
            json_res = response.json()
            return json_res
        else:
            print("Le POST sur '{}' a produit le code d'erreur {}.".format(
                url_coup, response.status_code)
            )
    except RuntimeError as error:
        print(error)
