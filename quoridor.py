import argparse
import api


# État de jeu donné dans l'énoncé du travail (utilisé pour tester la fonction 2).
#jeu_prof = {
    #"joueurs": [
        #{"nom": "idul", "murs": 7, "pos": [5, 5]},
        #{"nom": "automate", "murs": 3, "pos": [8, 6]}
    #],
    #"murs": {
        #"horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
        #"verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]
    #}
#}

# Fonction 1.
# La fonction sert à recevoir les commandes argparse
# d'un terminal. De plus, elle ne prend rien en entrée
# et retourne un objet parser contenant les commandes appelées.

def analyser_commande():
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 1')
    parser.add_argument('IDUL', metavar='IDUL',
                        default='yabel34', help="IDUL du joueur")
    parser.add_argument('-l', '--lister', dest='liste',
                        help='Lister les identifiants de vos 20 dernières parties.')
    return parser.parse_args()

# Fonction 2.
# La fonction ci-dessous permet de, à chaque coup, afficher
# le damier complet de l'état de jeu actuel pour que le
# prochain jouer puisse prévoir son coup. Cette fonction
# accepte en entrée un dicitonnaire (état_de_jeu) contenant
# toutes les infos de l'état du jeu actuel pour pouvoir
# l'afficher en sortie. Ainsi, cette fonction ne retourne
# rien, mais affiche le damier de l'état de jeu actuel
# (pions et murs placés aux bons endroits selon le
# déroulement de la partie). En première ligne de ma
# fonction, j'ai indiqué que ma matrice de jeu devra
# afficher un certain nombre de colonnes et de lignes,
# mais qu'elle devra également présenter le chiffre
# associé à chacune des lignes/colonnes pouvant
# accueillir un pion (d'où la variable 'jeu').

def afficher_damier_ascii(etat_de_jeu):
    jeu, colonne, ligne = [], [], []
    for i in range(9):
        mat_jeu, mat_colonne, mat_ligne = [], [], []
        for j in range(9):
            mat_jeu.append('.')
            mat_colonne.append(' ')
            mat_ligne.append('   ')
        jeu.append(mat_jeu)
        colonne.append(mat_colonne)
        ligne.append(mat_ligne)
    posi_j_1 = etat_de_jeu['joueurs'][0]['pos']
    posi_j_2 = etat_de_jeu['joueurs'][1]['pos']
    jeu[posi_j_1[1] - 1][posi_j_1[0] - 1] = '1'
    jeu[posi_j_2[1] - 1][posi_j_2[0] - 1] = '2'
    jeu.reverse()

    for a, b in etat_de_jeu['murs']['horizontaux']:
        ligne[b - 1][a - 1] = '---'
    ligne.reverse()

    for a, b in etat_de_jeu['murs']['verticaux']:
        colonne[b - 1][a - 1] = '|'
    colonne.reverse()
    sortie = "Légende: 1={}, 2=automate\n".format(etat_de_jeu['joueurs'][0]['nom'])
    sortie += "   -----------------------------------\n"
    for i in range(9):
        if i == 8:
            sortie += "1 |"
            sortie += "{}{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}  ".format(
                colonne[8][0], jeu[8][0],
                colonne[8][1], jeu[8][1],
                colonne[8][2], jeu[8][2],
                colonne[8][3], jeu[8][3],
                colonne[8][4], jeu[8][4],
                colonne[8][5], jeu[8][5],
                colonne[8][6], jeu[8][6],
                colonne[8][7], jeu[8][7],
                colonne[8][8], jeu[8][8],
            )
            sortie = sortie[:-1]
            sortie += "|\n"
        else:
            sortie += "{} |".format(9 - i)
            sortie += "{}{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}  ".format(
                colonne[i][0] if colonne[i + 1][0] != '|' else '|', jeu[i][0],
                colonne[i][1] if colonne[i + 1][1] != '|' else '|', jeu[i][1],
                colonne[i][2] if colonne[i + 1][2] != '|' else '|', jeu[i][2],
                colonne[i][3] if colonne[i + 1][3] != '|' else '|', jeu[i][3],
                colonne[i][4] if colonne[i + 1][4] != '|' else '|', jeu[i][4],
                colonne[i][5] if colonne[i + 1][5] != '|' else '|', jeu[i][5],
                colonne[i][6] if colonne[i + 1][6] != '|' else '|', jeu[i][6],
                colonne[i][7] if colonne[i + 1][7] != '|' else '|', jeu[i][7],
                colonne[i][8] if colonne[i + 1][8] != '|' else '|', jeu[i][8],
            )
            sortie = sortie[:-1]
            sortie += "|\n"
            sortie += "  |"
            sortie += "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(
                ligne[i][0], '-' if ligne[i][0] == '---' else colonne[i + 1 if i < 8 else 0][1],
                ligne[i][1] if ligne[i][0] != '---' else '---',
                '-' if ligne[i][1] == '---' else colonne[i + 1 if i < 8 else 0][2],
                ligne[i][2] if ligne[i][1] != '---' else '---',
                '-' if ligne[i][2] == '---' else colonne[i + 1 if i < 8 else 0][3],
                ligne[i][3] if ligne[i][2] != '---' else '---',
                '-' if ligne[i][3] == '---' else colonne[i + 1 if i < 8 else 0][4],
                ligne[i][4] if ligne[i][3] != '---' else '---',
                '-' if ligne[i][4] == '---' else colonne[i + 1 if i < 8 else 0][5],
                ligne[i][5] if ligne[i][4] != '---' else '---',
                '-' if ligne[i][5] == '---' else colonne[i + 1 if i < 8 else 0][6],
                ligne[i][6] if ligne[i][5] != '---' else '---',
                '-' if ligne[i][6] == '---' else colonne[i + 1 if i < 8 else 0][7],
                ligne[i][7] if ligne[i][6] != '---' else '---',
                '-' if ligne[i][7] == '---' else colonne[i + 1 if i < 8 else 0][8],
                ligne[i][8] if ligne[i][7] != '---' else '---',
                '-' if ligne[i][8] == '---' else colonne[i + 1 if i < 8 else 0][0]
            )
            sortie = sortie[:-1]
            sortie += "|\n"
    sortie += "--|-----------------------------------\n"
    sortie += "  | 1   2   3   4   5   6   7   8   9\n"
    print(sortie)

# Ici, j'ai voulu tester mon programme en initialisant une nouvelle
# partie et en utilisant l'identifiant résultant pour ensuite
# jouer mes coups.

#if __name__ == '__main__':
    #init = api.initialiser_partie('yabel34')
    #print(init)
    #coup = api.jouer_coup('0644ebf8-4eba-4240-b597-eb0376915397', 'D', (5,2))
    #afficher_damier_ascii(coup['état'])
    #print(coup)
