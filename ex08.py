import threading
import time
import random

fila = 30

s = threading.Semaphore(3)

def caixa(cliente_id):
    tempo_atendimento = random.randint(3, 10)
    print(f"Cliente {cliente_id} chegou e espera atendimento por {tempo_atendimento} segundos.")
    time.sleep(tempo_atendimento)
    print(f"Cliente {cliente_id} foi atendido.")

def clientes():
    for i in range(fila):
        cliente_id = i + 1
        threading.Thread(target=caixa, args=(cliente_id,)).start()
        time.sleep(random.uniform(0.1, 1.0))

clientes()