import multiprocessing
import random
import time

semaforo_pista = None
semaforo_equipe = None


def init(sp, se):
    global semaforo_pista, semaforo_equipe

    semaforo_pista = sp
    semaforo_equipe = se

def corrida(carro):

    global semaforo_pista
    global semaforo_equipe

    nome, equipe = carro

    print(f'{nome} aguardando liberação')

    # Apenas 5 carros na pista
    with semaforo_pista:

        # Apenas um carro por equipe
        with semaforo_equipe[equipe]:

            print(f'{nome} ({equipe}) entrou na pista')

            for volta in range(1,4):
                tempo_volta = round(random.uniform(60,90),2)
                time.sleep(1)
                print(f'{nome} 'f'Volta {volta}: 'f'{tempo_volta}s')
            print(f'{nome} saiu da pista\n')

def main():
    carros = [('Ferrari 1','Ferrari'),('Ferrari 2','Ferrari'),('Mercedes 1','Mercedes'),('Mercedes 2','Mercedes'),('RedBull 1','RedBull'),('RedBull 2','RedBull'),('McLaren 1','McLaren'),('McLaren 2','McLaren'),('AstonMartin 1','AstonMartin'),('AstonMartin 2','AstonMartin'),('Alpine 1','Alpine'),('Alpine 2','Alpine'),('Williams 1','Williams'),('Williams 2','Williams')]

    pista = multiprocessing.Semaphore(5)

    equipes = {'Ferrari': multiprocessing.Semaphore(1),'Mercedes': multiprocessing.Semaphore(1),'RedBull': multiprocessing.Semaphore(1),'McLaren': multiprocessing.Semaphore(1),'AstonMartin': multiprocessing.Semaphore(1),'Alpine': multiprocessing.Semaphore(1),'Williams': multiprocessing.Semaphore(1)}

    with multiprocessing.Pool(processes=14, initializer=init, initargs=(pista, equipes)) as pool:
        pool.map(corrida, carros)

if __name__ == "__main__":
    main()