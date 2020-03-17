import requests
import json


# Fonction 3. La fonction permet de lister l'historique de l'ensemble des parties jouées par un joueur sur un serveur. Elle accepte en entrée l'idul du joueur dont on souhaite avoir l'historique des parties. De plus, la fonction ne retourne rien, mais elle affiche à la console un json.

def lister_parties(idul):
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

# Fonction 4. La fonction ci-dessous permet de débuter une nouvelle partie. Elle initialise une partie en acceptant en entrée l'idul du joueur s'apprêtant jouer cette partie. Cette fonction retourne un tuple contenant l'identifiant de la partie et l'état initial du jeu. De plus, en cas d'erreur (message présent dans la réponse, la fonction soulève une exception de type RuntimeError avec le message reçu.

def initialiser_partie(idul):
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

# Fonction 5.
# Cette fonction permet au joueur d'inscrire le prochain coup qu'il souhaite jouer. En effet, cette fonction reçoit comme argument l'identifiant de la partie (déterminé avec la fonction précédente permettant de débuter une nouvelle partie), le type de coup désiré ('D' pour déplacer le jeton, 'MH' pour placer un mur horizontal et 'MV' pour placer un mur vertical) ainsi la position (x, y) du coup. La fonction retourne le damier de l'état de jeu actuel. En cas d'erreur, la fonction retourne une exception de type 'RuntimeError' avec le message reçu préalablement (message d'erreur). De plus, lorsque la partie se termine (lorsqu'un des joueur gagne), la fonction soulève une exception de type StopIteration avec le nom du gagnant comme message.

def jouer_coup(id_partie, type_coup, position):
    url_coup = 'https://python.gel.ulaval.ca/quoridor/api/jouer/'
    try:
        donnees = requests.post(url_coup, data={'id': id_partie, 'type': type_coup, 'pos': position})
        if donnees.status_code == 200:
            json_donnees = donnees.json()
            if 'gagnant' in json_donnees:
                raise StopIteration(json_donnees['gagnant'])
            else:
                return json_donnees
        else:
            print("Le POST sur '{}' a produit le code d'erreur {}.".format(
                url_coup, donnees.status_code)
            )
    except RuntimeError as error:
        print(error)
