import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 1')
    parser.add_argument('IDUL', metavar='IDUL',
                        default='yabel34', help="IDUL du joueur")
    parser.add_argument('-l', '--lister', dest='liste',
                        help='Lister les identifiants de vos 20 dernières parties.')
    return parser.parse_args()


def main():
    arguments = analyser_commande()


if __name__ == '__main__':
    main()

