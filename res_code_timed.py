import time
import res_code

def main():
    n = int(input('How many rounds?:'))

    if n < 1:
        return

    start = time.time()
    score = 0
    for _ in range(n):
        score += res_code.main()

    print('FINISH')
    print('Score: ', f'{score}/{n}')

    duration = time.time() - start
    avg_duration = duration/n
    avg_correct = duration/score if score != 0 else 0
    
    print('Time:', '{:.3f}s'.format(duration))
    print('Average Time:', '{:.3f}s/qn'.format(avg_duration))
    print('Accuracy:', '{:.3f}s/correct'.format(avg_correct))

if __name__ == '__main__':
    main()
