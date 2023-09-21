'''
Escreva um programa em Python, que simule a fila de atendimento de um banco.
O banco possui 3 caixas. O tempo de atendimento de cada cliente deve ser um
tempo aleatório entre 3 a 10 segundos. Suponha que a fila tenha um tamanho fixo
com 30 clientes em espera. Utilize um semáforo para fazer o gerenciamento dos
recursos compartilhados (caixas) entre os clientes (threads).
'''
from time import sleep
from random import randrange
from collections import deque
from threading import Thread, Semaphore


class Client:
    id: int
    
    def __init__(self, id: int) -> None:
        self.id = id


def attend(client: Client) -> None:
    global SEMAPHORE
    WAIT_TIME_MIN: int = 3
    WAIT_TIME_MAX: int = 10

    print(f'Client {client.id} is waiting to be attended...')
    SEMAPHORE.acquire()
    print(f'Started attending client {client.id}...')
    sleep(randrange(WAIT_TIME_MIN, WAIT_TIME_MAX))
    SEMAPHORE.release()
    print(f'Finished attending client {client.id}.')


def main() -> None:
    global CLIENTS

    # Build a queue of threads for each new client
    queue: deque[Thread] = deque()
    for i in range(CLIENTS):
        thread = Thread(target=attend, args=[Client(i + 1)])
        queue.append(thread)
    
    while queue:
        queue.popleft().start()
        #sleep(1) # Wait to next try attendiment


if __name__ == "__main__":
    RESOURCES_N: int = 3
    CLIENTS: int = 30
    SEMAPHORE = Semaphore(RESOURCES_N)
    main()
