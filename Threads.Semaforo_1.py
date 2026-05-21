import multiprocessing
import time
import random

carro_parado: int = 0
carro_andando: int = 0
carro_chegando: int = 0
semaforo = None

def init(stop_car, running_car, finish_car, s):
    global carro_parado, carro_andando, carro_chegando, semaforo
    carro_parado = stop_car
    carro_andando = running_car
    carro_chegando = finish_car
    semaforo = s

def carro(id):
    global semaforo

    carro_chegando(id)
    #início seção crítica
    with semaforo:
        carro_andando(id)
    #fim seção crítica
    carro_parado(id)

def chegada(id):
    ordem = random.randint(1,4)

    if ordem == 1:
        sentido = "NORTE -> SUL"
    elif ordem == 2:
        sentido = "SUL -> NORTE"
    elif ordem == 3:
        sentido = "LESTE -> OESTE"
    else:
        sentido = "OESTE -> LESTE"

    print(f'{id} está chegando no cruzamento ({sentido})')

    time.sleep(random.uniform(0.5, 2))

def saida(id):
    print(f'{id} atravessando o cruzamento')
    time.sleep(2)
    print(f'{id} saiu do cruzamento')

def parado(id):
    print(f'{id} finalizou o percurso')

def main():
    carros = ['Carro azul', 'Carro amarelo', 'Carro verde', 'Carro vermelho']

    sem = multiprocessing.Semaphore(1)

    with multiprocessing.Pool(processes=4, initializer=init, initargs=(parado, saida, chegada, sem)) as pool:
        pool.map(carro, carros)


if __name__ == "__main__":
    main()