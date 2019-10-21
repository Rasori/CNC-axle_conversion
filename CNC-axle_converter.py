# Tekijä: Waltteri Koskinen
# Milloin: 24.03.2019
# Miksi: Roni soitti hikisenä
# Mitä ohjelma tekee:  ohjelma lukee nc koodin ja muuttaa x-akselin lukemia
# kaksinkertaisiksi. Huomaa kuitenkin, että syötät ohjelmalle vain sen osan
# tiedostosta, joka sisältää ainoastaan koordinaatteja.
# This program is dedicated to the public domain under the GPLv3 license.
#
# V1.0
#           Working at the moment


def akselimuunnos(vanhatiedosto, tiedosto):
    vanhatiedosto = open(vanhatiedosto, mode='r')
    tiedosto = open(tiedosto, mode='w')
    akselit = ['X', 'C', 'K', 'I', 'J', 'F']

    for row in vanhatiedosto:
        row = row.rstrip('\n')
        if 'I' in row:
            alkupaa, x_arvo = row.split('I')
            loppupaa = ''
            akseli = ''
            if 'F' or 'K' or 'J' or 'I' or 'C' in x_arvo:
                for i in akselit:
                    try:
                        print(i)
                        x_arvo, loppupaa = x_arvo.split(i)
                        akseli = i
                        break
                    except ValueError:
                        continue

                x_arvo = float(x_arvo)
                x_arvo = 2 * x_arvo
                print(f'{alkupaa}X{x_arvo}{akseli}{loppupaa}', file=tiedosto)
            else:
                x_arvo = float(x_arvo)
                x_arvo = 2 * x_arvo
                print(f'{alkupaa}X{x_arvo}', file=tiedosto)
        else:
            print(row, file=tiedosto)

    return


def main():

    vanhatiedosto = input('Syötä alkuperäisen tiedoston nimi: ')
    tiedosto = input('Syötä luotavan tiedoston nimi: ')

    akselimuunnos(vanhatiedosto, tiedosto)
    return


main()
