import requests


url_base = 'https://python.gel.ulaval.ca/quoridor/api'

rep = requests.get('{}/lister/'.format(url_base), params={'idul': 'yabel34'})
if rep.status_code == 200:
    rep = rep.json()
    print(rep)  
else:
    print("Le GET sur '{}lister' a produit le code d'erreur {}".format(
        url_base, erp.status_code)
    )

