import argparse


def analyser_commande():
    parser = argparse.ArgumentParser()
    return parser.parse_args()


def main():
    args = analyser_commande()


if __name__ == '__main__':
    main()

