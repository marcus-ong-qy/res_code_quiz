import random

COLOURS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
COLOUR_CODES = {
    'black': '232',
    'brown': '131',
    'red': '196',
    'orange': '202',
    'yellow': '226',
    'green': '82',
    'blue': '21',
    'violet': '93',
    'grey': '244',
    'white': '15',
}

def get_colour_block(colour):
    return f'\u001b[38;5;{COLOUR_CODES[colour]}m \u2588 \033[00m'

def main():
    c1 = random.randint(1,9)
    c2 = random.randint(0,9)
    m = random.randint(0,9)

    number = (c1*10 + c2) * 10**m

    print(
        get_colour_block(COLOURS[c1]), 
        get_colour_block(COLOURS[c2]), 
        get_colour_block(COLOURS[m])
    )

    value = input('\nValue?: ')
    print()

    if int(value) == number:
        print('Correct!')
        return 1

    print('Wrong')   
    print('Number is', '{:,}'.format(number))
    return 0

if __name__ == '__main__':
    while True:
        main()
