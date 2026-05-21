import multiprocessing
import random
import time

# Distância máxima da corrida
DISTANCIA_MAX = 50         #de exemplo, pode ser qualquer distância para ser a distância máxima

# Tamanho máximo do salto
SALTO_MAX = 5       #determinado pelo exercício

posicao: None
semaforo = None

def init(s, p):
    global semaforo, posicao

    semaforo = s
    posicao = p

def corrida(nome):
    global posicao, semaforo

    distancia_percorrida = 0

    while distancia_percorrida < DISTANCIA_MAX:

        # Salto aleatório entre 1 e 5
        salto = random.randint(1, SALTO_MAX)

        distancia_percorrida = distancia_percorrida + salto

        # Evita ultrapassar a distância final
        if distancia_percorrida > DISTANCIA_MAX:
            distancia_percorrida = DISTANCIA_MAX

        print(f'{nome} pulou {salto} cm e percorreu {distancia_percorrida} cm')

        time.sleep(0.2)

        with semaforo:
            posicao.value += 1

            print(f'{nome} chegou ao final da corrida!'f'em {posicao}º lugar\n')


def main():   
    sapos = ['Sapo1', 'Sapo 2', 'Sapo 3', 'Sapo 4', 'Sapo 5']

    sem = multiprocessing.Semaphore(1)
    ranking = multiprocessing.Value('i', 0)
    with multiprocessing.Pool(processes=5, initializer=init, initargs=(sem, ranking)) as pool:
        pool.map(corrida, sapos)

if __name__ == '__main__':
    main()