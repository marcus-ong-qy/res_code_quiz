import random

COLOURS_ABBR = ['bk', 'br', 're', 'or', 'ye', 'gr', 'bl', 'vi', 'gy', 'wh']

def main():
    c1 = random.randint(1,9)
    c2 = random.randint(0,9)
    m = random.randint(0,9)

    number = (c1*10 + c2) * 10**m

    print('{:,}'.format(number))

    value = input('\nValue?: ')
    value = value.split(' ')
    print()

    answer = [COLOURS_ABBR[c1], COLOURS_ABBR[c2], COLOURS_ABBR[m]]

    if value == answer:
        print('Correct!')
    else:
        print('Wrong')   
        print('Answer is', answer)

if __name__ == '__main__':
    while True:
        main()
