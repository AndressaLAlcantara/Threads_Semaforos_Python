import multiprocessing
import time
import random
 
semaforo = None

def init(s):
    global semaforo
    semaforo = s

def pessoa(id):
    global semaforo

    velocidade = random.randint(4,6)      #cada pessoa anda de 4 a 6m/s

    tempo_corredor = 200/velocidade     #o corredor tem 200m | velocidade = deltaS / deltaT -> velocidade * deltaT = deltaS -> deltaT = deltaS/velocidade

    print(f'{id} começou a caminhar')
    print(f'Velocidade: {velocidade} m/s')

    time.sleep(tempo_corredor)

    print(f'{id} chegou à porta')

    with semaforo:

        print(f'{id} abriu a porta')

        tempo_porta = random.uniform(1,2)   #cada pessoa leva de 1 a 2s para abrir e cruzar a porta
        time.sleep(tempo_porta)

        print(f'{id} atravessou a porta')

    print(f'{id} finalizou o percurso\n')

def main():

    pessoas = ['Pessoa 1', 'Pessoa 2', 'Pessoa 3', 'Pessoa 4']

    sem = multiprocessing.Semaphore(1)

    with multiprocessing.Pool(processes=4, initializer=init, initargs=(sem,)) as pool:
        pool.map(pessoa, pessoas)

if __name__ == "__main__":
    main()
